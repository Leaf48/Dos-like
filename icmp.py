from scapy.all import *

ip = ""

ip_layer = IP(dst="")
icmp_layer = ICMP(seq=9999)

packet = ip_layer / icmp_layer
send(packet)