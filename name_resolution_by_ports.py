import matplotlib.pyplot as plt

# Path to your text file
file_path = "name_resolutions_ports.txt"

# Read and parse file
counts = []
ports = []

with open(file_path, "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            count, port = parts
            counts.append(int(count))
            ports.append(port)

# ✅ Sort by count (largest first)
sorted_pairs = sorted(zip(counts, ports), reverse=True)
counts_sorted, ports_sorted = zip(*sorted_pairs)

# Create horizontal bar chart with raw values
plt.figure(figsize=(10, 5))
bars = plt.barh(ports_sorted, counts_sorted, color='skyblue')

plt.xlabel("Number of Name Resolutions")
plt.ylabel("Protocal Name")
plt.title("Name Resolution Counts by protocol")
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate bars with counts
for i, v in enumerate(counts_sorted):
    plt.text(v + max(counts_sorted) * 0.01, i, str(v), va='center', fontsize=9)

# ✅ Reverse y-axis so largest value appears at the top
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()
