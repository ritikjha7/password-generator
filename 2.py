import random
import string
import tkinter as tk

# Define the GUI
class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Define the length label and entry
        self.length_label = tk.Label(master, text="Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)

        # Define the password label and text field
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_text = tk.Text(master, height=1, width=20)
        self.password_text.grid(row=1, column=1, padx=5, pady=5)

        # Define the generate button
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    def generate_password(self):
        # Get the desired length from the entry field
        length = int(self.length_entry.get())

        # Define the character sets for the password
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        digits = string.digits
        special_characters = string.punctuation

        # Combine the character sets
        all_characters = uppercase_letters + lowercase_letters + digits + special_characters

        # Generate the password
        password = ''.join(random.choice(all_characters) for i in range(length))

        # Display the password in the text field
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

# Create the main window and start the GUI
root = tk.Tk()
gui = PasswordGeneratorGUI(root)
root.mainloop()
