#!/usr/bin/python3 

# Wordlist Generator (Version 0.5) - Most Accurate Tool is under Development -- Created By Aman Chauhan

# Features 3 distinct modes:
# 1. Casual Mode
# 2. Pro Mode
# 3. Beast Mode

# Choose a more challenging mode to enhance your cracking potential.

import time
import sys

def generate_pass(name, special_characters, file):
    file.write(name + "\n")
    for i in range(10000):
        file.write(name + str(i) + "\n")
    for i in range(10000):
        for char in special_characters:
            file.write(name + char + str(i) + "\n")

special_characters = ['!', '@', '#', '$', '&', '*', '_', '.', '?']


def animated_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

try:
    animated_print("\n        WORDLIST GENERATOR (--version 2.1) by Aman Chauhan", 0.05)

    print("\nFeatures 3 DISTINCT MODES:\n1. CASUAL MODE\n2. PRO MODE\n3. BEAST MODE")
    print("The HIGHER you choose, the MORE you're able to CRACK!\n")

    user_input = input("Choose the mode (1, 2, or 3): ")

    first_name = input("Enter the first name of target: ").strip()
    last_name = input("Enter the last name of target (optional): ").strip()
    output_file = input("Enter the filename to save the wordlist (no spaces allowed): ").strip()

    with open(output_file, "w") as file:

        if user_input == "1":                   # Casual Mode
            generate_pass(first_name.lower(), special_characters, file)
            generate_pass(first_name.capitalize(), special_characters, file)
            if last_name:
            # Generate wordlist for the last name
                generate_pass(last_name.lower(), special_characters, file)
                generate_pass(last_name.capitalize(), special_characters, file)

        elif user_input == "2":                 # Pro Mode
            generate_pass(first_name.lower(), special_characters, file)
            generate_pass(first_name.capitalize(), special_characters, file)
            if last_name:
                generate_pass(last_name.lower(), special_characters, file)
                generate_pass(last_name.capitalize(), special_characters, file)
            # Combine first and last name
            if last_name:
                generate_pass(first_name.lower() + last_name.lower(), special_characters, file)
                generate_pass(first_name.capitalize() + last_name.lower(), special_characters, file)
                generate_pass(first_name.capitalize() + last_name.capitalize(), special_characters, file)

        elif user_input == "3":  # Beast Mode
            generate_pass(first_name.lower(), special_characters, file)
            generate_pass(first_name.capitalize(), special_characters, file)
            generate_pass(first_name.upper(), special_characters, file)
            if last_name:
                generate_pass(last_name.lower(), special_characters, file)
                generate_pass(last_name.capitalize(), special_characters, file)
                generate_pass(last_name.upper(), special_characters, file)
            # Combine first and last name
            if last_name:
                generate_pass(first_name.lower() + last_name.lower(), special_characters, file)
                generate_pass(first_name.capitalize() + last_name.lower(), special_characters, file)
                generate_pass(first_name.capitalize() + last_name.capitalize(), special_characters, file)
                generate_pass(first_name.upper() + last_name.upper(), special_characters, file)
                generate_pass(last_name.lower() + first_name.lower(), special_characters, file)
                generate_pass(last_name.capitalize() + first_name.lower(), special_characters, file)
                generate_pass(last_name.capitalize() + first_name.capitalize(), special_characters, file)
        else:
            print("Invalid mode selected. Please enter 1, 2, or 3.")



    print(f"\nYour wordlist have been saved to '{output_file}' successfully!\n Thanks for using :)")
    
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")

