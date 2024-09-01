import tkinter
import tkinter.messagebox
import tkinter as tk
import tkinter.scrolledtext
import os
import platform
import datetime
from tkinter import ttk
from tkinter import StringVar
from PyQt6.QtWidgets import *
from tkinter import PhotoImage
from tkinter import Canvas




c=0
a=0
h=10
plus=1
store=0
key=0
confing=['繁體中文-Chinese(Traditional)'
         , '简体中文- Chinese (Simplified)'
         , 'English-English (United States)']
zh_tw=['運行系統:', ' (註:非Windows系統無法運行此程式)', '電腦使用防止鎖 簡單、粗暴、強效   by ABestCookie', 
       '如果有空，不仿造訪一下: https://www.github.com/ABestCookie', '警告', '電腦即將鎖定', 
       '資訊', '電腦已解除鎖定', '錯誤', '密碼錯誤',
       '電腦使用防止鎖', '輸入密碼來解除鎖定', 
       '請不要手貝戈戈把視窗關掉', '解除鎖定', 
       '設定密碼', '檔案', '幫助', '設定', '退出', 
       '關於', '請設定密碼', '請務必記住密碼', 
       '除非你非常了解windows系統', '鎖定電腦', '為什麼你需要用這玩意兒', 'zh-TW']
zh_cn=['运行系统:', ' (注:非Windows系统无法运行此程序)', '计算机使用防止锁 简单、粗暴、强效   by ABestCookie', 
       '如果有空，不仿造访一下: https://www.github.com/ABestCookie', '警告', '计算机即将锁定', 
       '信息', '计算机已解除锁定', '错误', '密码错误',
       '计算机使用防止锁', '输入密码来解除锁定', 
       '请不要手残把窗口关掉', '解除锁定', 
       '设定密码', '档案', '帮助', '设定', '退出', 
       '关于', '请设定密码', '请务必记住密码', 
       '除非你非常了解windows系统', '锁定计算机', '为什么你得用这玩意儿', 'zh-CN']
en_us=['Running system:', ' (Note: Non-Windows systems cannot run this program)', 'Computer usage prevention lock. Simple, Useful and Powerful by ABestCookie',
        'If you are free, please visit: https://www.github.com/ABestCookie', 'Warning', 'The computer is about to be locked',
        'Message', 'Computer has been unlocked', 'Error', 'Wrong password',
        'Computer usage protection lock', 'Enter password to unlock',
        'Please do not close the window with your hands', 'Unlock',
        'Set password', 'File', 'Help', 'Settings', 'Exit',
        'About', 'Please set a password', 'Please remember the password',
        'Unless you know Windows very well', 'Lock', 'Why do you have to use this thing', 'en-US']

getconf=open('resources/language.txt', 'r')
conf=getconf.read()
getconf.close()
if conf==confing[0]:
    word=zh_tw
if conf==confing[1]:
    word=zh_cn
if conf==confing[2]:
    word=en_us
else:
    word=zh_tw
system=(word[0] + platform.system() + word[1] + ' ' + word[25] + ' mode')
print(word[2])
print(word[3])
print(system)

def timer():
    #時間及時處理函數，用來顯示時間
    global t
    t=datetime.datetime.now()
    w2["text"]=t
    main.after(10, timer)
def killer():
    os.system("taskkill /f /im explorer.exe")
    main.after(1000, timer)
def lock():
    #除了拿來顯示鎖定沒別的屁用的東西
    global a
    global store
    global t
    t=datetime.datetime.now()
    a=entry.get()
    
    #缺時間注入
    store=open('resources/history.txt', 'a')
    store.write('password:')
    store.write(a)
    store.write(' [')
    store.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    store.write('] \n')
    store.close()
    
    tkinter.messagebox.showwarning(word[4],word[5])
    password.destroy()
    

def unlock():
    #這東西就是解除鎖定
    global b
    global c
    
    b=e2.get()
    print(b)
    if a==b:
        tkinter.messagebox.showinfo(word[6],word[7])
        main.destroy()
        os.system("explorer.exe")
        c=1
    else:
        tkinter.messagebox.showerror(word[8],word[9])

def mainwindow():
    #鎖起來後的主視窗
    global main
    global w2
    global w5
    global w6
    global e2
    global bt2
    global icon
    
    #os.system("taskkill /f /im explorer.exe")#危險的玩意兒#
    main=tkinter.Tk()
    main.title(word[10])
    main.geometry("400x300")
    main.iconbitmap(icon)
    main.resizable(False, False)
    w2=tkinter.Label(main, text="----------", font=("System", 12))
    w2.place(x=20, y=250)
    w5=tkinter.Label(main, text=word[11], font=("System", 12))
    w5.place(x=20, y=30)
    w6=tkinter.Label(main, text=word[12], font=("System", 12))
    w6.place(x=20, y=90)
    e2=ttk.Entry(main, width=25)
    e2.place(x=20, y=60)
    bt2=ttk.Button(main, text=word[13], command=unlock)
    bt2.place(x=20, y=120)
    timer()
    main.mainloop()

