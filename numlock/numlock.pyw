'''
@Author: Brett Benischek
@Date: 9-7-24
@File: numlock.py

#This Script is Intended to Make Sure the 'Numlock' key stays in the on state. 
Checks every minute, and if it is "off" then it turns it back "on".

#List of virtual Keycodes: http://www.kbdedit.com/manual/low_level_vk_list.html
#*******************
External Libraries

pywin32 -> https://pypi.org/project/pywin32/
=>pip install pywin32

#*******************
'''
from win32api import GetKeyState
from win32con import VK_NUMLOCK
from win32con import VK_CAPITAL

import os
import time
#************************************

#Functions
#************************************
#Main Program
def main() -> None:
    #*****SCRIPT CONFIGURATION*****************************
    #How often Program Will Check Key State (in seconds). 60 recommended
    chk_sc:int = 60

    #How Many Times the Program Will Check Key State 
    #(if chk_sc==60, this is how many minutes the program will run). hrs * 60 for hours
    prg_len:int = 8 * 60
    #*****SCRIPT CONFIGURATION*****************************

    #Count of How many times Program Has Checked Key State
    r_ct:int = 0

    while r_ct < prg_len - 1:
        #Check if Numlock is on
        if GetKeyState(VK_NUMLOCK)==False:
            press_script()
            #print("Numlock Turned On",end="")

        #Stops Program Early if Caps Lock is on
        if GetKeyState(VK_CAPITAL)==True:
            #print("Program Terminated. Caps lock on.")
            break

        #Sleep 1 min then increment
        #print(f"{r_ct}")
        time.sleep(chk_sc)
        r_ct = r_ct + 1

    print("Program Ended", end="")

#Start the AutoHotkey Script in order to press the number lock key
def press_script() -> None:
    #f_dir:str = "C:\\Users\\brett\\Documents\\programs\\Autohotkey\\scripts\\"
    #Gets the Directory of the Python File You Are Running
    f_dir:str = os.path.dirname(os.path.realpath(__file__))
    f_nm:str = "numlock.ahk" #Assumes The AutoHotKey File is in the Same Folder As the Python Script
    os.chdir(f_dir)
    os.startfile(f_nm)
#************************************
#Start Program
if __name__ == "__main__":
    main()



