import serial

ser = serial.Serial('/dev/ttyUSB0', 57600)

while True:
    data = input("Mesajınız: ")
    ser.write(data.encode())
