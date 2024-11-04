import random
import string
import tkinter as tk
from tkinter import messagebox


# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4 characters.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")
        return

    use_uppercase = var_uppercase.get()
    use_lowercase = var_lowercase.get()
    use_digits = var_digits.get()
    use_special = var_special.get()

    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        messagebox.showwarning("Warning", "Select at least one character type.")
        return

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)


# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Length label and entry
tk.Label(root, text="Password Length:").pack(pady=5)
entry_length = tk.Entry(root, width=10)
entry_length.pack(pady=5)

# Character options
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase).pack(anchor='w')
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).pack(anchor='w')

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

# Display generated password
tk.Label(root, text="Generated Password:").pack(pady=5)
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

root.mainloop()
