import socket
import sys

# Creating the socket
s = socket.socket()
print("Socket successfully created.")

# Reserving a port on machine
port = 3004

# Binding the port
s.bind(("", port))

# Putting the socket into listening mode
s.listen(1)
print("Socket in listening mode.")

# Process placed inside a loop until there is an interruption, i.e. error

while True:
    c, address = s.accept()
    print("Connection established from", address)

#     Sending a message to the client, encoding to send byte type
    c.send("George Russell WDC 2022 confirmed.".encode())
    c.close()

    break

#     Test comment

