import sys 
import time
import pynput
from pynput.keyboard import Key, Controller
import os
from bind_keys import bindable

# usage: cvpaste.py spam.txt

bindings = {}


# prints msg in-game chat
def printer(key_pressed):
    message = bindings[key_pressed].split('\n')      # list of idividual lines in the message 

    for line in message:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.02)

        keyboard.type(line)   

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.02)
        

# parses file.txt and assigns messages to keybinds
def loadFile(binds : list[Key], file):

    with open(file, 'r', encoding='utf8') as f:
        text = f.read()
        emptyLine = '\n\n'     # empty line acts as a seperator for 2 texts
        msgs = text.split(emptyLine)

    if (len(msgs) != len(bindable)): print('could not have bound all keys/messages')
    
    for key, msg in zip(bindable, msgs):     # zip returns the minimum working tuple length
        bindings[key] = msg
    
    print(f"binded keys: {bindings}")

        
def on_press(key):
    print(key)
    if (key in bindings):
        printer(key)
    if (key == Key.esc): exit()
    


keyboard = Controller()
time.sleep(1)
all_chat = False


try: f = sys.argv[1]
except IndexError: 
    print("text file not specified")
    exit()

if (not os.path.isfile(f)):
    raise FileNotFoundError("passed text file does not exist :(")

# file is read once per program execution
loadFile()



# blocking thread; Collect events until released
with pynput.keyboard.Listener(
        on_press=on_press) as listener:
    print("\nlistening...")
    listener.join()


# # non-blocking thread; Collect events until released, calls on_press and on_release upon key action
# listener = pynput.keyboard.Listener( on_press=on_press, on_release=on_release) 
# listener.start()
# print('\nlistening...')


