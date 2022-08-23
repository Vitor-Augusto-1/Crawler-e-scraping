import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir Browser')
root.geometry('500x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text= 'Google', command=google).pack(pady=20)
root.mainloop()
