# Distributed-Log-Aggregation-System
Course: Computer Networks – Socket Programming Mini Project

Students:
- Kundan V – PES1UG24CS243
- Kuncha Pranay Krishna – PES1UG24CS242
- Anusri Sharma – PES1UG25CS803

## Project Overview
This project implements a distributed log aggregation system using UDP socket programming. Multiple clients generate log messages and send them over the network to a centralized aggregation server. The server receives, orders, and processes logs in real time while supporting multiple concurrent clients.

The system also evaluates performance using throughput measurement and implements basic backpressure handling to prevent overload.

## Features
- UDP Socket Communication – Low-level socket implementation  
- Real-Time Log Streaming – Clients continuously send log data  
- Multi-Client Support – Multiple clients can send logs simultaneously  
- Time Ordering – Logs are ordered using timestamps  
- Throughput Evaluation – Server measures logs received per second  
- Backpressure Handling – Server queue limit prevents overload

## System Architecture
![Architecture](Architecture/Architecture.png)

Clients generate logs and send them to the server through the network using UDP sockets.  
The aggregation server receives and processes logs in real time.

## Communication Model
Client sends log message:  
`timestamp | client_id | log_level | message`  

Example:  
```1717578803.7720332 | WINDOWS_CLIENT | INFO | Log message 74```  

Server receives and processes logs while maintaining time ordering.

## Installation & Setup
Prerequisites:
- Python 3
- Devices connected to the same network
Setup Steps:
Clone the repository
```bash
git clone <your-repo-url>
cd Distributed-Log-Aggregation-System
```
Ensure Python is installed
```bash
python3 --version
```
Find server IP address (Mac)
```bash
ipconfig getifaddr en0
```
Update the server IP in client.py
```python
SERVER_IP = "YOUR_SERVER_IP"
```

## Usage
Start the Server:
```bash
python3 server.py
```
Expected output  

```Server listening...```  

Start the Client:
```bash
python client.py
```
Clients will start sending log messages continuously.  

Multi-Client Execution:  
Run multiple clients on different systems or terminals.  

Example:
```bash
python client.py
python client.py
python client.py
```
The server will receive logs from all clients simultaneously.

## Performance Evaluation
The server measures throughput as:  
```Throughput: XX logs/sec```  

This metric is used to evaluate system performance under continuous log transmission.

## Backpressure Handling
To prevent memory overload:
- Server log queue is limited to 100 logs
- Old logs are automatically removed when the limit is exceeded

This ensures stable performance even under heavy log traffic.

## Sample Output
Example server output:
```
[('10.30.203.57', 56672)] WINDOWS_CLIENT | INFO | Log message 74
[('10.30.203.57', 56672)] WINDOWS_CLIENT | INFO | Log message 76
Throughput: 25 logs/sec
```

## Technologies Used
Language: Python  
Networking: UDP Sockets  
Libraries: socket, time  
Operating Systems: Mac (Server), Windows/Ubuntu (Clients)

## Project Structure
```
Distributed-Log-Aggregation-System/
│
├── Architecture/
│   └── Architecture.png
├── Client/
│   └── Client.py
├── Output/
│   ├── Backpressure.png
│   ├── Client.jpeg
│   ├── Client_1.jpeg
│   ├── Client_2.jpeg
│   ├── Server.png
│   ├── Server_1_2.png
│   └── Throughput.png
├── Server/
│   └── Server.py
├── .gitignore
└── README.md
```

## Future Improvements
Secure communication using SSL/TLS  
Log storage in database  
Log filtering and search functionality  
Web dashboard for monitoring  
Visualization of log statistics

## License
This project is created for educational purposes as part of the Computer Networks mini project.

## Acknowledgments
Course: Computer Networks  
Institution: PES University  
Project Type: Socket Programming Mini Project
