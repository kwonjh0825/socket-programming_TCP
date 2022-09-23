from socket import *

serverName = '192.168.0.10'
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

result = 0
r = 0
oper = ''

while True:   
    string = connectionSocket.recv(1024).decode()
    print(string)
    for i in string:
        if i == '*' or i == '/':
            oper = i
            idx = string.index(i)
    print(string[0:idx, oper, string[idx+1:]])
    if oper == '*':
        r = int(string[0:idx]) * int(string[idx+1:])
    elif oper == '/':
        r = int(string[0:idx]) / int(string[idx+1:])

    connectionSocket.send(result.encode())

connectionSocket.close()

