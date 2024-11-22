import re
import socket
from threading import Thread


# Function to handle incoming connections
def handle_connection(conn, addr):
    try:
        data = conn.recv(1024).decode('utf-8')
        # Regular expression to check for suspicious patterns
        suspicious_pattern = re.compile(r'(password|secret|token)')
        match = suspicious_pattern.search(data.lower())
        if match:
            print(f'Suspicious data received from {addr}: {data}')
        else:
            print(f'Data received from {addr}: {data}')
    finally:
        conn.close()


# Create a TCP server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 5000)
print(f'Starting server on {server_address}')
s.bind(server_address)
s.listen(5)

# Accept incoming connections in a loop
while True:
    conn, addr = s.accept()
    print(f'Connected with {addr}')
    # Start a new thread to handle the incoming connection
    thread = Thread(target=handle_connection, args=(conn, addr))
    thread.daemon = True
    thread.start()
