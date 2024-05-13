import serial
import requests

ser = serial.Serial('/dev/ttyUSB0', 57600)

while True:
    data = ser.readline().decode().strip()
    if data:
        payload = {'data': data}
        response = requests.post('localhost', data=payload)
        print("Response:", response.text)
