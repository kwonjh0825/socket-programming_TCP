from socket import *

serverName = '192.168.0.10'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


while True:
    sentence = input('input (q to quit) : ')
    if sentence == "q" or sentence == "Q":
        break
    clientSocket.send(sentence.encode())

    result = clientSocket.recv(1024)
    print("result : ", result.decode())

clientSocket.close()