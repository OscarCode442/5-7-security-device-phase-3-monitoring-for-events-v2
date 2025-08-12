import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import time  # Optional: for adding a small delay in the loop

GPIO.setwarnings(False)  # Ignore warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 7 as input with pull-down resistor

button_pressed = False  # Semaphore variable to track button state

while True:  # Infinite loop
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone has pressed the alert button!")
        button_pressed = True  # Set flag to True to avoid multiple prints

    elif GPIO.input(7) == GPIO.LOW and button_pressed:
        button_pressed = False  # Reset flag when button is released

    # Optional: avoid CPU overuse
    time.sleep(0.05)  # 50ms delay
