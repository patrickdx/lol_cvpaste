import sys 
import time
import pynput
from pynput.keyboard import Key, Controller
import os

# usage: cvpaste.py spam.txt




# prints msg in-game chat
def printer(message : str):
    for line in message:
        if (line == '\n'): continue         # cant write newline anyways
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.02)
        keyboard.type(line)     # \n is interepted as 'enter'
        time.sleep(0.02)
        

# sets keybinds to msgs
def binds(keys, msgs : list[str]):
    if (len(keys) != len(msgs)): raise Exception("Number of keys does not correspond to number of messages")
    for key, msg in zip(keys, msgs):
        bindings[key] = msg



def on_press(key):
    print(key)
    if (key in bindings): printer(bindings[key])
    if (key == Key.esc): exit()
    

def on_release(key):
    pass



keyboard = Controller()
msg = []
time.sleep(1)
all_chat = False


try: f = sys.argv[1]
except IndexError: 
    print("text file not specified")
    exit()

if (not os.path.isfile(f)):
    raise FileNotFoundError("passed text file does not exist :(")




# read in text from file once 
with open(f, 'r', encoding='utf8') as file:   # auto closes when done reading
    msg = [line for line in file]
    msg[-1] +=  '\n'         # this is for closing chatbox
    print(msg)

bindings = {Key.page_down : msg} 


# blocking thread; Collect events until released
with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    print("\nlistening...")
    listener.join()


# # non-blocking thread; Collect events until released, calls on_press and on_release upon key action
# listener = pynput.keyboard.Listener( on_press=on_press, on_release=on_release) 
# listener.start()
# print('\nlistening...')

