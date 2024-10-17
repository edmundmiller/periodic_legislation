# /// script
# requires-python = "<3.13"
# dependencies = [
#   "requests",
#   "dspy-ai",
# ]
# ///

import csv
import requests
import dspy
import time

# Set up DSPy
dspy.settings.configure(lm=dspy.OpenAI(model='gpt-3.5-turbo'))

def fetch_bill_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching bill text: {e}")
        return None

class SummarizeBills(dspy.Signature):
    """Analyze bills related to period care and feminine hygiene products."""

    state = dspy.InputField()
    bill_texts = dspy.InputField()
    vibe = dspy.OutputField(desc="Overall 'vibe' or sentiment of the legislation for period care in this state")

class BillAnalyzer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.summarize = dspy.Predict(SummarizeBills)

    def forward(self, state, bill_texts):
        result = self.summarize(state=state, bill_texts=bill_texts)
        return result.vibe

def main():
    states = {}
    with open('sources/legiscan/bills.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['state'] not in states:
                states[row['state']] = []
            states[row['state']].append(row)

    analyzer = BillAnalyzer()
    results = []

    for state, bills in states.items():
        print(f"Processing {state}...")
        bill_texts = []
        for bill in bills:
            text = fetch_bill_text(bill['text_url'])
            if text:
                bill_texts.append(f"Bill {bill['bill_number']}: {text[:1000]}...")  # Truncate to first 1000 chars

        vibe = analyzer(state, ' '.join(bill_texts))
        results.append({'state': state, 'vibe': vibe})
        time.sleep(1)  # Be nice to the API

    with open('sources/state_period_care_vibes.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['state', 'vibe'])
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    main()
