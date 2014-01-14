#!/usr/bin/python
import sys
import socket

# TODO - Multi-threaded support
# TODO - Port as command line option
# TODO - Scheme for targets of messages
# TODO - Queue of messages received
# TODO - Message Polling from Clients

def run_server(_host = '', _port=5151):
	
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("* Socket Created")
	try:
		serversocket.bind((_host,_port))
	except socket.error as msg:
		print("E Bind Failed.\nE\t%s" % str(msg))
		sys.exit(1)
	print("* Socket Bind Complete")
	serversocket.listen(5)
	print("* Socket Now Listening on Port %s" % str(_port))

	while True:
		(clientsocket, address) = serversocket.accept()
		print("* Connected with %s:%s" % (str(address[0]), str(address[1])))

		data = clientsocket.recv(1024)
		if not data:
			break

		print("# Received: %s" % str(data))
		
		response = "Thank you!\n"
		clientsocket.sendall(response.encode("utf-8"))
		print("* Gave Thanks")
		
		clientsocket.close()
		print("* Client Closed")
	
	serversocket.close()
	print("* All Sockets Closed")
	sys.exit(0)

if __name__ == "__main__":
	run_server()
