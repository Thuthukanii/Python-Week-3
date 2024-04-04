import csv
import re
import email
import tkinter as tk
from tkinter import messagebox
def register():
    with open("users.csv" ,mode = "a" ,newline= "") as f:
        writer = csv.writer(f, delimiter=",")

        def validation():

            while True:
                email = input("Please enter email: ")
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    break
                else:
                    print("Invalid email address.")

        validation()

        password = input("Please enter your password")
        password2 = input("Please re-enter your password")

        if password == password2:
            writer.writerow([email,password])
            print("Registration is successful!")
        else:
            print("Please try again")
 
def login():
    email = input("Please enter your email")
    password = input("Please enter your password")
    with open("users.csv" ,mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are logged in!")
                return True
    print("Please try again!")
    return False


import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Replace this with your actual login logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")


def signup():
    # Replace this with your actual signup logic
    messagebox.showinfo("Signup", "Signup Successful!")


# Create the main window
root = tk.Tk()
root.title("Login / Signup")

# Create and place widgets for login
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place widgets for signup
label_signup = tk.Label(root, text="New User? Sign up here:")
label_signup.grid(row=3, column=0, columnspan=2, pady=5)

signup_button = tk.Button(root, text="Signup", command=signup)
signup_button.grid(row=4, column=0, columnspan=2, pady=5)

# Start the GUI event loop
root.mainloop()

register()
login()