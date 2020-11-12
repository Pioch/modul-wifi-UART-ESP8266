import time
import serial

ser=serial.Serial(port='COM4', baudrate=115200, timeout=0.05, write_timeout=0.04) #timeout=0.04, write_timeout=0.03

f = open("t.txt", "r")
dlugosc = len(f.readlines())
f.close()

f = open("theta.txt", "r")
theta_list = f.readlines()
f.close()

f = open("x.txt", "r")
x_list= f.readlines()
f.close()

f = open("y.txt", "r")
y_list = f.readlines()
f.close()

liczba = 0
while liczba < dlugosc:

    msg = ser.readlines()
    if liczba == 0:
        while len(msg) == 0:
            msg = ser.readlines()

    for i in msg:

        tekst = i.decode("utf-8")

        if '+IPD' in tekst:
            print('Otrzymana wiadomosc: ')
            print(tekst[10:len(tekst)])

        if tekst != '\r\n' and '+IPD' not in tekst:
            print(tekst)
    msg.clear()

    # dzialajace

    x = x_list[liczba]
    x = round(float(x), 5)

    y = y_list[liczba]
    y = round(float(y), 5)

    message = ('%.5f%.5f' % (x, y)).encode()
    len1 = len(message)
    cmd = 'AT+CIPSEND=0,%d\r\n' % len1
    print('sending x, y: %s' % message.decode())
    ser.write(cmd.encode())
    potwierdzenie = ser.readline()

    while len(potwierdzenie) == 0:
        potwierdzenie = ser.readline()

    ser.write(message)
    # potwierdzenie.clear()
    print(liczba)

    liczba = liczba + 1

czas = time.perf_counter()
# b'AT\r\n', b'\r\n', b'OK\r\n'
message = 'koniec'.encode()
len1 = len(message)
cmd = 'AT+CIPSEND=0,%d\r\n' % len1
ser.write(cmd.encode())
ser.close()



print(czas)







