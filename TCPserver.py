from socket import *
import threading
import time

exitFlag = 0

class myThread(threading.Thread):

    def __init__(self, ip, port, clientSocket):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._clientSocket = clientSocket
        print("Thread created for: " + str(self._ip) +" on Port: " + str(self._port))

    def run(self):
        print("TCP connection: "+ str(self._ip) + ":"+ str(self._port))
        sentence = ''
        bufferSize = 1024
        while sentence != 'stop':
            sentence = self._clientSocket.recv(bufferSize).decode("UTF-8")
            print(sentence)
            capitalizedSentence = sentence.upper()
            self._clientSocket.send(capitalizedSentence.encode("UTF-8"))
        self._clientSocket.close() 


SERVER_PORT = 54320
TCP_CONNECTIONS = 5

serverSocket = socket(AF_INET, SOCK_STREAM)
host = gethostname()
serverSocket.bind((host, SERVER_PORT))
serverSocket.listen(TCP_CONNECTIONS)

while True:
    (clientSocket, (clientIP, port)) = serverSocket.accept()
    newThread = myThread(clientIP, port, clientSocket)
    newThread.start()