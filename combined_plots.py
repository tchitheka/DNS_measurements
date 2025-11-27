import pandas as pd
import matplotlib.pyplot as plt

# ----------------- FIRST PLOT DATA -----------------
df = pd.read_csv("DNS_resolvers_detailed.csv")
category_counts = df['Category'].value_counts(normalize=True)

# ----------------- SECOND PLOT DATA ----------------
requests = pd.read_csv('dns_requests_by_category.csv')
responses = pd.read_csv('dns_requests_succseede_by_category.csv')
requests = requests.rename(columns={'TotalRequests':'RequestsMade'})
responses = responses.rename(columns={'TotalRequests':'SuccessfulResponses'})
combined = pd.merge(requests, responses, on='Category', how='outer').fillna(0)
combined['SuccessRate(%)'] = (combined['SuccessfulResponses'] /
                              combined['RequestsMade']) * 100

# ----------------- PLOT BOTH IN ONE FIGURE -----------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))  # 1 row, 2 columns

BAR_WIDTH = 0.4   # ← change this to your preferred bar thickness

# --- Left plot ---
axes[0].bar(category_counts.index, category_counts.values,
            color=['#1f77b4', "#0b4658", "#11121D"],
            width=BAR_WIDTH)
axes[0].set_title("NS lookup requests")
axes[0].set_ylabel("Proportion")
axes[0].set_xlabel("DNS Server location")

for i, v in enumerate(category_counts):
    axes[0].text(i, v + 0.01, f"{v:.2%}", ha='center', fontweight='bold')

# --- Right plot ---
axes[1].bar(combined['Category'], combined['SuccessRate(%)'],
            color=['#1f77b4', '#0b4658', '#11121D'],
            width=BAR_WIDTH)
axes[1].set_title("DNS Success rate by category")
axes[1].set_ylabel("Success Rate (%)")
axes[1].set_xlabel("DNS Server location")
axes[1].set_ylim(0, 110)

for i, v in enumerate(combined['SuccessRate(%)']):
    axes[1].text(i, v + 2, f"{v:.1f}%", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
