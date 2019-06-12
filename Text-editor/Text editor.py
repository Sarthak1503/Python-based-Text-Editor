from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os
import time
from tkinter.filedialog import *
from tkinter import messagebox

def op(root,sr):
    try:
        a=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("JavaScript", "*.js")])
        f=open(a,'r')
        root.title('{}-Sarthak'.format(os.path.basename(a)))
        sr.delete(1.0,END)
        sr.clipboard_clear()
        sr.insert(INSERT,f.read())
        f.close()
    except:
        pass
def save(root,sr):
    try:
        a=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("JavaScript", "*.js")])
        f=open(a,'w')
        root.title('{}-Sarthak'.format(os.path.basename(a)))
        f.write(sr.get(1.0,END))
        f.close()
    except:
        pass

def ne(root):
    root.destroy()
    main()

def ex(root,top):
    top.destroy()
    root.destroy()

def clos(root):
    top=Toplevel()
    m=Label(top,text='Do you want to exit?')
    m.grid(row=0)
    b1=Button(top,text='Yes',command=lambda :ex(root,top))
    b2=Button(top,text='No',command=top.destroy)
    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)

def copy(sr):
    try:
        sr.clipboard_clear()
        text = sr.get("sel.first", "sel.last")
        sr.clipboard_append(text)
    except:
        pass

def cut(sr):
    try:
        sr.clipboard_clear()
        text = sr.get("sel.first", "sel.last")
        sr.clipboard_append(text)
        sr.delete("sel.first", "sel.last")
    except:
        pass

def aste(sr):
    try:
        text=sr.clipboard_get()
        print(text)
        sr.insert(INSERT,text)
    except:
        pass

def und(sr):
    try:
        sr.edit_undo()
    except:
        print('Nothing for undo')

def redo(sr):
    try:
        sr.edit_redo()
    except:
        print('Nothing to Redo')
def colo(sr,b):
    color = {
        'Default': '#000000.#FFFFFF',
        'Greygarious': '#83406A.#D1D4D1',
        'Aquamarine': '#5B8340.#D1E7E0',
        'Bold Beige': '#4B4620.#FFF0E1',
        'Cobalt Blue': '#ffffBB.#3333aa',
        'Olive Green': '#D1E7E0.#5B8340',
        'Night Mode': '#FFFFFF.#000000',
    }

    sr.configure(bg=color[b],fg='red')
def help(root):
    messagebox.showinfo("Help","This is a simple Notead")

def abut(root):
    messagebox.showinfo("About",'This is a Notepad.\nCreated by Decider groups')

def ln(t):
    num=get_line_numbers()
    t.state=NORMAL
    t.insert(1.0,num)
    #t.state=DISABLED


def up(event,root,sr,st):
    print('INSIDE')
    a=sr.get(1.0,END)
    print(a)
    l=a.split('.')
    print(l)
    st.config(text=len(l))

def status(sr,text,st):
    b=sr.index(INSERT)
    a=float(b)
    row=str(int(a))
    col=int(b[len(row)+1:])+1
    st.config(text='row:{},column:{}'.format(row,col))
    change(text,sr,row)

def red(root):
    if messagebox.askokcancel("Quit","Do You Want to Quit?"):
        root.destroy()
k=0
def change(t,sr,row):
    global k

    n = int(float(sr.index(END)))-1
    if n>k:
        print('In')
        t.insert(INSERT,str(n)+'\n')
        k=n
    if n<k:
        t.delete(END)

def main():

    root=Tk(className='Untitled-Notepad')
    #root.iconbitmap('favicon.ico')

    n = PhotoImage(file="new_file.gif")
    c = PhotoImage(file="cut.gif")
    s=PhotoImage(file="save.gif")
    cp=PhotoImage(file="copy.gif")
    on = PhotoImage(file="open_file.gif")
    un = PhotoImage(file="undo.gif")
    pas = PhotoImage(file="paste.gif")
    rd = PhotoImage(file="redo.gif")

    #************************************For Menu***************************
    men=Menu(root,tearoff=0)
    root.config(menu=men)
    submenu=Menu(men,tearoff=0)

#****************************************Menu OF FILE****************************************
    men.add_cascade(label='File',menu=submenu)
    submenu.add_command(label='New',accelerator='Ctrl+N',compound=LEFT, image=n,command=lambda :ne(root))
    root.bind('<Control-n>',lambda event: ne(root))
    submenu.add_command(label='Open',accelerator='Ctrl+O',compound=LEFT, image=on,command=lambda :op(root,sr))
    root.bind('<Control-o>', lambda event: op(root,sr))
    submenu.add_command(label='Save',accelerator='Ctrl+S',compound=LEFT, image=s,command=lambda:save(root,sr))
    root.bind('<Control-s>', lambda event: save(root,sr))
    submenu.add_command(label='Save as',accelerator='Alt+S', command=root.destroy)
    submenu.add_command(label='Close',accelerator='Ctrl+Q', command=lambda:clos(root))
    root.bind('<Control-q>', lambda event:clos(root))
    submenu=Menu(men,tearoff=0)

