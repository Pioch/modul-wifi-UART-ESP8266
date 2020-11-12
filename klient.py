import socket
import sys
import time
# import numpy as np
import BSP
# Create a TCP/IP socket
f = open("ip_adres.txt", "r")
ip = f.read()
f.close()

f = open("t.txt", "r")
dlugosc = len(f.readlines())
f.close()

# J = np.array([[0.233, -0.233], [0.0103, 0.0103]])
w_max = 9

print(dlugosc)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_STREAM TCP # spcket.SOCK_DGRAM UDP

# Connect the socket to the port where the server is listening
server_address = ('%s' % ip, 80)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)
print('CONNECT')

f = open("u1.txt", "r")
u1_list = f.readlines()
f.close()

f = open("u2.txt", "r")
u2_list = f.readlines()
f.close()

theta = []
x = []
y = []
dzialanie = True
liczba = 0

while liczba < dlugosc:

    otrzymana_wiadomosc2 = sock.recv(16)
    otrzymana_wiadomosc2 = otrzymana_wiadomosc2.decode()

    u1 = u1_list[liczba]
    u1 = float(u1)

    u2 = u2_list[liczba]
    u2 = float(u2)

    u_ds = [u1, u2]

    liczba = liczba + 1
    # message = input('podaj wiadomosc do serwera: ').encode()
    message = ('%f, %f' % (u_ds[0], u_ds[1])).encode()
    print('sending "%s"' % message.decode())
    sock.sendall(message)

    if otrzymana_wiadomosc2[0] == '-' and otrzymana_wiadomosc2[8] == '-':
        print('x: %s' % otrzymana_wiadomosc2[0:7])
        print('y: %s' % otrzymana_wiadomosc2[8:15])
        x.append(float(otrzymana_wiadomosc2[0:7]))
        y.append(float(otrzymana_wiadomosc2[8:15]))

    if otrzymana_wiadomosc2[0] == '-' and otrzymana_wiadomosc2[8] != '-':
        print('x: %s' % otrzymana_wiadomosc2[0:7])
        print('y: %s' % otrzymana_wiadomosc2[8:14])
        x.append(float(otrzymana_wiadomosc2[0:7]))
        y.append(float(otrzymana_wiadomosc2[8:14]))

    if otrzymana_wiadomosc2[0] != '-' and otrzymana_wiadomosc2[7] == '-':
        print('x: %s' % otrzymana_wiadomosc2[0:6])
        print('y: %s' % otrzymana_wiadomosc2[7:14])
        x.append(float(otrzymana_wiadomosc2[0:6]))
        y.append(float(otrzymana_wiadomosc2[7:14]))

    if otrzymana_wiadomosc2[0] != '-' and otrzymana_wiadomosc2[7] != '-':
        print('x: %s' % otrzymana_wiadomosc2[0:6])
        print('y: %s' % otrzymana_wiadomosc2[7:13])
        x.append(float(otrzymana_wiadomosc2[0:6]))
        y.append(float(otrzymana_wiadomosc2[7:13]))

    czas = time.perf_counter()

    if czas > 1:
        break



    print(liczba)

sock.close()

czas2 = time.perf_counter()

print(czas2)