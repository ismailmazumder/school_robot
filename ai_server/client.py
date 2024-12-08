import socket

host = "192.168.4.1"  # ESP8266's IP
port = 1234           # Port number

# Create a socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Connected to ESP8266")

while True:
    # Send a message
    message = input("You: ")
    if message.lower() == "exit":
        break
    client_socket.sendall((message + "\n").encode())

    # Receive a response
    response = client_socket.recv(1024).decode()
    print(response)

client_socket.close()
