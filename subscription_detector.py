import pandas as pd

# 1️⃣ Load CSV
df = pd.read_csv("transactions.csv", encoding='utf-8')

# 2️⃣ Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 3️⃣ Normalize vendor names
df['vendor_norm'] = df['vendor'].str.lower().str.strip()

# 4️⃣ Detect recurring subscriptions
subscriptions = []
for vendor, g in df.groupby('vendor_norm'):
    dates = g['date'].sort_values().tolist()

    # Frequency & next payment calculation
    if len(dates) >= 2:
        gaps = [(dates[i+1]-dates[i]).days for i in range(len(dates)-1)]
        avg_gap = sum(gaps)/len(gaps)
        
        if 25 <= avg_gap <= 35:
            freq = "Monthly"
        elif 350 <= avg_gap <= 380:
            freq = "Annual"
        else:
            freq = "Unknown"
        
        next_payment = (dates[-1] + pd.Timedelta(days=round(avg_gap))).date()
    else:
        freq = "One-time"
        next_payment = "N/A"
        avg_gap = 0

    # Low usage detection
    distinct_employees = g['employee_email'].nunique()
    status = "Low usage" if distinct_employees <= 1 else "OK"

    subscriptions.append({
        "Vendor": g['vendor'].iloc[0],
        "Frequency": freq,
        "Avg Amount": round(g['amount'].mean(),2),
        "Next Payment (approx)": next_payment,
        "Status": status
    })

# 5️⃣ Output
subs_df = pd.DataFrame(subscriptions)

# Optional: Pretty print
try:
    from tabulate import tabulate
    print(tabulate(subs_df, headers='keys', tablefmt='psql'))
except:
    print(subs_df)

# Save to CSV
subs_df.to_csv("detected_subscriptions.csv", index=False)
print("\nDetected subscriptions saved to 'detected_subscriptions.csv'")
