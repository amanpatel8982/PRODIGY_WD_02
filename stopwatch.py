import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")
        
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        
        self.label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=20)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side="left")
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=20)
        
    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            milliseconds = int((self.elapsed_time * 100) % 100)
            self.label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")
            self.root.after(10, self.update)
        
    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update()
        
    def pause(self):
        self.running = False
        
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
