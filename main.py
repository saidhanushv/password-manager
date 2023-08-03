import json
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Unacceptable Details", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        except json.decoder.JSONDecodeError:
            data = {}

        # dictionary to store emails and passwords in json format
        data.update({
            website: {
                "email": email,
                "password": password,
            }
        })
        with open("data.json", "w") as data_file:
            # Saving/Writing the data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    is_found = 0
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No File Found", message="No Data File Found")
        data = {}
    except json.JSONDecodeError:
        messagebox.showinfo(title="No Data Found", message="data.json does not contain data")
        data = {}
    else:
        for key, value in data.items():
            if key == website_entry.get():
                messagebox.showinfo(title=website_entry.get(),
                                    message=f"Username: {key}\nPassword: {value['password']}")
                is_found = 1
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        if is_found == 0:
            messagebox.showinfo(title="Error", message=f"No Details For {website_entry.get()} Found")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

main_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=main_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

website_search_btn = Button(text="Search", command=find_password)
website_search_btn.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "yourmail@gmail.com")  # END represents the last character of the entry ie.., the cursor will
# be at the end of the entry for you to edit. Or you can use 0 which represents the beginning of the entry

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21, show="*")
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
