import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Paths to your apps (update these to match your system!)
apps_to_start = {
    "Wallpaper Engine": r"C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\wallpaper32.exe",
    "Rainmeter": r"C:\Program Files\Rainmeter\Rainmeter.exe",
    "TranslucentTB": r"C:\Program Files\WindowsApps\28017CharlesMilette.TranslucentTB_2025.1.0.0_x64__v826wp6bftszj\TranslucentTB.exe"
}

# Process names to kill
apps_to_kill = [
    "wallpaper32.exe",
    "Rainmeter.exe",
    "TranslucentTB.exe"
]

# Functions
def kill_apps():
    for app in apps_to_kill:
        os.system(f"taskkill /f /im {app}")
    messagebox.showinfo("Task Status", "All apps have been stopped.")

def start_apps():
    for name, path in apps_to_start.items():
        if os.path.exists(path):
            subprocess.Popen(path)
        else:
            messagebox.showwarning("Missing File", f"{name} path not found:\n{path}")
    messagebox.showinfo("Task Status", "All apps have been started.")

# GUI setup
root = tk.Tk()
root.title("Game Mode")
root.geometry("300x150")
root.resizable(False, False)

title_label = tk.Label(root, text="Wallpaper & Tools Manager", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

btn_kill = tk.Button(root, text="Start Game Mode", command=kill_apps, bg="red", fg="white", width=20)
btn_kill.pack(pady=5)

btn_start = tk.Button(root, text="End Game Mode", command=start_apps, bg="green", fg="white", width=20)
btn_start.pack(pady=5)

root.mainloop()
