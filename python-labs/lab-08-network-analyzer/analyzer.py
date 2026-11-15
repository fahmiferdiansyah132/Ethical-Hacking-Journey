from collections import Counter

ip_counter = Counter()

with open("network.log", "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) == 2 and parts[1] == "CONNECTION":
            ip_counter[parts[0]] += 1

print("=== NETWORK SECURITY ANALYSIS ===")

for ip, total in ip_counter.most_common():
    if total >= 3:
        print(f"[WARNING] {ip} memiliki {total} koneksi")
    else:
        print(f"[NORMAL] {ip} memiliki {total} koneksi")
