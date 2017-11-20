#!/usr/local/bin/python
from pyautogui import press, typewrite, hotkey #Imports PyAutoGui whitch is need for this to work
import time, sys #Imports time whitch is needed as a wait command
i = 1
keystroke = raw_input("Enter your keystroke: ") #raw_input is a function to ask for user input then sets input as the variable: keystroke
amount = raw_input("Enter the amount of times you want your keystroke to continue: ")
delay = raw_input("Enter the time(seconds) you want to wait till the keystroke starts: ")
enter = raw_input('Enter after each line?(y/n): ')
isinstance( delay, int )
#typewrite(keystroke) #This part is the typing part
if enter == "y":
    print 'Selection confirmed'
else:
    print 'Selection confirmed'


#The following part is the end part.
delay = str(delay) #Converts the variable so it can be used in the next command. The reason is beyond my understanding.
print "Starting keystroke in "+delay+" second(s)" #Prints how long till the the keystroke starts
delay = float(delay) #Converts it so it works as a float value. Still beyond my reasoning.
time.sleep(delay)

if enter == "y":
    while i < int(amount):
        print i
        typewrite(keystroke)
        typewrite('\n')
        i = i + 1
    typewrite(keystroke)
    typewrite('\n')
    print i
    print("Done\nExiting in 5 seconds")
    time.sleep(5)
    sys.exit()

else:
    while i < int(amount):
        print i #Print the number you are at
        typewrite(keystroke) #The macro
        i = i + 1 #Ups a variable by 1
    print i
    typewrite(keystroke) #Uses macro 1 extra time
    time.sleep(5) #Sleeps before exit
