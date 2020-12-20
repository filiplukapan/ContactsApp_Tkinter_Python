from tkinter import *
import datetime
import myPeople

date = datetime.datetime.now().date()

class Application(object):
    def __init__(self,master):
        self.master = master

        #Frames
        self.top=Frame(master,height=150,bg='white')
        self.top.pack(fill=X)
        ###top frame of mainwindow

        ####################################################
        self.bottom=Frame(master,height=500,bg='#8EE26B') ##hellgrün
        self.bottom.pack(fill=X)                           #
        ###bottom frame of mainwindow#######################


        ###head, image and date
        self.top_image=PhotoImage(file='icons/bookresized.png')
        self.top_image_label = Label(self.top, image= self.top_image, bg='white', width=100, height=100)
        self.top_image_label.place(x=120,y=15) ##place image

        self.heading=Label(self.top,text='Adressbuch', font='arial 15 bold', fg='#29303B', bg='white')
        self.heading.place(x=230, y=60) ##place text

        self.date_label=Label(self.top, text='Heutiges Datum: ' +str(date), font='arial 10 bold', bg='white', fg='#29303B')
        self.date_label.place(x=450,y=5)


        ###first button
        self.button1Icon=PhotoImage(file='icons/mycontacts.png')
        self.personButton = Button(self.bottom, text='Meine Kontakte', font='arial 10 bold', width=200, command=openupMyPeople)
        self.personButton.config(image=self.button1Icon, compound=LEFT)
        self.personButton.place(x=230, y=50)


        ###second button
        self.button2Icon=PhotoImage(file='icons/addcontact.png')
        self.addContactButton = Button(self.bottom, text='Kontakt hinzufügen', font='arial 10 bold', width=200)
        self.addContactButton.config(image=self.button2Icon, compound=LEFT)
        self.addContactButton.place(x=230, y=120)

        ###third    button
        self.button3Icon=PhotoImage(file='icons/aboutus.png')
        self.aboutUsButton = Button(self.bottom, text='Über uns', font='arial 10 bold', width=200)
        self.aboutUsButton.config(image=self.button3Icon, compound=LEFT)
        self.aboutUsButton.place(x=230, y=180)


def openupMyPeople():
    people=myPeople.myPeopleClass()

def main():
    root = Tk()
    app = Application(root)
    root.title("Adressbuch App")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()
    ###main window customization

if __name__ == '__main__':
    main()