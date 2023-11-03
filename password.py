import random
import tkinter as tk

def generate_password():
    password_length = 9  
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(password_length))
    pwd_label.config(text=password)

window = tk.Tk()

generate_btn = tk.Button(window, text="Generate Password", command=generate_password,width=50,height=10)
generate_btn.pack()

pwd_label = tk.Label(window, text="")
pwd_label.pack()

window.mainloop()