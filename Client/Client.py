import socket
import time
import random

SERVER_IP = "10.30.200.145"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_id = "WINDOWS_CLIENT"

while True:
    log = f"{time.time()} | {client_id} | INFO | Log message {random.randint(1,100)}"
    sock.sendto(log.encode(), (SERVER_IP, PORT))
    print("Sent:", log)
    time.sleep(1)