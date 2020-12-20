from tkinter import *
import sqlite3
import addPeople


####database connection
con=sqlite3.connect('database.db')
cur = con.cursor()


####window that connects and opens from main.py to myPeople.py
class myPeopleClass(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("Meine Kontakte")
        self.resizable(False,False)

        #Frames
        self.top=Frame(self,height=150,bg='#8EE26B')
        self.top.pack(fill=X)
        ###top frame of mainwindow

        ####################################################
        self.bottomFrame=Frame(self,height=500,bg='#EB5352')    ##udemyrot
        self.bottomFrame.pack(fill=X)                           #
        ###bottom frame of mainwindow#######################


        ###head
        self.heading=Label(self.top,text='Meine Kontakte', font='arial 15 bold', fg='#29303B', bg='#8EE26B')
        self.heading.place(x=230, y=60) ##place text
        ###image
        self.top_image=PhotoImage(file='icons/resizedmycontacts.png')
        self.top_image_label = Label(self.top, image= self.top_image, bg='#8EE26B', width=100, height=100)
        self.top_image_label.place(x=120,y=15) ##place image

        ##scrollBar
        self.sb=Scrollbar(self.bottomFrame,orient=VERTICAL)
        ##listbox
        self.listBox=Listbox(self.bottomFrame,width=60,height=31)
        self.listBox.grid(row=0, column=0, padx=(40,0))
        self.sb.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=1,sticky=N+S)

        ##Buttons

        buttonAdd = Button(self.bottomFrame, text='Hinzufügen', width=12, font='arial 12 bold', command=self.funcAddPeople)
        buttonAdd.grid(row=0,column=2, sticky=N, padx=10, pady=10)

        buttonUpdate = Button(self.bottomFrame, text='Aktualisieren', width=12, font='arial 12 bold')
        buttonUpdate.grid(row=0,column=2, sticky=N, padx=10, pady=60)

        buttonDisplay = Button(self.bottomFrame, text='Anzeigen', width=12, font='arial 12 bold')
        buttonDisplay.grid(row=0,column=2, sticky=N, padx=10, pady=110)

        buttonDelete = Button(self.bottomFrame, text='Löschen', width=12, font='arial 12 bold')
        buttonDelete.grid(row=0,column=2, sticky=N, padx=10, pady=160)


    def funcAddPeople(self):
        addPage = addPeople.addPeople()