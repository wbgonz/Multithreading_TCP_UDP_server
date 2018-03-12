from socket import *

serverName = gethostname()
serverPort = 54320
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect() addresses server welcoming TCP socket
address = (serverName, serverPort)
clientSocket.connect(address)

# setting sentence buffer
sentence = ''
bufferSize = 1024

while True:
    # get user input until return character (press enter)
    sentence = input('Input lowercase sentence:')

    if sentence == 'stop':
        break
    # Drops sentence into the client socket so it can be sent to server
    clientSocket.sendall(sentence.encode("UTF-8"))
    modifiedSentence = clientSocket.recv(bufferSize).decode("UTF-8")

    # will receive at most 1024 bits
    print('Server replies:', modifiedSentence)

clientSocket.close()