from gpiozero import Button
from signal import pause

# GPIO 17 connected to the NO pin of your switch/zone
bumper = Button(17, pull_up=True)

def bumper_hit():
    print("BUMPER HIT DETECTED! Stopping motors...")

def bumper_cleared():
    print("Bumper released.")

bumper.when_pressed = bumper_hit
bumper.when_released = bumper_cleared

print("Bumper test running... Press the switch lever.")
pause()
