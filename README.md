# Sockets-ChatApp
Socket-ChatApp is a basic server and client communication system between two nodes on a network. One socket(node) listens on a particular port at an IP, while the other attempts to connect with that socket to form a connection. My application specifically imitates chat programs like WhatsApp, where users can direct message other users just by their IP addresses. A host is required to run server.py at all times, and anyone interested can use the client.py to establish a connetion with another user using client.py. 

# How To Install
- git clone https://github.com/CuriousAvenger/Sockets-ChatApp
- python3 server.py or client.py # Python3 Required

# How To Use
- A host is required to run server.py, to which our clients will connect. 
- Change the variable 'IP' in client.py to the server's IP address. 
- Use ipconfig for windows or ifconfig for mac/linux to get the IP addr. 
- After client & server connects, specify the IP of your friend & vice versa.
- This enables communication between 2 users, and to quit, type 'quit'.

# Error Handling
- Make sure the two users are **not** from the same device, else the ChatApp will crash.
- If you run into a forever loop, use task manager to kill python to exit the ChatApp. 
