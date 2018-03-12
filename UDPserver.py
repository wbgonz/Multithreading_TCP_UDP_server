from socket import *
import threading




SERVER_PORT = 12005
host = gethostname()
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((host, SERVER_PORT))

class myThread(threading.Thread):

    def __init__(self, s, address, serverSocket):
        threading.Thread.__init__(self)
        self._address = address
        self._serverSocket = serverSocket
        self._sentence = s
        # print("Thread " + str(threading.current_thread()) + " created for: " + str(self._address))

    def run(self):
        print(" Starting UDP connection: "+ str(self._address))
        
        if self._sentence == 'stop':
            print("Ending UDP connection: "+ str(self._address))

        print(self._sentence)
        capitalizedSentence = self._sentence.upper().encode('UTF-8')
        self._serverSocket.sendto(capitalizedSentence, self._address)
        # address destination is attached to the message - automatically by OS


sentence = ''
while True:
    (s, address) = serverSocket.recvfrom(2048)
    sentence = s.decode('UTF-8')
    newThread = myThread(sentence, address, serverSocket)
    newThread.start()
