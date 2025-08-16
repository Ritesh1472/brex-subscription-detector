# brex-subscription-detector
Recurring Subscription Detector
What it Does
This project helps companies keep track of their subscriptions automatically. It detects recurring payments, calculates average amounts, predicts the next payment date, and flags subscriptions that are rarely used.
Features
Detects if a subscription is Monthly, Annual, or One-time
Predicts next payment date
Highlights low usage subscriptions (used by only 1 employee)
Shows average amount spent per vendor
Saves results to a CSV file
Input CSV Format
Your CSV should look like this:
date,vendor,amount,description,employee_email,payment_method
date  YYYY-MM-DD
vendor  Name of the service (e.g., Zoom, Slack)
amount  Transaction amount
employee_email  Employee who paid
How to Use
Put transactions.csv in the project folder
Run the script:
python subscription_detector.py
Output:
Console table showing subscriptions
detected_subscriptions.csv saved automatically
Requirements
Python 3Pandas
Optional: Tabulate for prettier table (pip install tabulate)
