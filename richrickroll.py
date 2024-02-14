import string
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from colorama import Fore, Style

class PasswordGenerator:
    @staticmethod
    def generate(length=8, include_lowercase=True, include_uppercase=True, include_digits=True, include_special=True):
        characters = ''
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if len(characters) == 0:
            raise ValueError("At least one character type must be included.")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

class PasswordTester:
    @staticmethod
    def test(password):
        characters_sum = sum([1 for char in password if char.isalnum()])
        combinations = characters_sum ** len(password)
        time_to_crack_seconds = combinations / 1000000000

        if time_to_crack_seconds < 86400:
            category = "Weak password"
        elif 86400 <= time_to_crack_seconds < 604800:
            category = "Medium password"
        else:
            category = "Strong password"

        return time_to_crack_seconds, category

def generate_password():
    length = int(length_entry.get())
    include_lowercase = lowercase_var.get() == 1
    include_uppercase = uppercase_var.get() == 1
    include_digits = digits_var.get() == 1
    include_special = special_var.get() == 1
    generated_password = PasswordGenerator.generate(length, include_lowercase, include_uppercase, include_digits, include_special)
    generated_password_var.set(generated_password)

def test_password():
    test_password = test_password_entry.get()
    time_to_crack_seconds, category = PasswordTester.test(test_password)
    messagebox.showinfo("Password Test Result", f"Time to crack: {time_to_crack_seconds} seconds\nPassword category: {category}")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

# Password Generator Frame
generator_frame = ttk.LabelFrame(root, text="Password Generator")
generator_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

length_label = ttk.Label(generator_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_entry = ttk.Entry(generator_frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

lowercase_var = tk.IntVar()
lowercase_check = ttk.Checkbutton(generator_frame, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=1, columnspan=2, padx=5, pady=5, sticky="w")
lowercase_var.set(1)

uppercase_var = tk.IntVar()
uppercase_check = ttk.Checkbutton(generator_frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=2, columnspan=2, padx=5, pady=5, sticky="w")
uppercase_var.set(1)

digits_var = tk.IntVar()
digits_check = ttk.Checkbutton(generator_frame, text="Include Digits", variable=digits_var)
digits_check.grid(row=3, columnspan=2, padx=5, pady=5, sticky="w")
digits_var.set(1)

special_var = tk.IntVar()
special_check = ttk.Checkbutton(generator_frame, text="Include Special Characters", variable=special_var)
special_check.grid(row=4, columnspan=2, padx=5, pady=5, sticky="w")
special_var.set(1)

generate_button = ttk.Button(generator_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2, padx=5, pady=5)

generated_password_var = tk.StringVar()
generated_password_label = ttk.Label(generator_frame, text="Generated Password:")
generated_password_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
generated_password_display = ttk.Label(generator_frame, textvariable=generated_password_var, wraplength=300)
generated_password_display.grid(row=6, column=1, padx=5, pady=5, sticky="w")

# Password Tester Frame
tester_frame = ttk.LabelFrame(root, text="Password Tester")
tester_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

test_password_label = ttk.Label(tester_frame, text="Test Password:")
test_password_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
test_password_entry = ttk.Entry(tester_frame)
test_password_entry.grid(row=0, column=1, padx=5, pady=5)

test_button = ttk.Button(tester_frame, text="Test Password", command=test_password)
test_button.grid(row=1, columnspan=2, padx=5, pady=5)

root.mainloop()
