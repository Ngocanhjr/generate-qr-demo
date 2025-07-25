import customtkinter as ctk
import pyqrcode
from PIL import Image, ImageTk

ctk.set_appearance_mode("Dark")  # Set initial appearance mode to Dark
ctk.set_default_color_theme("blue")  # Set default color theme to blue

class QRApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")  # Set window title
        self.geometry("400x700")  # Set fixed window size
        self.resizable(False, False)  # Disable window resizing

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 700) // 2
        self.geometry(f"400x700+{x}+{y}")

        self.link_name = ctk.StringVar()  # Variable to store name input
        self.link = ctk.StringVar()  # Variable to store link input
        self.create_widgets()  # Initialize widgets

    def create_widgets(self):
        # Create main frame with transparent background and padding
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=25, pady=25)

        # Create title label with centered and bold text
        self.title_label = ctk.CTkLabel(self.main_frame, text="QR CODE GENERATOR",
                                        font=("Segoe UI", 28, "bold"), text_color="white")
        self.title_label.pack(pady=(0, 40))

        # Create theme toggle button and position it at bottom right
        self.theme_button = ctk.CTkButton(self.main_frame, text="🌙 NIGHT MODE",
                                          width=120, height=24, corner_radius=16,
                                          fg_color="#000000", hover_color="#1a1a1a",
                                          text_color="white", font=("Segoe UI", 9, "bold"),
                                          command=self.toggle_theme)
        self.theme_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-20)

        self.is_dark_mode = True  # Track current theme mode (starts as Dark)

        # Create label and entry for name input
        self.name_label = ctk.CTkLabel(self.main_frame, text="Name",
                                       font=("Segoe UI", 14, "bold"), anchor="w")
        self.name_label.pack(fill="x", pady=(0, 8))

        self.entry_name = ctk.CTkEntry(self.main_frame, textvariable=self.link_name,
                                       height=50, corner_radius=12, font=("Segoe UI", 12),
                                       placeholder_text="Enter name...")
        self.entry_name.pack(fill="x", pady=(0, 25))

        # Create label and entry for link input
        self.link_label = ctk.CTkLabel(self.main_frame, text="Link",
                                       font=("Segoe UI", 14, "bold"), anchor="w")
        self.link_label.pack(fill="x", pady=(0, 8))

        self.entry_link = ctk.CTkEntry(self.main_frame, textvariable=self.link,
                                       height=50, corner_radius=12, font=("Segoe UI", 12),
                                       placeholder_text="Enter URL...")
        self.entry_link.pack(fill="x", pady=(0, 30))

        # Create generate button with custom styling
        self.generate_btn = ctk.CTkButton(self.main_frame, text="Generate QR Code",
                                          width=50, height=40, corner_radius=12,
                                          font=("Segoe UI", 14, "bold"), fg_color="#7C3AED",
                                          hover_color="#6D28D9", command=self.generate_qr)
        self.generate_btn.pack(fill="x", pady=(0, 30))

        # Create frame for QR code display
        self.qr_frame = ctk.CTkFrame(self.main_frame, height=220, corner_radius=12)
        self.qr_frame.pack(fill="x", pady=(0, 20))
        self.qr_frame.pack_propagate(False)

        self.qr_label = ctk.CTkLabel(self.qr_frame, text="QR Code will appear here",
                                     font=("Segoe UI", 12))
        self.qr_label.pack(expand=True)

    def toggle_theme(self):
        # Switch theme based on current mode
        if self.is_dark_mode:
            ctk.set_appearance_mode("Light")
            self.theme_button.configure(text="☀️ DAY MODE", fg_color="#f5f5f5",
                                        hover_color="#e0e0e0", text_color="#2d2d2d")
            self.title_label.configure(text_color="#7C3AED")
            self.is_dark_mode = False
        else:
            ctk.set_appearance_mode("Dark")
            self.theme_button.configure(text="🌙 NIGHT MODE", fg_color="#1a1a1a",
                                        hover_color="#333333", text_color="#ffffff")
            self.title_label.configure(text_color="white")
            self.is_dark_mode = True

    def generate_qr(self):
        # Get input values and remove whitespace
        name = self.link_name.get().strip()
        link = self.link.get().strip()

        # Check if both fields are filled
        if not name or not link:
            error_dialog = ctk.CTkToplevel(self)
            error_dialog.title("Missing Information")
            error_dialog.geometry("300x150")
            error_dialog.transient(self)
            error_dialog.grab_set()
            error_dialog.geometry(f"+{self.winfo_x() + 50}+{self.winfo_y() + 100}")

            ctk.CTkLabel(error_dialog, text="Please fill in both fields.",
                         font=("Segoe UI", 12)).pack(pady=20)
            ctk.CTkButton(error_dialog, text="OK", command=error_dialog.destroy,
                          fg_color="#7C3AED", hover_color="#6D28D9").pack(pady=10)
            return

        file_name = name + ".png"
        try:
            # Generate QR code and save as PNG
            qr = pyqrcode.create(link)
            qr.png(file_name, scale=8)
            # Load and display the QR code image
            image = Image.open(file_name).resize((180, 180))
            img_tk = ImageTk.PhotoImage(image)
            self.qr_label.configure(image=img_tk, text="")
            self.qr_label.image = img_tk
        except Exception as e:
            # Handle errors during QR code generation
            error_dialog = ctk.CTkToplevel(self)
            error_dialog.title("Error")
            error_dialog.geometry("350x150")
            error_dialog.transient(self)
            error_dialog.grab_set()
            error_dialog.geometry(f"+{self.winfo_x() + 25}+{self.winfo_y() + 100}")

            ctk.CTkLabel(error_dialog, text=f"Failed to generate QR: {str(e)}",
                         font=("Segoe UI", 12), wraplength=300).pack(pady=20)
            ctk.CTkButton(error_dialog, text="OK", command=error_dialog.destroy,
                          fg_color="#7C3AED", hover_color="#6D28D9").pack(pady=10)

if __name__ == "__main__":
    app = QRApp()
    app.mainloop()  # Start the application main loop
