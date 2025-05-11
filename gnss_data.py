import serial
import pynmea2
import json
from datetime import datetime

# Serial configuration
SERIAL_PORT = '/dev/ttyACM1'
BAUD_RATE = 9600

# Open USB serial port
ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line.startswith('$GNGGA') or line.startswith('$GPGGA'):
            msg = pynmea2.parse(line)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            latitude = msg.latitude
            longitude = msg.longitude
            altitude = msg.altitude

            # Print to terminal
            print(f"Timestamp: {timestamp}, Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}m")

            # Write to shared JSON file
            with open("latest_gnss.json", "w") as f:
                json.dump({
                    "timestamp": timestamp,
                    "latitude": latitude,
                    "longitude": longitude,
                    "altitude": altitude
                }, f)

    except Exception as e:
        print(f"Error: {e}")
