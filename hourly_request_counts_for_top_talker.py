import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data
df = pd.read_csv("top_talker_hourly_dns_counts.txt", sep=r"\s+", names=["Count", "ClientIP", "HourBin"])

# Convert HourBin (hours since epoch) to datetime
df["Timestamp"] = df["HourBin"].apply(lambda h: datetime.utcfromtimestamp(h * 3600))

# Sort by time
df = df.sort_values("Timestamp")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df["Timestamp"], df["Count"], marker="o", linewidth=2)
plt.title("DNS Requests per Hour for the busiet machine")
plt.xlabel("Time (UTC)")
plt.ylabel("Number of DNS Requests")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
