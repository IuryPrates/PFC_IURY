import socket
HOST = '192.168.100.8'
PORT = 5566
# cria a conexão socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# associa a porta
s.bind((HOST, PORT))
# servidor entra na escuta por conexões
s.listen()
print('Esperando conexoes.. \n')
# aceita alguma conexão
s_cliente, address = s.accept()
print ('’Conectado em: '’, address)
msg = s_cliente.recv(1024)
print(msg.decode('utf-8'))
while True:

 opt = input("Acionar (1)\nSair (0)\n")
 s_cliente.send(opt.encode('utf-8')) #Envia opção escolhida
 if(opt == '0'):
 print(‘’Encerrando ..’’)
 break