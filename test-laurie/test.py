'''
TUTOS:
tkinter:
    https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
makefile:
    https://earthly.dev/blog/python-makefile/
    https://stackabuse.com/how-to-write-a-makefile-automating-python-setup-compilation-and-testing/
    https://blog.horejsek.com/makefile-with-python/
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])

value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()

fenetre.mainloop()