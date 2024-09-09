# pynumlock
A program that uses python to integrate with AutoHotKey to ensure the numberlock key stays on throughout the day.

Sometimes my numlock key seems to randomly turn off throughout the day. This script is designed to run to automatically turn it on if it detects it is off, checking every 60 seconds.

#Requirements:
-Python Installed
-Python Library pywin32 Installed (can be installed using "pip install pywin32" in cmd)
-AutoHotKey Installed

#Configuration
By default the script checks every 60 seconds and runs for 8 hours. This can be reconfigured in the beginning of the "main()" function

#Includes a numlock.pyw file which can be run by Windows as an executable in the background and scheduled to start on startup

#Stopping Script Mid-Runtime
By default, the program will stop if it detects that the CAPS LOCK is on when it checks the numlock key. If you frequently use CAPS LOCK you may want to either comment this out or change the exit key to a different one.
