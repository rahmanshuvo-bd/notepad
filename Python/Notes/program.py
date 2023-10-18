def newtext(text):
    
    #Open file and add new text and close

    addText=open('Files/Memories.txt','a')

    addText.write(text)
    addText.write('\n')

    addText.close()
    return

def viewtext():

    #Open file and read it

    readText=open('Files/Memories.txt')
    
    print('Notepad Opening: \n')
    print(readText.read())
    readText.close()
    return

def takeText(textValue):
    
    #Take note input
    note=input('Enter your text: ')

    return note

#Clear notepads
def clearnotes():

    print('Notes cleared successfully! \n')

    addText=open('Files/Memories.txt','w')

    addText.write('\"Welcome to Python notepad\" \n')

    addText.close()
    return

#Add time on the note

import time

def localtime():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("Last edited %m/%d/%Y, %H:%M:%S", named_tuple)

    addText=open('Files/Memories.txt','a')

    addText.write(time_string)
    addText.write('\n')

    addText.close()

    return

#add separation
def addsep():

    addText=open('Files/Memories.txt','a')

    addText.write('\n')


    addText.close()
    return

#Display options startup

def startup():

    print('\"NotePad\"\n')

    print('Write the value')

    print('w for Add new text')

    print('r for read text file')

    print('q for quite the program')

    print('c for clear notes')




def shortmsg():
    print('Thanks for using Notepad')
    print('Choose Operation: w r q c \n')

#take options

def options(opt):
    
    option=input('Enter your choice: ')
    return option

#Quit application
def quitapp():
    print('Thanks! Comeback again!')
    return

#Take operation and compare

  
#StartUp Display

option='0'
startup()


while True:

    option=options(option)

    if option == 'w' :


        text='0'
        text=takeText(text)
        newtext(text)
        addsep()
        localtime()
        addsep()
    
        print('\n')
        shortmsg()
        continue

    elif option == 'r' :

        viewtext()
        shortmsg()
        continue 
        

    elif option == 'q' :

        quitapp()
        break
    
    elif option == 'c' :

        clearnotes()
        shortmsg()
        continue
