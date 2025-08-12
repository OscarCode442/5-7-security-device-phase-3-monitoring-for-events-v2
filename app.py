import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)  # Ignore warnings (e.g., if GPIO was used previously)
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering (not BCM/GPIO numbers)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 7 as input with pull-down resistor

while True:  # Infinite loop to keep checking the pin
    if GPIO.input(7) == GPIO.HIGH:  # Check if the button is pressed (pin goes high)
        print("Someone has pressed the alert button!")  # Print message to console
