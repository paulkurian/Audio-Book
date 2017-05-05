import pyttsx
from Tkinter import *
engine = pyttsx.init()

def reader(text_name,voice_var,censor,rate_var):

    #Assigning default values to the rate and voice type
    try:
        Rate_var=int(rate_var.get())
    except:
        Rate_var=0
    else:
        Rate_var=int(rate_var.get())
        
    Voice_var=voice_var.get()
    if Voice_var=='M' or Voice_var=='m':
        intvoice=0
    #the default voice type is female, because you know... Ashoka
    else:
        intvoice=1
    Text_name=text_name.get()
    
    flag=True


    #Program exits if the file cannot be found/opened
    try:
        open_text = open(Text_name, "r")
    except:
        print "Invalid File name"
        flag=False

    if flag==False:
        exit()

    Censor=censor.get()    
    

    #Accesing the default voice properties from pyttsx engine   
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+Rate_var)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[intvoice].id)
    
    open_text = open(Text_name, "r")
    lines = open_text.readlines()
    
    final_lines=''
    
    #We put the undesired words into a list "C_list"
    C_list=Censor.split()
    lis_length=len(C_list)
    for i in range (lis_length):
        C_list[i]=C_list[i].lower()
    for each_line in lines:
        for each_word in each_line.split():
            finalword=each_word.lower()

            #Removing the default next line function that is present in text editors like Notepad
            if finalword=="/n":
                finalword='' 

                
            #Now we ignore any non-ascii characters which cannot be read by the pyttsx engine
            try:
                finalword.decode('ascii')
            except UnicodeDecodeError:
                for c in finalword:
                    try:
                        c.decode('ascii')
                    except UnicodeDecodeError:
                        finalword=finalword.replace(c,"")

                        
            #Filetering out the censored words        
            for i in range (lis_length):
                if finalword.find(C_list[i])!=-1:
                    finalword=finalword.replace(C_list[i],'beeee eeee eeep')
            #Finally, we pu the edited text in "final_lines" which is what the pyttsx engine will be reading out.
            final_lines=final_lines+" "+finalword
         
            
    


    print final_lines
    #pyttsx engine reads out the edited text here
    engine.say(final_lines)
    engine.runAndWait()
    
root = Tk()

label1 = Label( root, text="Rate (-1000 to 1000, 0 for normal speed)* ")
rate_var = Entry(root, bd =5)

label2 = Label( root, text="Voice type (Enter 'M' for Male and 'F' for Female)*")
voice_var = Entry(root, bd =5)

label3 = Label( root, text="Text file name Eg:Pride_and_Prejudice.txt** ")
text_name = Entry(root, bd =5)

label4 = Label( root, text="Words to be censored: (Enter the words you want censored out and separate each with a space)")
censor = Entry(root, bd =5)

label5 = Label( root, text="*If an invalid/no input is entered the program will assign default values to these fields: \nDefault Rate=0 \nDefault voice type=Female \n**Mandatory fieid ")
submit = Button(root, text ="Submit", command = lambda: reader(text_name,voice_var,censor,rate_var))

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
