from pyautogui import press, typewrite, hotkey #Imports PyAutoGui whitch is need for this to work
import time #Imports time whitch is needed as a wait command
keystroke = raw_input("Enter your keystroke: ") #raw_input is a function to ask for user input then sets input as the variable: keystroke
amount = raw_input("Enter the amount of times you want your keystroke to continue: ")
delay = raw_input("Enter the time(seconds) you want to wait till the keystroke starts: ")
isinstance( delay, int )

#typewrite(keystroke) #This part is the typing part

#The following part is the end part.
delay = str(delay) #Converts the variable so it can be used in the next command. The reason is beyond my understanding.
print "Starting keystroke in "+delay+" second(s)" #Prints how long till the the keystroke starts
delay = float(delay) #Converts it so it works as a float value. Still beyond my reasoning.
time.sleep(delay)
