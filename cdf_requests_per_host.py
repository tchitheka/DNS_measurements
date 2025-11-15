import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === 1. Load CSV file ===
df = pd.read_csv('dns_requests_per_client.csv')

# === 2. Extract and sort request counts ===
counts = np.sort(df['Request_Count'])

# === 3. Compute the CDF ===
cdf = np.arange(1, len(counts) + 1) / len(counts)

# === 4. Plot CDF ===
plt.figure(figsize=(8, 5))
plt.plot(counts, cdf, marker='.', linestyle='-', color='b',linewidth=0.5)

# === 5. Configure log-scale x-axis ===
plt.xscale('log')
plt.xticks([1, 10, 100, 1000, 10000, 100000],
           ['1', '10', '100', '1k', '10k', '100k'])
plt.minorticks_off()

# === 6. Set y-axis ticks (0.1 to 1.0) ===
plt.yticks(np.arange(0.1, 1.1, 0.1))

# === 7. Labels and styling ===
plt.title('CDF of DNS Requests per Client')
plt.xlabel('Number of DNS Requests (per client)')
plt.ylabel('Cumulative Probability')
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# === 8. Show plot ===
plt.tight_layout()
plt.show()
