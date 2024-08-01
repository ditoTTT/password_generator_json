from tkinter import *
from tkinter import messagebox
import random
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_choices = random.choices(letters, k=random.randint(8, 10))
    symbol_choices = random.choices(symbols, k=random.randint(2, 4))
    number_choices = random.choices(numbers, k=random.randint(2, 4))
    password_list = letter_choices + symbol_choices + number_choices
    password = ''.join(password_list)
    password_entry.insert(0, password)

def savefunc():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showerror(title='Error', message='Make Sure there is no empy field')     
    else:
        try:
            with open('day29/data.json') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('day29/data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('day29/data.json', 'w') as file:
                json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search_func():
    website = website_entry.get()

    try:
        with open('day29/data.json') as file:
            data = json.load(file)
            websites = []
            for key, values in data.items():
                websites.append(key)
                if key == website:
                    messagebox.showinfo(title=None, message=f"Password: {values['password']}\nEmail: {values['email']}")
            if website not in websites:
                    messagebox.showerror(title=None, message='No details for the website exists')
    except FileNotFoundError:
        messagebox.showerror(title=None, message='No Data File Found')

window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='day29/logo.png')
canvas.create_image(100,100, image = logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_username_label = Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, 'walbol@iml.com')
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

search_button = Button(text='Search', width=8, command=search_func)
search_button.grid(row=1, column=2)

generate_button = Button(text='Generate',command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=38, command=savefunc)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()