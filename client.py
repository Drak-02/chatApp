import socket
import threading

class Client:

    def __init__(self, host='127.0.0.1', port=1234):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            # Connexion au serveur
            self.sock.connect((self.host, self.port))
            print(f'Connexion réussie avec le serveur : {self.host}:{self.port}')
            
            self.sendClient()  # Envoi initial
            threading.Thread(target=self.receiveClient, daemon=True).start()
            self.start_discussion()
        except Exception as e:
            print(f'Erreur de connexion au serveur: {e}')

    def close_sock(self):
        self.sock.close()
        print(f'Déconnexion réussie du serveur : {self.host}:{self.port}')

    def sendClient(self): # donnée le information de l'utilisateur pour qu'il se connecter
        nom = str(input("Nom: "))
        prenom = str(input("Prénom: "))
        email = str(input("Email: "))
        message = f" Connection Client,{nom},{prenom},{email}"  # Message à envoyer
        self.sock.send(message.encode())  # Envoi du message encodé en bytes
        print("Message envoyé au serveur.")

    def receiveClient(self):
        while True:
            response = self.sock.recv(1024)
            print("Message reçu du serveur:", response.decode())

    def start_discussion(self):
        while True:
            message = input("->: ")
            if message.lower() == "exit":
                break
            elif message.lower() == "@unichat":
                pass
            elif message.lower() == "@multicast":
                pass
            elif message.lower() == "@diffusion":
                pass
            self.sock.send(message.encode())  
            print(f"Message envoyé : {message}")
           

client = Client()
client.connect()  # Démarre la connexion et la discussion
client.close_sock()  # Déconnecte du serveur après la discussion
