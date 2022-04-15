import socket, threading

FADDR = {}
PORT = 4444
IP = "0.0.0.0"
ADDR = (IP, PORT)

sr_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #start the tcp connection
sr_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #start the udp connection

sr_tcp.bind(ADDR) #connect to the server
sr_udp.bind(("", PORT+1)) #start the udp as host

print("[+] Server is starting")
def start_accept_connections():
	print(f"[*] Listeneing on {ADDR[0]}:")
	sr_tcp.listen()
	while True:
		fr_value = 0
		conn, addr = sr_tcp.accept()
		for i in FADDR:
			if addr[0] == FADDR[i]:
				fr_value = i
				ack_msg = "!Success".encode("utf-8")
				sr_udp.sendto(ack_msg, (fr_value, PORT+2))
				ignore = conn.recv(1024)
				sr_udp.sendto(ack_msg, (addr[0], PORT+2))
			else:
				fr_value = 0

		thread = threading.Thread(target=handle_clients, args=(conn, addr, fr_value))
		thread.start()
		print(f"[*] Active connections: {threading.activeCount() - 1}")

def handle_clients(conn, addr, fr_value):
	global FADDR
	print(f"[+] {addr[0]} connected on port {addr[1]}")
	if fr_value != 0:
		del FADDR[fr_value]
	else:
		msg_fddr = conn.recv(1024).decode("utf-8")
		FADDR[addr[0]] = msg_fddr
		fr_value = msg_fddr

	while True:
		msg = conn.recv(1024).decode("utf-8")
		sr_udp.sendto(msg.encode("utf-8"), (fr_value, PORT+2))
		if msg.lower() == "exit" or msg.lower() == "quit":
			break
	print(f"[+] {addr[0]} disconnected")
	conn.close()

start_accept_connections()
