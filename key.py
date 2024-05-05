import keyboard
import os

print('Press the "Escape" key to stop the program from running.')

recorded = keyboard.record(until='esc') 

with open("keyboard.txt", "w") as f:
    f.writelines(str(recorded))

with open('keyboard.txt', 'r') as f:
    text = f.read()
    characters = []
    for char in text:
        characters.append(char)
    
charbetween = []
between = False

for char in characters:
    if char == '(':
        between = True
    elif char == ')':
        between = False
    elif between:
        charbetween.append(char)

with open('cleaner.txt', 'w') as f:
    f.writelines(charbetween)

with open('cleaner.txt', 'r') as f:
    text = f.read()
    characters2 = []
    for char in text:
        characters2.append(char)

charbetween2 = []
between2 = False

for char2 in characters2:
    if char2 == 'n':
        between2 = True
    elif char2 == ' ':
        between2 = False
    elif between2:
        charbetween2.append(char2)

with open('clean.txt', 'w') as f:
    f.writelines(charbetween2)
    os.remove('keyboard.txt')
    os.remove('cleaner.txt')