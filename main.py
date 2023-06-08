from tkinter import *  #type: ignore
from tkinter import messagebox
import json
import string
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    #random 8 letters
    alpbabets = ''.join(random.choices(string.ascii_letters, k=8))
    #random 4 symbols
    symbol = ''.join(random.choices(string.punctuation, k= 4))
    #random 2 numbers
    number = ''.join(random.choices(string.digits, k=2))
    password = alpbabets+symbol+number
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_csv():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="OOPS", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:
                with open("D:\\coding\\python_in_hole\\python code\\password gui\\password_data.json", mode='r') as file:
                    #reading old data
                    data = json.load(file)
            except FileNotFoundError:
                #updating new data
                with open("D:\\coding\\python_in_hole\\python code\\password gui\\password_data.json", mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("D:\\coding\\python_in_hole\\python code\\password gui\\password_data.json", mode='w') as file:
                        # saving new data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    with open("D:\\coding\\python_in_hole\\python code\\password gui\\password_data.json") as file:
        data = json.load(file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"E-Mail:{email} \n password:{password}")
        else:
            messagebox.showerror(title="Error", message="Sorry Website is not in data")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="D:\\coding\\python_in_hole\\python code\\password gui\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "believeitsreal@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=1)


# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_to_csv)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="search", width=10, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()