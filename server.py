import socket


def main():
	# next create a socket object
	s = socket.socket()
	print ("Socket successfully created")

	# reserve a port on your computer in our
	port = 8080
	
	# Next bind to the port
	# we have not typed any ip in the ip field
	# instead we have inputted an empty string
	# this makes the server listen to requests
	# coming from other computers on the network
	s.bind(('', port))
	print ("socket binded to %s" %(port))

	# put the socket into listening mode
	s.listen(5)
	print ("socket is listening")

	# a forever loop until we interrupt it or
	# an error occurs

	while True:
		# Establish connection with client.
		c, addr = s.accept()
		print ('Connected to ', addr )
		# send a thank you message to the client. encoding to send byte type.
		c.send('I am the main server'.encode())
		# Close the connection with the client
		c.close()
		# Breaking once connection closed
		break

if __name__ == "__main__":
	main()

# Create a thread which will only save the last connected IPs
# Use dictionary for faster shearch
# Auto update function ( deletes the IPs which connected more than 3 seconds ago )
