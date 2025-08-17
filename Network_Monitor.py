import tkinter as tk
import psutil
import time
import ctypes
import platform

class RealTimeNetworkMonitor(tk.Tk):
    def __init__(self):
        super().__init__()

        # === Window Setup ===
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", "#111111")
        self.config(bg="#111111")
        self.geometry("340x260+1600+100")

        # === Font Setup ===
        self.title_font = ("Poppins", 14, "bold")
        self.label_font = ("Poppins", 11)

        # === Colors ===
        self.main_bg = "#1a1a1a"
        self.accent_fg = "#90ee90"
        self.shadow_color = "#222222"

        # === Container ===
        self.container = tk.Frame(self, bg=self.main_bg, bd=0,
                                  highlightthickness=1,
                                  highlightbackground=self.shadow_color)
        self.container.pack(expand=True, fill="both", padx=12, pady=12)

        # === Close Button ===
        self.close_btn = tk.Button(self.container, text="✕", font=("Poppins", 10, "bold"),
                                   fg="#ff5c5c", bg=self.main_bg, bd=0,
                                   activebackground=self.main_bg, activeforeground="#ff0000",
                                   command=self.destroy, cursor="hand2")
        self.close_btn.pack(anchor="ne", padx=2, pady=2)

        # === Title Label ===
        self.title_label = tk.Label(self.container, text="📶 Network Monitor", font=self.title_font,
                                    fg=self.accent_fg, bg=self.main_bg)
        self.title_label.pack(anchor="center", pady=(0, 15))

        # === Data Labels ===
        self.download_label = tk.Label(self.container, font=self.label_font, fg=self.accent_fg, bg=self.main_bg)
        self.upload_label = tk.Label(self.container, font=self.label_font, fg=self.accent_fg, bg=self.main_bg)
        self.total_label = tk.Label(self.container, font=self.label_font, fg=self.accent_fg, bg=self.main_bg)
        self.speed_dl_label = tk.Label(self.container, font=self.label_font, fg=self.accent_fg, bg=self.main_bg)
        self.speed_ul_label = tk.Label(self.container, font=self.label_font, fg=self.accent_fg, bg=self.main_bg)

        self.download_label.pack(anchor="center", pady=2)
        self.upload_label.pack(anchor="center", pady=2)
        self.total_label.pack(anchor="center", pady=2)
        self.speed_dl_label.pack(anchor="center", pady=5)
        self.speed_ul_label.pack(anchor="center", pady=2)

        # === Network Data Setup ===
        net = psutil.net_io_counters()
        self.start_received = net.bytes_recv
        self.start_sent = net.bytes_sent
        self.last_received = self.start_received
        self.last_sent = self.start_sent
        self.last_time = time.time()

        # === Begin Monitoring ===
        self.update_usage()

        # === Enable Window Dragging ===
        self.bind("<Button-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)

        # === DPI Fix for Windows ===
        if platform.system() == "Windows":
            ctypes.windll.shcore.SetProcessDpiAwareness(1)

    def update_usage(self):
        current_time = time.time()
        interval = current_time - self.last_time

        net = psutil.net_io_counters()
        current_received = net.bytes_recv
        current_sent = net.bytes_sent

        # === Real-Time Delta ===
        delta_recv = current_received - self.last_received
        delta_sent = current_sent - self.last_sent

        # === Total Since App Start ===
        total_recv = current_received - self.start_received
        total_sent = current_sent - self.start_sent
        total_all = total_recv + total_sent

        # === Speeds (Bytes/sec converted to MBps or Kbps) ===
        speed_dl = delta_recv / interval
        speed_ul = delta_sent / interval

        speed_dl_str = f"{speed_dl / 1024 / 1024:.2f} MB/s" if speed_dl > 1024 * 1024 else f"{speed_dl / 1024:.2f} KB/s"
        speed_ul_str = f"{speed_ul / 1024 / 1024:.2f} MB/s" if speed_ul > 1024 * 1024 else f"{speed_ul / 1024:.2f} KB/s"

        # === Update Labels ===
        self.download_label.config(text=f"⬇ Downloaded: {total_recv / 1024 / 1024:.2f} MB")
        self.upload_label.config(text=f"⬆ Uploaded:   {total_sent / 1024 / 1024:.2f} MB")
        self.total_label.config(text=f"🔁 Total Usage: {total_all / 1024 / 1024:.2f} MB")
        self.speed_dl_label.config(text=f"🚀 Download Speed: {speed_dl_str}")
        self.speed_ul_label.config(text=f"📤 Upload Speed:   {speed_ul_str}")

        # === Update Last Values ===
        self.last_received = current_received
        self.last_sent = current_sent
        self.last_time = current_time

        # === Next Update ===
        self.after(1000, self.update_usage)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self.x
        y = self.winfo_pointery() - self.y
        self.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    app = RealTimeNetworkMonitor()
    app.mainloop()
