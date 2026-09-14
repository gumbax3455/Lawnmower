from gpiozero import DistanceSensor
from time import sleep

# Define Trigger and Echo GPIO pins
sensor = DistanceSensor(echo=24, trigger=23)

print("Reading HC-SR04 Sensor... Press Ctrl+C to stop.")

try:
    while True:
        # Distance is returned in meters (multiply by 100 for cm)
        distance_cm = sensor.distance * 100
        print(f"Distance: {distance_cm:.2f} cm")
        sleep(0.5)
except KeyboardInterrupt:
    print("\nTest stopped.")
