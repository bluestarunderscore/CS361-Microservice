import socket
import pickle
import pandas as pd

###############################################################
# Example client interaction with service                     #
# - Sends "give" to microservice, microservice will respond   #
#   with pandas DataFrame.                                    #
#                                                             #
###############################################################
def get_mushroom_data(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1",port))
    # print("Connected to microservice on port", port)
    request_msg = "give"
    close_msg = "close"
    client_socket.sendall(request_msg.encode())
    response = client_socket.recv(2048)
    full_response = pickle.loads(response)
    print(full_response)
    client_socket.sendall(close_msg.encode())
    client_socket.close()

    #Send message to shut server down. Requires another connection.
    
    
    #client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client_socket.connect(("127.0.0.1",port))
    
    #client_socket.close()
    

def main():
    get_mushroom_data(1100)

if __name__ == "__main__":
    main()

