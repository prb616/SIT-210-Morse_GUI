import tkinter as tk
import RPi.GPIO as GPIO
import time

# Define Morse code mappings for letters and numbers
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

# GPIO pin for the LED
LED_PIN = 17

# Function to blink the LED using Morse code
def blink_morse_code(word):
    for letter in word.upper():  # Convert input to uppercase
        if letter == ' ':
            time.sleep(3)  # Pause for 3 units between words
        elif letter in MORSE_CODE_DICT:  # Check if the character is in the Morse code dictionary
            morse_code = MORSE_CODE_DICT[letter]  # Get Morse code representation
            for symbol in morse_code:
                if symbol == '.':
                    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED (dot)
                    time.sleep(0.2)  # Dot duration
                elif symbol == '-':
                    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED (dash)
                    time.sleep(0.6)  # Dash duration
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
                time.sleep(0.2)  # Pause between symbols
            time.sleep(0.4)  # Pause between letters

# Function to handle the button click event
def on_button_click():
    user_input = entry.get()[:12]  # Get the user input (max 12 characters)
    blink_morse_code(user_input)

# Initialize the GPIO
GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering mode to BCM
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure the LED is initially off

# Create the GUI
root = tk.Tk()
root.title("Morse Code Blinker")

label = tk.Label(root, text="Enter a word (max 12 characters):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Blink Morse Code", command=on_button_click)
button.pack()

root.mainloop()  # Start the GUI main loop

# Cleanup GPIO on program exit
GPIO.cleanup()  # Reset GPIO configuration when the program exits
