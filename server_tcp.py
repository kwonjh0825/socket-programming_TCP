from socket import *

serverName = '192.168.0.10'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)


connectionSocket, addr = serverSocket.accept()

sumSocket = socket(AF_INET, SOCK_STREAM)
mulSocket = socket(AF_INET, SOCK_STREAM)

result = ''

sumSocket.connect((serverName, 9998))       # plus_minus_server Port: 9998
mulSocket.connect((serverName, 9999))       # times_div_server Port: 9999

while True:
    string = connectionSocket.recv(1024).decode()
    if string == 'q':
        break
    else:
        if '+' in string or '-' in string:              # send to plus_minus_server
            sumSocket.send(string.encode())

            result = sumSocket.recv(1024).decode()
        elif '*' in string or '/' in string:            # send to times_div_server
            mulSocket.send(string.encode())

            result = mulSocket.recv(1024).decode()
            
        connectionSocket.send(result.encode())
        
sumSocket.close()                
mulSocket.close()
connectionSocket.close()