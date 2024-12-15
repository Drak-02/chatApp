import socket

#
class Client :

    def __init__(self, host='127.0.0.1', port=1234):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try: #try to connect to the server 
            self.sock.connect((self.host, self.port))
            print(f'Connection Avec Succès au Server : {self.host}:{self.port}')
        except Exception as e:
            print(f'Erreur de connexion au server!{e}')
    
    def close_sock(self):
        self.sock.close()
        print(f'Déconnexion averc Succès au Server : {self.host}:{self.port}')