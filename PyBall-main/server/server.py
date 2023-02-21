import socket
import pickle
from _thread import *
from network import get_ip
class pyBallServer:
    
    def __init__(self,stadium):
        
        self.port = 5555
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.gamesettings = {
            "stadium" : None,
            "players" : {},
            "redteam" : [],
            "blueteam" : []
        }
            
        

        try:
            self.serverSocket.bind(("localhost", self.port))
        except socket.error as e:
            str("Error")






        self.serverSocket.listen()
        print("Waiting for a connection, Server Started")




    def newClient(self,connection, player):
        connection.send(str.encode("received"))
        
        while True:
            try:
                data = connection.recv(4096).decode()
                #first data received should  be the player name,

             
                    

                
            except:
                break

        print("Lost connection")
        try:
            print("deleting", player)
            del self.gamesettings["players"][player]
        except:
            pass
        connection.close()


    def connectionChecker(self):
        
        connection, address = self.serverSocket.accept()
        print("connected to:", address)
        


        start_new_thread(threaded_client, (connection, player, gameId))


   
 
servernew = pyBallServer("smallStadium")
 
while True:
    servernew.connectionChecker()
