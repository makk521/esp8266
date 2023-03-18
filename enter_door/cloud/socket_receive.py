import socket

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.0.12.13', 7789)  # Listen on localhost, port 8000
server_socket.bind(server_address)
server_socket.listen(1)

print('Waiting for connection...')

# Wait for a client to connect
client_socket, client_address = server_socket.accept()
print('Connection from', client_address)

# Receive and process incoming data
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print('Received:', data.decode())

# Clean up the connection
client_socket.close()
server_socket.close()
