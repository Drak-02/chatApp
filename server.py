import signal
import socket
import sys
import threading

class Server:
    total_ligne = {} # pour Stocker les informations du client avec un identifiant

    def __init__(self, host='127.0.0.1', port=1234, server=None):
        if server is None:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.server = server
        self.port = port
        self.host = host

    def bind_and_listen(self):
        try:
            # On lie le socket à l'adresse IP et au port
            self.server.bind((self.host, self.port))
            print(f"Serveur démarré sur {self.host}:{self.port} ...")
            # Le serveur écoute les connexions entrantes jusqu'à 5 connexions
            self.server.listen(5)
        except Exception as e:
            print(f"Erreur lors du démarrage du serveur : {e}")
            self.server.close()

    def accept_connection(self):
        try:
            # Accepter une connexion entrante, renvoie un socket et l'adresse du client
            client_socket, client_address = self.server.accept()
            print(f"Connexion établie avec : {client_address}")
            return client_socket, client_address
        except Exception as e:
            print(f"Erreur lors de l'acceptation de la connexion : {e}")
            self.server.close()
            return None, None

    def close_socket(self):
        self.server.close()
        print("Le socket du serveur a été fermé avec succès.")

    def handle_client(self, client_socket, client_address):
        try:
            if self.verifierClient(client_socket.recv(4096).decode('utf-8')): # si vrai que le client est autoriser effectuer la connexion
                print("Client Vérifier avec succès")
                while True :
                        request = client_socket.recv(4096)  
                        if not request:
                            print(f"Le client {client_address} a fermé la connexion.")
                            break

                        try:
                            print(f"Récu du client : {client_address} : {request.decode('utf-8')}")
                        except UnicodeDecodeError :
                            print(f"Erreur message client: {client_address}")
                            client_socket.send("Erreur de décodage.".encode('utf-8'))
            else:
                client_socket.close()
        except Exception as e:
            # En cas d'erreur pendant la gestion du client
            print(f"Erreur avec le client {client_address}: {e}")
        finally:
            # Toujours fermer la connexion client à la fin
            client_socket.close()
            print(f"Connexion avec {client_address} fermée.")

    def runServer(self):
        """
        Démarre le serveur et accepte les connexions entrantes.
        Pour chaque connexion, un nouveau thread est lancé pour gérer le client.
        """
        # Démarrer à écouter les connexions
        self.bind_and_listen()

        while True:
            # Attendre une connexion client
            client_socket, client_address = self.accept_connection()
            if client_socket:
                # Lancer un nouveau thread pour chaque client qui se connecte
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_handler.start()
    def verifierClient(self,message="inconnues"): # nom, prenom, email
        print(f"Infos a vérifier :{message} ")
        infosClient = message.split(',')
        #print(type(s))
        for x in infosClient:
            print(x)
        #Vérifier les informations du client avant qu'il comment discussiiobn
        return True

# Créer et démarrer le serveur
server = Server()
server.runServer()


