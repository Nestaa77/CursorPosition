import pyautogui
import tkinter as tk 
import keyboard
import threading
from infi.systray import SysTrayIcon



root = tk.Tk()
root.attributes("-alpha", 1)
root.config(bg='black')
root.overrideredirect(True)
root.attributes('-topmost', True)

###########################################"
lastClickX = 0
lastClickY = 0
lab_pos = tk.Label(root,text="position : ")
lab_pos.pack()

def Stop(systray):
    root.destroy()
    systray.shutdown()
    th1.root.quit()
menu_options = (("Stop and Quit", "close.ico", Stop),)
systray = SysTrayIcon("icon.ico", "Cursor Position", menu_options)


def SaveLastClickPos():
    while True:
        x,y = pyautogui.position()
        global lastClickX, lastClickY
     
        if 1222 < x <1314 and y <711:
            root.geometry("+%s+%s" % (x-60 , y+30))
            lab_pos.config(text="position : {}".format((x,y)))
            root.update()
            
        elif x > 1314 and y <690:
            root.geometry("+%s+%s" % (x-120 , y+30))
            lab_pos.config(text="position : {}".format((x,y)))
            root.update()
        
        elif x > 1222 and y > 690:
            root.geometry("+%s+%s" % (x-120 , y-60))
            lab_pos.config(text="position : {}".format((x,y)))
            root.update()
        elif x < 1222 and y > 711:
            root.geometry("+%s+%s" % (x-60 , y-60))
            lab_pos.config(text="position : {}".format((x,y)))
            root.update()
        elif x>1222 and y >711:
            root.geometry("+%s+%s" % (x , y))
            lab_pos.config(text="position : {}".format((x,y)))
            root.update()
        
        else:
            root.geometry("+%s+%s" % (x+30 , y+30))
            lab_pos.config(text="position : {}".format((x,y)))
            root.update()
        systray.start()

th1 = threading.Thread(target=SaveLastClickPos)
th1.setDaemon(True)
th1.start()

###############################################""

root.mainloop()