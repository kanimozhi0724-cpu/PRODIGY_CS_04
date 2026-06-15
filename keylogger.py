import tkinter as tk
from datetime import datetime

LOG_FILE = "keystrokes.txt"


def log_key(event):
    key = event.keysym

    # Convert special keys into readable text
    if key == "space":
        key = "Space"
    elif key == "Return":
        key = "Enter"
    elif key == "BackSpace":
        key = "Backspace"
    elif len(key) > 1:
        key = f"[{key}]"

    # Save the key press to the file
    with open(LOG_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} : {key}\n")


# Create the main window
root = tk.Tk()
root.title("Educational Key Logger")
root.geometry("500x250")

# Instructions
label = tk.Label(
    root,
    text="Type inside the box below.\n"
         "Only keystrokes entered here will be recorded.",
    font=("Arial", 12),
    pady=10
)
label.pack()

# Text area to capture keystrokes
text_box = tk.Text(root, height=8, width=50)
text_box.pack(pady=10)

# Bind key press events to the text box
text_box.bind("<Key>", log_key)

# Start with an empty log file
with open(LOG_FILE, "w") as file:
    file.write("=== Educational Key Log Started ===\n")

root.mainloop()