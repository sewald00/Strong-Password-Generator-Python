# Random password Generator
# Seth Ewald
# March 6th 2018

import tkinter as tk
from tkinter import ttk
from random import randint


# Define the main program function to run
def main():
    # Define function to change label text on button click
    def onClick():
        password = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz1234567890!@#$%&*?')

        # Assign the first letter to the PW to make sure it is a letter
        randomPW = []
        x = randint(0, 51)
        randomPW.append(password[x])

        #If/else statement to determine state of allow special characters checkbox
        if checkVar1.get()==1:
        # assign specified number
            for i in range(19):
                x = randint(0, 69)
                randomPW.append(password[x])
            finalPW = (''.join(randomPW))
            e.delete(0, 20)
            e.insert(0, finalPW)
        else:
            for i in range(19):
                x = randint(0, 61)
                randomPW.append(password[x])

            finalPW = (''.join(randomPW))
            e.delete(0, 20)
            e.insert(0, finalPW)

    # Create app window

    root = tk.Tk()
    root.minsize(width=300, height=75)
    root.maxsize(width=300, height=75)
    root.title("Password Generator")

    # Create button to generate a random password
    button = tk.Button(root, text='Generate Password',
                       width=25, command=onClick)
    button.pack()

    # Create a label to display the random password
    e = tk.Entry(root, width=30)
    e.pack()

    #create check button
    checkVar1=tk.IntVar()
    C1 = tk.Checkbutton(root, text="Allow Special Characters", variable=checkVar1,
                        onvalue=1, offvalue=0, height=5,width=20,command=print(checkVar1.get()))
    C1.pack()

    root.mainloop()


main()



