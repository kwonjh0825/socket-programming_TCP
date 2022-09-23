from socket import *

serverName = '192.168.0.10'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)


connectionSocket, addr = serverSocket.accept()



calSocket = socket(AF_INET, SOCK_STREAM)

result = ''

while True:
    string = connectionSocket.recv(1024).decode()
    if string == 'q':
        break
    else:
        if '+' in string or '-' in string:                        # send to plus_minus_server
            calSocket.connect((serverName, 9998))       # plus_minus_server Port: 9998
            calSocket.send(string.encode())

            result = calSocket.recv(1024).decode()
            calSocket.close()                
                
        elif '*' in string or '/' in string:
            calSocket.connect((serverName, 9999))       # times_div_server Port: 9999
            calSocket.send(string.encode())

            result = calSocket.recv(1024).decode()
            calSocket.close()

        connectionSocket.send(result.encode())

connectionSocket.close()