# Create a diceware password using the EFF foundation's approved word list - by Troy Caywood
# Icon image credit to https://www.flaticon.com/free-icons/passkey Passkey icons created by smalllikeart - Flaticon
# Main image credit to https://www.flaticon.com/free-icons/dice"title="dice icons">Dice icons created by Smashicons

import json
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip


index_number_list = []
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# -------------------- WORD LOOKUP -------------------- #
with open("data.json") as data_file:
    data = json.load(data_file)


def dice_roll():
    for _ in range(5):
        roll = random.randrange(1, 7)
        index_number_list.append(str(roll))


def word_lookup():
    index_number_list.clear()
    dice_roll()
    index_number = "".join(index_number_list)
    return data[index_number]


def password_assemble():
    password_list = []

    try:
        for num in range(int(words_entry.get())):
            word = word_lookup()
            if num % 2 == 0:
                password_list.append(word.capitalize())
            else:
                password_list.append(word)

        for _ in range(int(numbers_entry.get())):
            password_list.append(random.choice(numbers))

        for _ in range(int(symbols_entry.get())):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)
        password = f"{seperator_entry.get()}".join(password_list)
        pyperclip.copy(password)
        messagebox.showinfo(title="Your Generated Password", message=f"Your password is '{password}'\n"
                                                                     f"Your password has been copied to your clipboard")
    except ValueError:
        messagebox.showinfo(title="Invalid Entry", message="Only numbers are valid entries for words,"
                                                           " symbols, and numbers")


# -------------------- USER INTERFACE -------------------- #

window = tk.Tk()
window.minsize(width=200, height=200)
window.title("Tiny Dice")
window.config(padx=20, pady=5)

canvas = tk.Canvas(width=64, height=64)
logo_image = tk.PhotoImage(file="images/logo.png")
canvas.create_image(35, 32, image=logo_image)

window.iconbitmap("images/logo.ico")

canvas.grid(column=0, row=0, columnspan=2)

numbers_label = tk.Label(text="Number of numbers")
numbers_label.grid(column=0, row=2)

symbols_label = tk.Label(text="Number of symbols")
symbols_label.grid(column=0, row=3)

words_label = tk.Label(text="Number of words")
words_label.grid(column=0, row=1)

words_entry = tk.Entry(width=10)
words_entry.insert(index=0, string="0")
words_entry.grid(column=1, row=1)

numbers_entry = tk.Entry(width=10)
numbers_entry.insert(index=0, string="0")
numbers_entry.grid(column=1, row=2)

symbols_entry = tk.Entry(width=10)
symbols_entry.insert(index=0, string="0")
symbols_entry.grid(column=1, row=3)

seperator_label = tk.Label(text="Seperator")
seperator_label.grid(column=0, row=5)

seperator_entry = tk.Entry(width=10)
seperator_entry.grid(column=1, row=5)

generate_pw_button = tk.Button(text="Generate Password", command=password_assemble)
generate_pw_button.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

instructions_label = tk.Label(text="Enter the number of words, numbers, and symbols\n"
                                   " you want in your password.\n\n"
                                   " Enter a separator if you want one.\n"
                                   " Otherwise leave it blank.")
instructions_label.grid(column=0, row=6, columnspan=2)
instructions_label.config(padx=10, pady=10)

window.mainloop()
