##########################################################################
# PSKill allows bulk task kill. 
# List of tasks are maintained and pulled from a text file
# 
# ##########################################################################

import psutil 
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import font

#######################################################################
# globals
f_exit = False
window = ''
fr1 = ''
fr2 = ''
fr2 = ''
ps = []
fname = "pskill.txt"
#######################################################################

#######################################################################

def create_default_file():
    f = open(fname, "w+")


    filedata = """jusched.exe
onenotem.exe
chrome.exe"""
    
    f.write(filedata)
    f.close()
    msg = "Config file 'pskill.txt' not found. Default file has been created in the folder.\nReview / Edit the file as required and run the program again. "         
    messagebox.showinfo('FreeMem', msg)
    

def read_file():
    f = open(fname, "r")
    ps = f.read().splitlines()
    return ps
    

def init():
# process list in format name:process 
    global f_exit

    if os.path.isfile(fname):
        f = open(fname)
        return f
    else:
        f_exit = True
        create_default_file()


   
def freemem():
    global fr1
    ps = read_file()
    cnt = 1

    fr1.destroy()
    # frame 1 - process list
    fr1 = tk.Frame(window, relief=tk.RIDGE, borderwidth=5)
    fr1.place(relheight = .85, relwidth = .4)

    for i in psutil.process_iter():
        # print(i.name())

        if i.name() in ps:    
            # print(f'Killing redundant process  {i.name()} ')
            cb = tk.Checkbutton(fr1, text=i.name(), anchor=tk.W, width=12, state=tk.DISABLED)
            cb.grid(row=cnt + 1, columnspan=2)

            try:
                i.kill()
                i.wait()                
            except:
                cb.deselect()
            else:
                cb.select()
            cnt+=1
    
    messagebox.showinfo('FreeMem','Process cancelled.') 


#################################################################
# Define layout
def set_layout():
    global window, fr1, fr2, fr3
    
    # window 
    window = tk.Tk()    
    window.title('FreeMem')
    window.geometry("380x700+50+50")
    window.resizable(0, 0)


    # frame 1 - process list
    fr1 = tk.Frame(window, relief=tk.RIDGE, borderwidth=5)
    fr1.place(relheight = .85, relwidth = .4)

    # frame 2 - text
    fr2 = tk.Frame(window,  relief=tk.RIDGE, borderwidth=5)
    fr2.place(relx = .4, relheight = .85, relwidth = .6)

    # frame 3 - OK Button
    fr3 = tk.Frame(window,  relief=tk.RIDGE, borderwidth=5)
    fr3.place(rely=.85, relheight=.15, relwidth=1)


    # frame 2 widgets
    lbl = """This tool frees up memory by cancelling processes.

List of processes that will be tried to cancel are stored in a file pskill.txt. The file should be in the same folder as the tool. 

Please note, some of these processes can restart automatically. Hence use this tool as when needed.





*************************************

1. Checkbox SELECTED - Processes successfully cancelled 

2. Checkbox DE-SELECTED - Possible authorization errors. Processes could not be cancelled. Run the tool as Administrator

3. Process name do not appear in list - Means process is not running.

*************************************





*** Disclaimer ***
Force killing a process may result in unexpected behaviour/error."""

    tk.Label(fr2, text=lbl, anchor=tk.W, wraplength=200, padx = 10, justify = tk.LEFT ).grid(row=1)



    # frame 3 widgets
    btn_freemem = tk.Button(fr3, text='Free Memory', bg='green', command=freemem, width=200)
    btn_freemem['font'] = font.Font(size=30)
    btn_freemem.pack(side=tk.LEFT, fill=tk.BOTH)


#################################################################

# main
if __name__ == "__main__":
    set_layout()
    init()
    if f_exit == False:
         window.mainloop()
  