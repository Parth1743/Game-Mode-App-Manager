# 🔧 App Manager – One-Click Desktop Control

**App Manager** is a lightweight Python GUI tool that offers seamless, one-click control over popular desktop enhancement apps like:

- 🎨 Wallpaper Engine  
- 📟 Rainmeter  
- 🌫️ TranslucentTB

Whether you're prepping your system for gaming, troubleshooting performance, or just need a clean slate fast — **App Manager saves time and clicks.**

---

## ✨ Features

- ✅ Kill multiple apps instantly with one click
- 🚀 Start all apps back up again just as fast
- 🎛️ Clean and minimal user interface (built with Tkinter)
- 🖱️ Usable as a `.py` script or `.exe` for double-click convenience
- 💡 Ideal for gamers, streamers, minimalists, and productivity enthusiasts

---

## 🖥️ Preview
![image](https://github.com/user-attachments/assets/6aa669d0-107c-45fe-86ff-80ae6a3ed8d0)

> _Simple UI with “Start Game Mode” and “End Game Mode” buttons_

---

## 📦 How to Use

### Run the Python Script

1. Make sure Python 3.x is installed
2. Clone this repo:
   git clone https://github.com/your-username/app-manager.git
   cd app-manager

3. Run the script:

   ```bash
   python app_manager.py
   ```

> 🛠️ Update the paths inside `app_manager.py` to match where the apps are installed on your system.

---

### Optional: Create a `.exe`

To turn it into a double-clickable app (no terminal):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole app_manager.py
```

The `.exe` will be inside the `dist/` folder. You can then:

* Move it anywhere
* Create a desktop shortcut
* (Optional) Add a custom icon

---

## 🧾 Requirements

* Python 3.x
* Tkinter (included with Python)
* PyInstaller (only for .exe conversion)

---

## 🙌 Credits

Developed by [Parth Garg](https://github.com/Parth1743)
Inspired by a desire for **Effortless desktop customization control.**

---
