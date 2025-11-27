import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("DNS_resolvers_detailed.csv")

# Compute normalized counts (proportions)
category_counts = df['Category'].value_counts(normalize=True)  # normalize=True gives fractions

# Plot bar chart
plt.figure(figsize=(6,4))
category_counts.plot(kind='bar', color=['#1f77b4',"#0b4658","#11121D"])
plt.title("Proportion of DNS Servers by Category")
plt.ylabel("Proportion")
plt.xlabel("Category")
plt.xticks(rotation=0)

# Add percentage labels on top of each bar
for i, v in enumerate(category_counts):
    plt.text(i, v + 0.01, f"{v:.2%}", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
