# imports
import numpy as np
import tkinter
from tkinter import *

# variables
relative = np.array([[3, 1, 3], [3, 3, 3], [2, 3, 3], [2, 0, 0], [2, 2, 3], [2, 0, 3], [2, 3, 3], [2, 3, 2], [1, 0, 2], [0, 3, 0], [3, 0, 0]])
response = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
count = 0
res = []
diagnosis = ""
questions = ["Do you cough? ",
"Does your throat sore? ",
"Is your breath short? ",
"Have you experienced fatigue? ",
"Do you experience pain on your body? ",
"Do you have a headache? ",
"Do you have runny or stuffy nose? ",
"Do you have diarrhea? ",
"Do you sneeze? ",
"Have you lost the ability to taste or smell? ",
"", ""]


#Creating GUI with tkinter
def send():
    global count
    global res
    global diagnosis
    msg = EntryBox.get("1.0",'end-1c').strip().lower()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "\nYou: " + msg + '\n')
        ChatLog.insert(END, "\n" + questions[count])
        if msg == 'yes' or msg == "y" or msg == 'yup':
            response[count,:] = 1
        else:
            response[count,:] = 0
        count += 1
        if count == 11:
            mult = relative*response
            total = [sum(mult[:,0]), sum(mult[:,1]), sum(mult[:,2])]
            result = total.index(max(total))

            if result == 0:
                diagnosis = 'COVID-19'
            elif result == 1:
                diagnosis = 'a COLD'
            elif result == 2:
                diagnosis = 'the FLU'

            if sum(total) == 0:
                ChatLog.insert(END, "It seems that you don't have any respiratory disease")
            else:
                ChatLog.insert(END, "Based on your symptoms it is more possible that you have " + diagnosis + "\n")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("CoBot-19")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(foreground="#442265", font=("Verdana", 11 ))
ChatLog.insert(END, "Hello. I am CoBot-19 and I will help you know if you have COVID-19 or not. Please answer to the following questions with yes or no.\nDo you have fever? \n")

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
