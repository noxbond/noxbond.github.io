import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files_sequentially():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files_with_dates = []

    for file in files:
        filepath = os.path.join(folder_path, file)
        modified_time = os.path.getmtime(filepath)
        files_with_dates.append((file, modified_time))

    # Sort by modified time (earliest first)
    files_sorted = sorted(files_with_dates, key=lambda x: x[1])

    for index, (original_name, _) in enumerate(files_sorted, start=1):
        original_path = os.path.join(folder_path, original_name)
        
        # Remove any existing numbering prefix
        stripped_name = original_name
        if original_name[:3].isdigit() and original_name[2] == '.':
            stripped_name = original_name[4:]

        new_name = f"{index:02d}. {stripped_name}"
        new_path = os.path.join(folder_path, new_name)

        # Skip if already named correctly
        if original_path == new_path:
            continue

        os.rename(original_path, new_path)
        status_text.insert(tk.END, f"Renamed: {original_name} -> {new_name}\n")
        status_text.see(tk.END)
        root.update()

    messagebox.showinfo("Completed", "File renaming completed.")

root = tk.Tk()
root.title("Chronological File Renamer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn = tk.Button(frame, text="Select Folder and Rename Files", command=rename_files_sequentially)
btn.pack(pady=(0, 10))

status_text = tk.Text(frame, width=80, height=20)
status_text.pack()

root.mainloop()
