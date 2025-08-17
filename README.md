# Real-Time Network Bandwidth Monitor

A sleek, always-on-top desktop widget built with Python and Tkinter to monitor your network bandwidth usage in real time. Track your upload and download speeds as well as the total data used since launching the app, all within a minimalistic and modern interface.

Now available as a standalone `.exe` — no need to install Python!

---

## Features

- Clean dark-themed UI with light green accents for easy readability  
- Displays total data downloaded, uploaded, and combined since app start  
- Shows real-time upload and download speeds (in MB/s or KB/s)  
- Always stays on top of other windows and can be freely dragged around the screen  
- Frameless window design with a close button for quick exit  
- Lightweight and efficient, leveraging `psutil` for accurate network statistics  
- Fully packaged as a Windows executable (`.exe`) — portable and no Python required  

---

## 🔧 Installation (Source Code)

If you'd like to run the project from source:

1. Ensure you have Python 3 installed. Download it from [python.org](https://www.python.org/) if needed.
2. Clone or download this repository to your local machine.
3. Install the required Python package:

```bash
pip install psutil
```

## Run the Executable (.exe)
If you're using the pre-built .exe version:

Download Network_Monitor.exe from the Releases section (or your provided location).

Double-click to launch the app.

The widget will appear on your screen with real-time bandwidth stats.

The executable requires no installation or Python setup.

## How It Works
Starts monitoring bandwidth usage from the moment the app is opened

Tracks:

Downloaded data (MB)

Uploaded data (MB)

Total data transferred (MB)

Live upload/download speeds

Speeds update every second

Drag anywhere to reposition the widget

Click the ✕ in the corner to close the app
## License
This project is open-source and distributed under the MIT License.

## Contact
If you have any questions, suggestions, or feedback, feel free to get in touch!