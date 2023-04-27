# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess
from time import sleep

# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nJawairia Malik (Jojo)")
print("Partner: Lucas and Ren")
print("Program Name: Competition")
print("Date: 4/24/2023")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")
        """
        sendmsg('command', 0)
        sendmsg('takeoff',0)
        sendmsg('up 20', 0)
        sendmsg('go 10 11 12 13 ')
       # sendmsg('up 50')
       # sendmsg('forward 200')
       # sendmsg('up 50')
        #sendmsg('left 20')
       # sendmsg('forward 220')
        # sendmsg('go 220 -20 30 50', 8)
        #sendmsg('curve -100 150 0 -100 0 0 40')
        sendmsg('land')
        """

        sendmsg('command, 0')
        sendmsg('takeoff, 0')
        sendmsg('go 50 50 50 55', 0)
        #sendmsg('forward 220', 0)
        #sendmsg('curve -100 150 0 -100 0 0 55', 0)
        #sendmsg('forward 220')
        sendmsg('land', 0)






        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()