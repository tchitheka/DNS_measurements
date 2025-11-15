import pandas as pd
import matplotlib.pyplot as plt

# === 1. Load your two CSV files ===
requests = pd.read_csv('dns_requests_by_category.csv')          # total DNS requests
responses = pd.read_csv('dns_requests_succseede_by_category.csv')  # successful DNS responses

# === 2. Rename columns for clarity ===
requests = requests.rename(columns={'TotalRequests': 'RequestsMade'})
responses = responses.rename(columns={'TotalRequests': 'SuccessfulResponses'})

# === 3. Merge both datasets by category ===
combined = pd.merge(requests, responses, on='Category', how='outer').fillna(0)

# === 4. Compute success rate (%) per category ===
combined['SuccessRate(%)'] = (combined['SuccessfulResponses'] / combined['RequestsMade']) * 100

# === 5. Plot Success Rate per Category ===
plt.figure(figsize=(8, 5))
plt.bar(combined['Category'], combined['SuccessRate(%)'], color=['#4C72B0', '#55A868', '#C44E52'])

# Add labels and title
plt.ylabel('Success Rate (%)')
plt.xlabel('DNS Server Category')
plt.title('DNS Success Rate by Category')
plt.ylim(0, 110)  # slightly above 100% for spacing

# Add value labels on top of each bar
for i, v in enumerate(combined['SuccessRate(%)']):
    plt.text(i, v + 2, f"{v:.1f}%", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
