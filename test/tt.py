from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import ttk
from tkinter import messagebox
import pyqrcode
from PIL import ImageTk, Image
import os

def generate():
    link_name = name_var.get().strip()
    link = link_var.get().strip()

    if not link_name or not link:
        messagebox.showwarning("Missing Info", "Please fill in both fields.")
        return

    file_name = link_name + ".png"
    try:
        qr = pyqrcode.create(link)
        qr.png(file_name, scale=8)

        img = Image.open(file_name)
        img = img.resize((200, 200))  # resize for UI
        img_tk = ImageTk.PhotoImage(img)

        qr_label.config(image=img_tk)
        qr_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR: {e}")

# --- Main UI ---
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

# Optional: Set icon
# root.iconbitmap('icon.ico')  # Add your icon here

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12))

# Variables
name_var = StringVar()
link_var = StringVar()

# Layout
ttk.Label(root, text="QR Code Generator", font=("Segoe UI", 18, "bold"), foreground="blue").pack(pady=(20, 10))

frame = ttk.Frame(root, padding=20)
frame.pack()

ttk.Label(frame, text="Link name:").grid(row=0, column=0, sticky="w")
ttk.Entry(frame, textvariable=name_var, width=30).grid(row=1, column=0, pady=(0, 10))

ttk.Label(frame, text="Link:").grid(row=2, column=0, sticky="w")
ttk.Entry(frame, textvariable=link_var, width=30).grid(row=3, column=0, pady=(0, 20))

ttk.Button(frame, text="Generate QR Code", command=generate).grid(row=4, column=0, pady=10)

qr_label = ttk.Label(root)
qr_label.pack(pady=10)

# --- Start UI ---
root.mainloop()
