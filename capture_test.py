
from scapy.all import *

print("Capturing 10 packets...")

packets = sniff(count=10)

print(f"Captured {len(packets)} packets!")