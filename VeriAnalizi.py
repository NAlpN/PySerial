import serial

ser = serial.Serial('/dev/ttyUSB0', 57600)

while True:
    data = ser.readline().decode().strip()
    if data:
        temperature = float(data)
        if temperature > 30:
            print("Uyarı: Sıcaklık yüksek!")
