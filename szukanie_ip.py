import serial
import time
#ser = serial.Serial('/dev/ttyUSB0')  # open serial port
ser=serial.Serial(port='COM2', baudrate=115200, timeout=1)

def adres_ip():

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

    ser.close()

    return ip
