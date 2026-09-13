import sys
from time import sleep
from gpiozero import LED

# Assign GPIO 17 (no physical hardware required)
test_pin = LED(17)

print("Testing gpiozero installation...")

# Set pin to HIGH (3.3V)
test_pin.on()
print(f"Pin 17 ON  -> State: {test_pin.is_lit}")

sleep(1)

# Set pin to LOW (0V)
test_pin.off()
print(f"Pin 17 OFF -> State: {test_pin.is_lit}")

# Cleanly release the pin
test_pin.close()

print("gpiozero execution test complete!")