def exit_app():
    global c
    c=1
    password.destroy()
def set_app():
    def set_exit():
        mainset.destroy()
    def history():
        os.system("textviewer.exe resources/history.txt")
    def darkmode():
        global setting_write
        setting_write=open('resources/temp.txt', 'w')
        if bg_cval.get()==True:
            setting_write.write('bgcolor=#2F3136')
        else:
            setting_write.write('bgcolor=#f1f1f1')
        setting_write.close()
    def show(It_is_useless_but_it_need_to_stay_here):
        global lg
        lg=open('resources/language.txt','w')
        lg.write(ListVariable.get())
        lg.close()
            
    global mainset
    global icon
    global out
    global bg_cval
    global setting_write
    global bg_cbt
    global language
    global ListVariable
    global Ver_List
    mainset=tkinter.Tk()
    mainset.title("設定")
    mainset.geometry("800x450")
    mainset.resizable(False, False)
    icon=os.path.join("resources", "Settings.ico")
    mainset.iconbitmap(icon)
    out=tk.Menu(mainset)
    out.add_command(label='保存設定', command=set_exit)#apply
    out.add_command(label='密碼歷史', command=history)
    mainset.config(menu=out)
    bg_cval=tkinter.BooleanVar(mainset)
    #判斷是否已啟用深色模式
    setting_write=open('resources/temp.txt', 'r')
    setting_write.seek(8)
    if setting_write.read()=="#f1f1f1":
        bg_cval.set(False)
    else:
        bg_cval.set(True)
    setting_write.close()

    bg_cbt=ttk.Checkbutton(mainset, text="啟用深色模式(重啟程式生效)", variable=bg_cval, command=darkmode)
    bg_cbt.pack()
    language=['(空的)', '繁體中文-Chinese(Traditional)', '简体中文- Chinese (Simplified)', 'English-English (United States)']
    ListVariable = StringVar(mainset)
    Ver_List = ttk.OptionMenu(mainset, ListVariable, *language, command=show)
    Ver_List.configure(width=30)
    Ver_List.pack()
    mainset.mainloop()

def about():
    app = QApplication([])
    window = QLabel('')
    text = "<center>" \
                "<h1>電腦使用防止鎖</h1>" \
                "&#8291;" \
                "<img src=resources/icon.png>" \
                "</center>" \
                "<p>版本 b0.1開發版 <br/>" \
                "此程式由ABestCookie撰寫，請自由使用</p>"
    QMessageBox.about(window, "關於", text)
    window.show()
    app.exec()
def fun():
    global h
    global plus
    w5.place(x=h, y=230)
    if (h<-50):
        plus=1
    if (h>350):
        plus=0
    if (plus==1):
        h=(h+10)
    if (plus==0):
        h=(h-10)
    password.after(50, fun)



#設置密碼的視窗
password=tkinter.Tk()#ThemedTk(theme="equilux")
password.title(word[14])
password.geometry("500x400")
icon=os.path.join("resources", "icon.ico")
get_set=open('resources/temp.txt', 'r')
get_set.seek(8)
bg_color=get_set.read()
password.configure(background=bg_color)
password.iconbitmap(icon)
password.resizable(False, False)#鎖定視窗
menubar=tk.Menu(password)
filemenu=tk.Menu(menubar, tearoff=0)
helpmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label=word[15], menu=filemenu)
menubar.add_cascade(label=word[16], menu=helpmenu)
filemenu.add_command(label=word[17], command=set_app)
filemenu.add_separator()
filemenu.add_command(label=word[18], command=exit_app)
helpmenu.add_command(label=word[19], command=about)
password.config(menu=menubar)

w1=tkinter.Label(password, text=word[20], font=("Times New Roman", 20))
w1.place(x=150, y=20)
w3=tkinter.Label(password, text=word[21], font=("Times New Roman", 18))
w3.place(x=150, y=110)
w4=tkinter.Label(password, text=word[22], font=("Times New Roman", 18))
w4.place(x=105, y=150)
entry=ttk.Entry(password, width=35)
entry.place(x=90, y=70)
bt1=ttk.Button(password, text=word[23], command=lock)
bt1.place(x=350, y=70)
w6=tkinter.Label(password, text=system, font=("Times New Roman", 8))
w6.place(x=0, y=360)
w5=tkinter.Label(password, text=word[24], font=("Times New Roman", 25))
fun()
password.mainloop()

if (a==0):
        c=1

while(True):
    if (c==1):
        #跳出迴圈
        break
    else:
        mainwindow()
#2024/9/1 上午10:22 我操他媽的終於把這鬼東西做完了!!!!!!!



