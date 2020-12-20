from tkinter import *
import sqlite3


con=sqlite3.connect('database.db')
cur=con.cursor()


class addPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title('Add People')
        self.resizable(False, False)


        #Frames
        self.top=Frame(self,height=150,bg='#8EE26B')
        self.top.pack(fill=X)
        ###top frame of mainwindow

        ####################################################
        self.bottomFrame=Frame(self,height=500,bg='#EB5352')    ##udemyrot
        self.bottomFrame.pack(fill=X)                           #
        ###bottom frame of mainwindow#######################


        ###head
        self.heading=Label(self.top,text='Benutzer hinzufügen', font='arial 15 bold', fg='#29303B', bg='#8EE26B')
        self.heading.place(x=230, y=60) ##place text
        ###image
        self.top_image=PhotoImage(file='icons/resizedmycontacts.png')
        self.top_image_label = Label(self.top, image= self.top_image, bg='#8EE26B', width=100, height=100)
        self.top_image_label.place(x=120,y=15) ##place image

        self.bottom_image=PhotoImage(file='icons/resizedbenutzer.png')
        self.bottom_image_label = Label(self.bottomFrame, image=self.bottom_image, bg='#EB5352')
        self.bottom_image_label.place(x=420,y=130)

        ###############################################################################################################################################

        ####labels and entrys:
        
        #first_name
        self.label_fn=Label(self.bottomFrame,text='Vorname:', font='arial 10 bold', fg='#29303B', bg='#EB5352')
        self.label_fn.place(x=40,y=40)
        self.entry_fn = Entry(self.bottomFrame, width=30, bd=4)
        # self.entry_fn.insert(0, 'Geben sie den Vornamen ein')
        self.entry_fn.place(x=170, y=39)

        #last_name
        self.label_ln=Label(self.bottomFrame,text='Nachname:', font='arial 10 bold', fg='#29303B', bg='#EB5352')
        self.label_ln.place(x=40,y=80)
        self.entry_ln = Entry(self.bottomFrame, width=30, bd=4)
        # self.entry_ln.insert(0, 'Geben sie den Nachnamen ein')
        self.entry_ln.place(x=170, y=79)

        #email
        self.label_email=Label(self.bottomFrame,text='Email:', font='arial 10 bold', fg='#29303B', bg='#EB5352')
        self.label_email.place(x=40,y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        # self.entry_email.insert(0, 'Geben sie die Email ein')
        self.entry_email.place(x=170, y=119)

        #phoneNumber
        self.label_phonenr=Label(self.bottomFrame,text='Telefonnummer:', font='arial 10 bold', fg='#29303B', bg='#EB5352')
        self.label_phonenr.place(x=40,y=160)
        self.entry_phonenr = Entry(self.bottomFrame, width=30, bd=4)
        # self.entry_phonenr.insert(0, 'Geben sie die Telefonnummer ein')
        self.entry_phonenr.place(x=170, y=159)

        #address##################################################################################################################
        self.label_address=Label(self.bottomFrame,text='Adresse:', font='arial 10 bold', 
                                    fg='#29303B', bg='#EB5352')
        self.label_address.place(x=40,y=300)
        self.entry_address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.entry_address.place(x=170, y=200)

        ###button
        buttonAddPerson=Button(self.bottomFrame, text='Person hinzufügen')
        buttonAddPerson.place(x=270,y=460)

        ###############################################################################################################################################