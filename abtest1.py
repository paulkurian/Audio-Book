import pyttsx
from Tkinter import *
engine = pyttsx.init()

def audiobook(text_name,rate_var,voice_var,censor):
    
    Rate_var=int(rate_var.get())
    
    Voice_var=voice_var.get()
    Text_name=text_name.get()
    
    Censor=censor.get()
    

        
    
    
    if Voice_var=='M' or 'm':
        intvoice=0
    elif Voice_var=='F' or 'f':
        intvoice=1
    else:
        print "Invalid Voice type entered"
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+Rate_var)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[intvoice].id)
    open_text = open(Text_name, "r")
    lines = open_text.readlines()
    lines1=''
    
    lis=Censor.split()
    l=len(lis)
    for i in range (l):
        lis[i]=lis[i].lower()
    for line in lines:
        for word1 in line.split():
            word=word1.lower()
            if word=="/n":
                word=''
            
            try:
                word.decode('ascii')
            except UnicodeDecodeError:
                for c in word:
                    try:
                        c.decode('ascii')
                    except UnicodeDecodeError:
                        word=word.replace(c,"")
                    
            for i in range (l):
                if word.find(lis[i])!=-1:
                    word=word.replace(lis[i],'beeee eeee eeep')
            
            lines1=lines1+" "+word
         
            
    


    print lines1
    engine.say(lines1)
    engine.runAndWait()
    
root = Tk()

label1 = Label( root, text="Rate (-100 to 100, 0 for normal speed) **")
rate_var = Entry(root, bd =5)

label2 = Label( root, text="Voice type (Enter 'M' for Male and 'F' for Female)")
voice_var = Entry(root, bd =5)

label3 = Label( root, text="Text file name Eg:Pride_and_Prejudice.txt **")
text_name = Entry(root, bd =5)

label4 = Label( root, text="Words to be censored: (Enter the words you want censored out and separate each with a space)")
censor = Entry(root, bd =5)

label5 = Label( root, text="** Mandatory fields")
submit = Button(root, text ="Submit", command = lambda: audiobook(text_name,rate_var,voice_var,censor))

label1.pack()
rate_var.pack()
label2.pack()
voice_var.pack()
label3.pack()
text_name.pack()
label4.pack()
censor.pack()
label5.pack()
submit.pack(side =BOTTOM) 
root.mainloop()
