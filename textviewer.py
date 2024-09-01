import tkinter
import os
import tkinter.scrolledtext
import tkinter as tk
import sys
try:
    get=sys.argv[1]
    try:
        hisopen=open(get,'r')
        hisget=hisopen.read()
        hisopen.close()
        def set_exit():
            main.destroy()
        main=tkinter.Tk()
        main.title("TextViewer")
        main.geometry("400x300")
        main.resizable(False, False)
        icon=os.path.join("resources", "Settings.ico")
        main.iconbitmap(icon)
        out=tk.Menu(main)
        out.add_command(label='exit', command=set_exit)
        main.config(menu=out)
        text=tkinter.scrolledtext.ScrolledText(main)
        text.place(x=0, y=0, width=400, height=300)
        text.insert(tkinter.END, hisget)
        main.mainloop()
    except:
        os.system("notepad")
except:
    os.system("notepad")