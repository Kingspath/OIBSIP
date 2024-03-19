import socket

SERVER_HOST = 'localhost'  # The server's hostname or IP address.
SERVER_PORT = 1234       # The port used by the server.

def connect_to_server(): # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.connect((SERVER_HOST, SERVER_PORT)) # Connect to the server
        print("Connected to the server!")
        while True:
            data = input("Enter the data to send to the server: ")
            s.sendall(data.encode('utf-8')) # Send data to the server
            if data == "exit": # If the data is "exit", then break the loop
                break
            
            data = s.recv(1024).decode('utf-8') # Receive data from the server
            print(data) # Print the received data
            
if __name__ == "__main__":
    connect_to_server() # Call the function to connect to the server
    
# Instructions to run the code:

# 1. Run the server code first in one terminal.

# 2. Run multiple client code in different terminal windows to begin chatting.
        