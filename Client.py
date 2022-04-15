import socket, threading

FADDR = input("Enter your friend's addr: ")
PORT = 4444
IP = #<change this to server ip>
ADDR = (IP, PORT)

cl_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #start the tcp connection
cl_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #start the udp connection

cl_tcp.connect(ADDR) #connect to the server
cl_udp.bind(("", PORT+2)) #start the udp as host

cl_tcp.send(FADDR.encode("utf-8"))
print("[*] Waiting for your friend to join!")
#waits for the servers response and ack-syn
ack = cl_udp.recv(1024).decode("utf-8")
if ack == "!Success":
	print("[+] Success! Your friend is online")

	def send_msgs():
		connected = True
		while connected:
			msg = input("Msg: ")
			if msg.lower() == "exit" or msg.lower() == "quit":
				connected = False
			cl_tcp.send(msg.encode("utf-8"))
		print("[!] You disconnected from the server")

	def recv_msgs():
		connected = True
		while connected:
			inc_msg = cl_udp.recv(1024).decode("utf-8")
			if inc_msg.lower() == "exit" or inc_msg.lower() == "quit":
				connected = False
			print(f"\n[{FADDR}]: {inc_msg}")
		print("[!] Your friend has left the chat!")

	recv_msgs_thread = threading.Thread(target=recv_msgs)
	recv_msgs_thread.start()
	send_msgs() #definition or function

else:
	print("[!] Your friend failed to connect")
