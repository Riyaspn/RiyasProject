from tkinter import *

import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="Red")

r_button = Button(st,text="Restart",font=("Times New Roman",35,"bold"),relief=RAISED,cursor="circle",command=restart)
r_button.place(x=150,y=10,height=60,width=200)

rt_button = Button(st,text="Restart Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=80,height=60,width=200)

lg_button = Button(st,text="Log Out",font=("Times New Roman",35,"bold"),relief=RAISED,cursor="circle",command=logout)
lg_button.place(x=150,y=150,height=60,width=200)

st_button = Button(st,text="Shut Down",font=("Times New Roman",30,"bold"),relief=RAISED,cursor="circle",command=shutdown)
st_button.place(x=150,y=220,height=60,width=200)




st.mainloop()