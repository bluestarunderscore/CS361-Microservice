# CS361-Microservice
As a preface, I use the terms "microservice" and "server" interchangeably within this document, as this microservice is effectively a server program.
The microservice returns a DataFrame with random mushroom attributes. Connections to the microservice are done using the socket library and the DataFrame is sent via pickling.

In short, the following must be done to use the microservice:
  1. Start the random_mushroom.py microservice file (feel free to change the port). The server will announce it has started on LOCALHOST on the specified port.
  2. In the client, create a python socket with socket.AF_INET and socket.SOCK_STREAM as parameters and bind it to 127.0.0.1 (localhost) and the port used by the microservice.
  3. Connect to the microservice using the socket.
  4. Run commands (more detail on these below) as necessary.
  5. Close the socket connection (make sure to send "close" to the microservice so it stops as well)

## Microservice Commands ##
There are two valid commands for the microservice: "give" and "close". The "give" command tells the microservice to send the DataFrame, and the "close" command signals the server to close the connection and stop running. The server will not shut down until it receives this command. These commands must be sent as bytestrings over a connection socket. Below is a short code snippet showing how to send the commands to the microservice:

```
request = "give" # can be "give" or "close", note that close will stop the microservice
socket_name.sendall(request.encode())
```


## Handling the Received Data ##
When the DataFrame is sent by the server, the main program should be ready to receive it using recv(). I used 2048 bytes as the recv argument in example_call.py and it seems to fit all of the data; raise this number if it does not. After receiving the data, use pickle.loads() on it to unpack it back into a DataFrame usable by the Pandas library. Below is a short code snippet showing how to handle the received data:
```
received_data = socket_name.recv(2048)
unpacked_data = pickle.loads(received_data)
```

UML Sequence Diagram:
![UML](https://github.com/bluestarunderscore/CS361-Microservice/assets/157440828/26ce5036-159b-4b88-878e-624f41f272b6)
(Note: I apologize for some styling issues in the UML, I could not find how to signify loops and deletions in Visual Paradigm and added them afterward.



