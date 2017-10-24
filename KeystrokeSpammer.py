from pyautogui import press, typewrite, hotkey #Imports PyAutoGui whitch is need for this to work
import time #Imports time whitch is needed as a wait command
keystroke = raw_input("Enter your keystroke: ") #raw_input is a function to ask for user input then sets input as the variable: keystroke
amount = raw_input("Enter the amount of times you want your keystroke to continue(type 0 for loop): ")
delay = raw_input("Enter the time(seconds) you want to wait till the keystroke starts: ")
if amount == 0:
    print "Success"

#typewrite('Hello world')
#time.sleep(2)
