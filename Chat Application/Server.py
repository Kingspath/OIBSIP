import socket # Import the socket module
import threading # Import the threading module


SERVER_HOST = 'localhost' # The server's hostname or IP address.
SERVER_PORT = 1234 # The port used by the server.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

server_socket.bind((SERVER_HOST, SERVER_PORT)) # Bind the server to the host and port

server_socket.listen() # Listen for incoming connections

client_list = [] # Create an empty list to store the clients

clients = []

def handle_client(client_socket, client_address): # Function to handle the client
    while True: # Loop to keep the connection with the client
        try: # Try to receive data from the client
            message = client_socket.recv(1024).decode('utf-8') # Receive data from the client
            if message: # If the message is not empty
                print(f"[{client_address[0]}:{client_address[1]}]: {message}") # Print the message
                broadcast(message, client_socket) # Broadcast the message to all the clients
            else: # If the message is empty
                remove(client_socket) # Remove the client from the list
        except: # If there is an error
            remove(client_socket) # Remove the client from the list
            break # Break the loop

def broadcast(message, sender_socket): # Function to broadcast the message to all the clients
    for client in clients: # Loop through all the clients
        if client != sender_socket: # If the client is not the sender
            client.send(message.encode('utf-8')) # Send the message to the client

def remove(client_socket): # Function to remove the client from the list
    if client_socket in clients: # If the client is in the list
        clients.remove(client_socket) # Remove the client from the list

def accept_connections(): # Function to accept connections from the clients
    while True: # Loop to keep accepting connections
        client_socket, client_address = server_socket.accept() # Accept the connection from the client
        clients.append(client_socket) # Add the client to the list
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address)) # Create a thread to handle the client
        client_thread.start() # Start the thread

print("Server started. Waiting for connections...") # Print a message to indicate that the server has started


accept_thread = threading.Thread(target=accept_connections) # Create a thread to accept connections
accept_thread.start() # Start the thread