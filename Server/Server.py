import socket
import time
from cryptography.fernet import Fernet

SERVER_IP = "0.0.0.0"
PORT = 9999

key = b'PASTE_YOUR_KEY_HERE'
cipher = Fernet(key)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print("Server listening...")

logs = []

count = 0
start = time.time()

MAX_LOGS = 100

while True:
    data, addr = sock.recvfrom(1024)
    
    try:
        message = cipher.decrypt(data).decode()
    except:
        continue

    timestamp = time.time()
    logs.append((timestamp, message))

    if len(logs) > MAX_LOGS:
        logs.pop(0)

    logs.sort(key=lambda x: x[0])

    print(f"[{addr}] {message}")

    count += 1

    if time.time() - start >= 1:
        print(f"Throughput: {count} logs/sec")
        count = 0
        start = time.time()