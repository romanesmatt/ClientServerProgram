import socket

# Creating the socket
s = socket.socket()
print("Socket successfully created.")

# Reserving a port on machine
port = 3004

s.connect(("127.0.0.1", port))

# Receiving data from the server and decoding it to get the string
print(s.recv(1024).decode())

# Closing the connection
s.close()
print("Connection closed.")