import serial

ser = serial.Serial('/dev/ttyUSB0', 57600)
ser.write(b'Hello, Nvidia!')