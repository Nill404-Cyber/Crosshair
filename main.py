#WRITTEN BY NILL-XD
import tkinter as tk

class Crosshair:
    def __init__(self, master):
        self.master = master
        self.master.title("Crosshair")
        self.master.attributes("-transparentcolor", "white")  
        self.master.attributes("-topmost", True)  
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white", highlightthickness=0)  
        self.canvas.pack()
        self.draw_crosshair()
        self.master.bind("<ButtonPress-1>", self.start_move)
        self.master.bind("<ButtonRelease-1>", self.stop_move)
        self.master.bind("<B1-Motion>", self.do_move)
        self.master.bind("<F3>", self.lock_position)
        self.locked = False
    def draw_crosshair(self):
        self.canvas.create_oval(190, 190, 200, 200, fill='GREEN')  
    def start_move(self, event):
        if not self.locked:
            self.x = event.x
            self.y = event.y
    def stop_move(self, event):
        pass
    def do_move(self, event):
        if not self.locked:
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.master.winfo_x() + deltax
            y = self.master.winfo_y() + deltay
            self.master.geometry(f"+{x}+{y}")
    def lock_position(self, event):
        self.locked = not self.locked
        if self.locked:
            print("Position locked")
        else:
            print("Position unlocked")

root = tk.Tk()
root.configure(bg="white")  
root.overrideredirect(True)  
my_crosshair = Crosshair(root)
root.mainloop()
