import pyttsx
from Tkinter import *
engine = pyttsx.init()

def audiobook(E1,E2,E3,E4):
    rate = engine.getProperty('rate')
    e1=int(E1.get())
    e2=int(E2.get())
    e3=E3.get()
    e4=E4.get()
    
    engine.setProperty('rate', rate+e1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[e2].id)
    text_file = open(e3, "r")
    lines = text_file.readlines()
    lines1=''
    lis=e4.split()
    l=len(lis)
    for i in range (l):
        lis[i]=lis[i].lower()
    for line in lines:
        for word1 in line.split():
            word=word1.lower()
            if word.find("/n")!=-1:
                word=word.replace("/n",'')
            for i in range (l):
                if word.find(lis[i])!=-1:
                    word=word.replace(lis[i],'beeee eeee eeep')
            
            lines1=lines1+" "+word
    



    engine.say(lines1)
    engine.runAndWait()
    
root = Tk()

label1 = Label( root, text="Rate")
E1 = Entry(root, bd =5)

label2 = Label( root, text="Voice type")
E2 = Entry(root, bd =5)

label3 = Label( root, text="Text file name")
E3 = Entry(root, bd =5)

label4 = Label( root, text="Words to be censored")
E4 = Entry(root, bd =5)

submit = Button(root, text ="Submit", command = lambda: audiobook(E1,E2,E3,E4))

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
submit.pack(side =BOTTOM) 
root.mainloop()
