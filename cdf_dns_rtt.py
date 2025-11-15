import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("DNS_RTT.csv")

#
ttl_values = df['RTT'].dropna().values

#concert to millseconds


# Sort the values
rtt_sorted = np.sort(ttl_values)

# Compute CDF
cdf = np.arange(1, len(rtt_sorted) + 1) / len(rtt_sorted)


# Create plot
plt.figure(figsize=(8, 6))

plt.plot(rtt_sorted, cdf, linewidth=1)   # <-- reduce linewidth to make the line thinner

# X-axis in log scale with custom ticks
plt.xscale("log")
plt.xticks([1,3, 6, 12, 24], ["1","3", "6", "12", "24"])

# Y-axis ticks
plt.yticks(np.arange(0.1, 1.1, 0.1))

plt.xlabel("Recursive lookup RTT (Seconds)")
plt.ylabel("CDF")
plt.title("Recursive RTT  ")

plt.grid(True, which="both", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
