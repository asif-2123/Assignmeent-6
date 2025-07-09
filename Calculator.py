from tkinter import *

window=Tk()

window.title("CALCULATOR")
window.geometry('600x500')
window.config(bg='grey')

e=Entry(window,width=64,borderwidth=15)
e.place(x=0,y=0)

def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

b=Button(window,text='9',width='17',height='5',command=lambda :click(9))
b.place(x=10,y=90)

b=Button(window,text='8',width='17',height='5',command=lambda :click(8))
b.place(x=150,y=90)

b=Button(window,text='7',width='17',height='5',command=lambda :click(7))
b.place(x=290,y=90)

b=Button(window,text='6',width='17',height='5',command=lambda :click(6))
b.place(x=10,y=190)

b=Button(window,text='5',width='17',height='5',command=lambda :click(5))
b.place(x=150,y=190)

b=Button(window,text='4',width='17',height='5',command=lambda :click(4))
b.place(x=290,y=190)

b=Button(window,text='3',width='17',height='5',command=lambda :click(3))
b.place(x=10,y=290)

b=Button(window,text='2',width='17',height='5',command=lambda :click(2))
b.place(x=150,y=290)

b=Button(window,text='1',width='17',height='5',command=lambda :click(1))
b.place(x=290,y=290)

b=Button(window,text='0',width='17',height='5',command=lambda :click(0))
b.place(x=150,y=390)

def clear():
    e.delete(0,END)

b=Button(window,text='<--',width='17',height='5',command=clear,bg='orange')
b.place(x=10,y=390)

def add():
    n1=e.get()
    global math
    math='addition'
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text='+',width='17',height='5',command=add,bg='lavender')
b.place(x=430,y=90)

def sub():
    n1=e.get()
    global math
    math='subtraction'
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text='-',width='17',height='5',command=sub,bg='lavender')
b.place(x=430,y=190)

def mul():
    n1=e.get()
    global math
    math='multiplication'
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text='*',width='17',height='5',command=mul,bg='lavender')
b.place(x=430,y=290)

def div():
    n1=e.get()
    global math
    math='division'
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window,text='/',width='17',height='5',command=div,bg='lavender')
b.place(x=430,y=390)

def equal():
    n2=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,i+int(n2))
    elif math=='subtraction':
        e.insert(0,i-int(n2))
    elif math=='multiplication':
        e.insert(0,i*int(n2))
    elif math=='division':
        e.insert(0,i/int(n2))

b=Button(window,text='=',width='17',height='5',command=equal,bg='light green')
b.place(x=290,y=390)




mainloop()