#*****************************************Menu of Edit************************
    men.add_cascade(label='Edit',menu=submenu)
    submenu.add_command(label='Cut',image=c,accelerator='Ctrl+X',compound=LEFT,command=lambda :cut(sr))
    root.bind('<Control-b>',lambda event:cut(sr))
    submenu.add_command(label='Copy',image=cp,accelerator='Ctrl+C',compound=LEFT,command=lambda :copy(sr))
    root.bind("<Control-c>", lambda event: copy(sr))
    submenu.add_command(label='Paste',image=pas,accelerator='Ctrl+P',compound=LEFT,command=lambda :aste(sr))
    root.bind('<Control-v>',lambda event:aste(sr))
    submenu.add_command(label='Undo',image=un,accelerator='Ctrl+Z',compound=LEFT,command=lambda :und(sr))
    submenu.add_command(label='Redo',image=rd,accelerator='Ctrl+B',compound=LEFT,command=lambda :redo(sr))
#*****************************************Menu of View****************************
    submenu = Menu(men, tearoff=0)

    men.add_cascade(label='View', menu=submenu)
    v=BooleanVar()
    v.set(FALSE)
    #submenu.add_checkbutton(label='Status Bar',onvalue=1,offvalue=0,variable=v, command=lambda:root.destroy())
    sub = Menu(submenu, tearoff=0)
    submenu.add_cascade(label='Theme',menu=sub)

    sub.add_command(label='Default', command=lambda :colo(sr, 'Default'))
    sub.add_command(label='Greygarious', command=lambda :colo(sr,'Greygarious'))
    sub.add_command(label='Aquamarine', command=lambda:colo(sr,'Aquamarine'))
    sub.add_command(label='Bold Beige', command=lambda:colo(sr,'Bold Beige'))
    sub.add_command(label='Cobalt Blue', command=lambda:colo(sr,'Cobalt Blue'))
    sub.add_command(label='Olive Green', command=lambda:colo(sr,'Olive Green'))
    sub.add_command(label='Night Mode', command=lambda: colo(sr,'Night Mode'))



    submenu=Menu(men,tearoff=0)
    men.add_cascade(label='Help',menu=submenu)
    submenu.add_command(label='Help',command=lambda :help(root))
    submenu=Menu(men,tearoff=0)
    men.add_cascade(label='About',menu=submenu)
    submenu.add_command(label='About',command=lambda :abut(root))





    f6 = Frame(root, height=30, width=1360)
    f6.pack(side=TOP,anchor=W)
    b1 = Button(f6, image=n, height=30, width=45, command=lambda: ne(root))
    b1.pack(side=LEFT)
    b2 = Button(f6, image=on, height=30, width=45, command=lambda: op(root,sr))
    b2.pack(side=LEFT)
    b2 = Button(f6, image=s, height=30, width=45, command=lambda: save(root,sr))
    b2.pack(side=LEFT)
    b3 = Button(f6, image=cp, height=30, width=45, command=lambda: copy(sr))
    b3.pack(side=LEFT)
    b4 = Button(f6, image=c, height=30, width=45, command=lambda: cut(sr))
    b4.pack(side=LEFT)
    b5 = Button(f6, image=pas, height=30, width=45, command=lambda: aste(sr))
    b5.pack(side=LEFT)
    b6 = Button(f6, image=un, height=30, width=45, command=lambda: und(sr))
    b6.pack(side=LEFT)
    b7 = Button(f6, image=rd, height=30, width=45, command=lambda: redo(sr))
    b7.pack(side=LEFT)
###########################################        side number using text widget

    sc = Scrollbar(root)
    sc.pack(side=RIGHT, fill=Y)


    t=Text(root,width=11,bg='grey',yscrollcommand=sc.set)
    t.pack(side=LEFT,fill=Y)


    f1=Frame(root,height=710,width=1330)
    f1.pack(expand=YES,fill=BOTH)
    sr = Text(f1,yscrollcommand=sc.set)
    sr.pack(expand=YES, fill=BOTH)
    sc.config(command=sr.yview)

    st = Label(root,text='Line:{} Column:{}'.format(1,1),relief=RAISED,anchor=E)
    st.pack(side=BOTTOM,fill=X)

    sr.bind("<<Text_Modified>>",lambda event:change(event,t,sr))
    root.bind('<Key>',lambda event:status(sr,t,st))
    root.protocol("WM_DELETE_WINDOW",lambda :red(root))
    mainloop()


main()
