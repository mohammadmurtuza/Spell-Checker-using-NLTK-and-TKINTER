import tkinter as tk
from tkinter import *
from textblob import TextBlob

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='SPELLING CHECKER')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='ENTER WORD OR SENTENCE:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def Spell():
    a= entry1.get()
    b=TextBlob(a)

    label3 = tk.Label(root, text= 'incorrect: ' + a ,font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label1 = tk.Label(root, text='Corrected: '+str(b.correct()))
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Check', command=Spell,bg='red',fg='white')
canvas1.create_window(200, 180, window=button1)



root.mainloop()
