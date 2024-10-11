# The Mighty Calculator
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

# Calculator function demonstrations
result = add_numbers(5, 3)
print("The sum is:", result)

result = subtract_numbers(10, 4)
print("The difference is:", result)

result = multiply_numbers(6, 2)
print("The product is:", result)

result = divide_numbers(15, 0)
print("The quotient is:", result)


# The Quest for Fibonacci
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number to find the Fibonacci sequence: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")


# The Cryptic Decoder
def decode_message(encoded_message):
    cipher_dict = {
        'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 
        'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v', 
        'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a', 
        'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f', 
        'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 
        'z': 'l'
    }
    decoded_message = ''.join(cipher_dict.get(char, char) for char in encoded_message)
    return decoded_message

encoded = input("Enter a message to decode: ").lower()
print("Decoded message:", decode_message(encoded))


# The Magical Validator
import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return "Valid email address."
    else:
        return "Invalid email address."

email = input("Enter an email address to validate: ")
print(validate_email(email))
