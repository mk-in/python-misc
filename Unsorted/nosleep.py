##########################################################################
# This is a fun tool
# It does 2 things
## Prevents system(windows) from sleeping
## Moves the mouse indefinitely to prevent focused app from timing out
# To EXIT -> Move the mouse to top left corner of the screen
##########################################################################

import pyautogui
import time
import os

class WindowsInhibitor:
    '''Prevent OS sleep/hibernate in windows; code from:
    https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/preventsuspendplus/core.py
    API documentation:
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx'''
    
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001

    def __init__(self):
        pass

    def inhibit(self):
        import ctypes
        # print("Preventing Windows from going to sleep")
        ctypes.windll.kernel32.SetThreadExecutionState(
            WindowsInhibitor.ES_CONTINUOUS | \
            WindowsInhibitor.ES_SYSTEM_REQUIRED)

    def uninhibit(self):
        import ctypes
        # print("Allowing Windows to go to sleep")
        ctypes.windll.kernel32.SetThreadExecutionState(
            WindowsInhibitor.ES_CONTINUOUS)


osSleep = None

# head start for user to bring app into focus
time.sleep(5)


# in Windows, prevent the OS from sleeping while we run
if os.name == 'nt':
    osSleep = WindowsInhibitor()
    osSleep.inhibit()

# mouse movement
while True:
    pyautogui.moveTo(900,600,duration=1)
    pyautogui.moveTo(300,300,duration=1)

# exit
if osSleep:
    osSleep.uninhibit()