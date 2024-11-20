import socket
import time
import RPi.GPIO as GPIO
HOST = '192.168.100.8'
PORT = 5566
GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
#Relé1
GPIO.setup(18, GPIO.OUT)
#Relé2
GPIO.setup(24, GPIO.OUT)
# criando o socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
# teste de conexão com o servidor
 c.connect((HOST, PORT))
except Exception as erro:
 print(str(erro))
print('Conectado com: ', HOST)
#Recebe informações disponíveis
msg = "MENU:"
c.send(msg.encode())
while True:
 # testa msg recebida
 try:
    info = c.recv(1024).decode()
 except Exception as err:
 break
 # Decodifica mensagem em UTF-8:
 if (info == '1'):
 GPIO.output(18, GPIO.HIGH)
 print("Relé1 ON")
 time.sleep(1)
 # GPIO.output(24, GPIO.HIGH)
 # print("Relé2 ON")
 # time.sleep(1)

 GPIO.output(18, GPIO.LOW)
 print("Relé1 OFF")
 time.sleep(1)
 # GPIO.output(24, GPIO.LOW)
 # print("Relé2 OFF")
 # time.sleep(1)
 if (info == '0'):
 print('’Encerrando ...'’)
 
 break
GPIO.cleanup()