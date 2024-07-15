import time, threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key
# from tkinter import *

# window = Tk() 
# window.title("No Hands Clicking")

delay = 0.5
buttonToClick = Button.left 
start_stop_key = KeyCode(char='g')
exit_key = KeyCode(char='p')

class ClickMouse(threading.Thread):
    def __init__(self, delay, buttonToClick):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.buttonToClick = buttonToClick
        self.running = False
        self.program_run = True
    
    def start_clicking(self):
        self.running = True 

    def stop_clicking(self): 
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False 

    def run(self):
        while self.program_run:
            while self.running: 
                mouse.click(self.buttonToClick)
                time.sleep(self.delay)
            time.sleep(4)

mouse = Controller()
thread = ClickMouse(delay, buttonToClick)
thread.start() 

def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener: 
    listener.join()

# Window UI 
# lbl = Label(window, text="Press the g key to start")
# lbl.grid(column=1, row=0, padx=(75,10))

# window.geometry('200x150')