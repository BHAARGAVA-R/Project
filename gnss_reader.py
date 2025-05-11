import serial
import pynmea2

# Open the USB serial port (change ttyUSB0 if needed)
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore')
        if line.startswith('$GNGGA'):
            msg = pynmea2.parse(line)
            print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}, Altitude: {msg.altitude}m")
    except Exception as e:
        print(f"Error: {e}")
