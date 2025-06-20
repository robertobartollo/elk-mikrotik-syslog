import socket
import time

# Configurações
UDP_IP = "192.168.1.43"  # IP do seu servidor
UDP_PORT = 514

# Mensagem de teste no formato do Mikrotik
test_message = "<134>input accept in:ether1 out:ether2, proto tcp, 192.168.1.1:12345->8.8.8.8:80, len 60"

# Criar socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar mensagem
print(f"Enviando mensagem de teste para {UDP_IP}:{UDP_PORT}")
sock.sendto(test_message.encode(), (UDP_IP, UDP_PORT))
print("Mensagem enviada!")

# Fechar socket
sock.close() 