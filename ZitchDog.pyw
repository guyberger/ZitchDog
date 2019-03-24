
# save this file as a .pyw to make the logger run in the background. exit via task manager.

from pynput.keyboard import Key, Listener
import logging
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(200, 50)

        self.myLabel = tk.Label(None, text = "Marshall says: Zitchdog!")
        self.myLabel.pack()

        self.attributes("-topmost", True)
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#make a log file

log_dir = ""    #default same location
tracker = ""    #tracker is the current string typed. looking for target.
target = ["dog", "Dog", "dOg", "doG", "DOg", "DoG", "DOG", "dOG"]   #looking for a dog...

logging.basicConfig(filename=(log_dir + "log.txt"), level = logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    #if key == Key.esc:
        #return false
    key = str(key)[1]    #strip from ' '
    global tracker
    global target
    tracker = tracker + str(key)
    if tracker in target:
        logging.info(tracker) #this logs the key typed in the file
        app = SampleApp()
        app.mainloop()
        tracker = ""
    if len(tracker) > 3: #for dog...
        tracker = ""

with Listener(on_press = on_press) as listener:
    listener.join()
