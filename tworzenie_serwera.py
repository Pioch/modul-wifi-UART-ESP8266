import serial
import time
#ser = serial.Serial('/dev/ttyUSB0')  # open serial port
ser=serial.Serial(port='COM4', baudrate=115200, timeout=0.04) #COM4 na uczelni

#tworzenie serwera
read_timeout = 2
cmd = ["AT+CIPMUX=1\r\n", "AT+CIPSERVER=1,80\r\n"]

for c in cmd:
    ser.write(c.encode())
    msg = ser.readlines()
    for i in msg:
        tekst = i.decode("utf-8")
        if tekst != '\r\n':
            print(tekst)

cmd = "AT+CIFSR\r\n"

ser.write(cmd.encode())
msg = ser.readlines()

tekst = msg[1].decode("utf-8")

print(tekst[13:len(tekst)])
ip = ''
for i in tekst[13:len(tekst)]:

    if i != '"':
        ip = ip + i

ip = ip.rstrip('\r\n')

f = open("ip_adres.txt", "w")
f.write(ip)
f.close()

f = open("ip_adres.txt", "r")
print(f.read())


ser.close()








