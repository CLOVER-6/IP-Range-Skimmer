import sys
from ping3 import ping
import ipaddress

iprange = sys.argv[1]
file_to_store = sys.argv[2]
net4 = ipaddress.ip_network(iprange)


print("Skimming IPs...")

for x in net4.hosts():
    resp = ping(str(x), timeout=0.5)

    if resp == None:
        continue
    elif isinstance(resp, float):
        print(str(x))
        with open(file_to_store, "a") as opened:
            opened.write(f"{str(x)}\n")
    else:
        continue
