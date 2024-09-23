import socket 

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('"0linux ip"', "0port of linux" ))
print('[+] Listening of the Incoming Connections')
sock.listen(5)
target, ip= sock.accept()
print('[+] Target Connected From: '+ str(ip))
target_communication()