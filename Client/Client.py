import socket
import time
import random
from cryptography.fernet import Fernet

SERVER_IP = "YOUR_SERVER_IP"
PORT = 9999

key = b'PASTE_YOUR_KEY_HERE'
cipher = Fernet(key)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_id = "WINDOWS_CLIENT"

while True:
    log = f"{time.time()} | {client_id} | INFO | Log message {random.randint(1,100)}"
    
    encrypted_log = cipher.encrypt(log.encode())
    
    sock.sendto(encrypted_log, (SERVER_IP, PORT))
    
    print("Sent:", log)
    
    time.sleep(1)