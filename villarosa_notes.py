# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
class Note_Keeping_App:

    def __init__(self, date, title, description, status):
        self.date = date
        self.title = title
        self.description = description
        self.status = status

    #add function
    def add(self, date, title, description):
        status = "Active"
        ob = Note_Keeping_App(date, title, description, status)
        note.append(ob)
    #edit function
    def edit(self, note):
        if(len(note)==0):
            return print ("No note found!")
        elif (len(note)>0):
            ctr = 0
            note_num = int(input("\nEnter note number: "))

            if (note_num < 0):
                print ("Invalid note number!")
                return
            for ctr in range(len(note)):
                print ("Edit which part?"
                       "\n[a] Date"
                       "\n[b] Title"
                       "\n[c] Description"
                       "\n[d] Status")
                print ("Input choice: ")
                ch = input()

                if ch == 'a' or ch == 'A':
                    print ("Enter new date: ")
                    new_date = input()
                    note[ctr].date = new_date

                elif ch == 'b' or ch == 'B':
                    print ("Enter new Title: ")
                    new_title = input()
                    note[ctr].title = new_title

                elif ch == 'c' or ch == 'C':
                    print("Enter new Description: ")
                    new_description = input()
                    note[ctr].description = new_description

                elif ch == 'd' or ch == 'D':
                    print("Changing status from 'Active' to 'Draft' ")
                    note[ctr].status = 'Draft'
    #view function
    def view(self, note):
        if (len(note) == 0):
            return print("\nThe note list is empty!")
        elif(len(note) > 0):
            ctr = 0
            for ctr in range (len(note)):
                if (note[ctr].status == "Active"):
                    print("\nNote #: ", ctr)
                    print("Title: ", note[ctr].title)
                    print("Description: ", note[ctr].description)
                    print("Status: ", note[ctr].status)
note = []
obj = Note_Keeping_App(' ', ' ', ' ', ' ')
#main function
if __name__ == '__main__':


    print ("Note Keeping App")
    print ("Proponent: Jasper Villarosa")

    while (True):
        print("This is the MENU:"
              "\n[A] Add"
              "\n[E] Edit"
              "\n[V] View"
              "\n[X] Exit")

        print("Enter your choice: ")
        ch = input()

        if ch=='A' or ch == 'a':
            print("Enter today's date: ")
            date = input()

            print("Enter Title: ")
            title = input ()

            print("Enter Description: ")
            description = input()

            obj.add(date,title,description)

        elif ch=='E' or ch == 'e':
            obj.edit(note)

        elif ch=='V' or ch == 'v':
            obj.view(note)

        elif ch=='X' or ch == 'x':
            exit()

        os.system("pause")
        os.system('cls')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
