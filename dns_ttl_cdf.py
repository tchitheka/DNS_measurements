import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("dns_ttls_port53_v2.csv")

# Assuming the TTL column is named 'ttl'
# If the column name is different, change 'ttl' accordingly
ttl_values = df['max_TTL'].dropna().values

# Sort the values
ttl_sorted = np.sort(ttl_values)

# Compute CDF
cdf = np.arange(1, len(ttl_sorted) + 1) / len(ttl_sorted)

# Create plot
plt.figure(figsize=(8, 6))

plt.plot(ttl_sorted, cdf, linewidth=1)   # <-- reduce linewidth to make the line thinner

# X-axis in log scale with custom ticks
plt.xscale("log")
plt.xticks([1,10, 100, 1000, 10000], ["1","10", "100", "1000", "10000"])

# Y-axis ticks
plt.yticks(np.arange(0.1, 1.1, 0.1))

plt.xlabel("Maximum TTL Values (Seconds)")
plt.ylabel("CDF")
plt.title("CDF of Maximum TTL  ")

plt.grid(True, which="both", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
