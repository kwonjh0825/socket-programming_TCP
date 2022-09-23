from socket import *

serverName = '192.168.0.10'
serverPort = 9998
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

result = 0
r = 0
oper = ''

while True:
    string = connectionSocket.recv(1024).decode()

    for i in string:
        if i == '+' or i == '-':
            oper = i
            idx = string.index(i)

    if oper == '+':
            r = int(string[0:idx]) + int(string[idx+1:])
    elif oper == '-':
            r = int(string[0:idx]) - int(string[idx+1:])

    print(f"{string} = {r}")
    
    result = str(r)
    
    connectionSocket.send(result.encode())