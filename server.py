import socket
import threading

class Server:

    def __init__(self, host='127.0.0.1', port=1234, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.port = port
        self.host = host

    # Associate the socket with the IP address
    def bind_and_listen(self):
        try:
            self.sock.bind((self.host, self.port))
            print(f"Server Démarrer sur {self.host}:{self.port}")
            self.sock.listen(5)  # Listen for up to 5 connections
        except Exception as e:
            print(f"Error au démarrage: {e}")
            self.sock.close()

    # Accept the client connection
    def accept_connection(self):
        try:
            client_socket, client_address = self.sock.accept()
            print(f"Connection etablie avec : {client_address}")
            return client_socket, client_address
        except Exception as e:
            self.sock.close()
            print("Server socket close")
            return None, None

    def close_socket(self):
        self.sock.close()
        print("Socket closed successfully")

    # Handle client communication
    def handle_client(self, client_socket, client_address):
        try:
            client_socket.send("Welcome to the server!".encode())
                
        except Exception as e:
            print(f"Error with client {client_address}: {e}")

        
    def runServer(self):
        self.bind_and_listen()

        while True:
            client_socket, client_address = self.accept_connection()
            if client_socket:
                # Start a new thread for each client
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_handler.start()


