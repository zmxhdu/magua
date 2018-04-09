# codint = utf-8

from tkinter import *
import pip

installed_packages = pip.get_installed_distributions()

app = Tk()
label = Label(text='Python Packages', font=('Hack', 20, 'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2', fg='red')
listbox.pack(fill=BOTH, expand=True)

for package in installed_packages:
    listbox.insert(END, package)

app.mainloop()
app.run()
