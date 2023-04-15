from tkinter import *

#def vis(memFile, stateFile):
def vis():
    
    master = Tk()
    w = Canvas(master, width=2000, height=1200)
    w.pack()

    ######
    ######The following code will only be run once. Draws all base shapes.
    ######

    ##Draw memory cells
    j=0
    for i in range(100,1000,20):
        w.create_rectangle(0,i,100,i+100,fill="white",outline="black")
        w.create_text(50,i+10,text=str(j))
        j+=1
    for i in range(100,1000,20):
        w.create_rectangle(100,i,300,i+100,fill="white",outline="black")


    ###Draw fetch unit
        fu=w.create_rectangle(600,100,900,400,fill="white",outline="black")

    ###Draw Control Unit
                 cu=w.create_rectangle(1000,100,1300,400,fill="white",outline="black")

    ###Draw ALU
        alu=w.create_rectangle(1000,500,1300,800,fill="white",outline="black")

    ###Draw MemAccess Unit
        mau=w.create_rectangle(600,500,900,800,fill="white",outline="black")

    ###Draw register file
        w.create_rectangle(1700,100,1900,200,fill="white",outline="black")
        w.create_rectangle(1700,200,1900,300,fill="white",outline="black")
        w.create_rectangle(1700,300,1900,400,fill="white",outline="black")
        w.create_rectangle(1700,400,1900,500,fill="white",outline="black")
        w.create_rectangle(1700,500,1900,600,fill="white",outline="black")
        w.create_rectangle(1700,600,1900,700,fill="white",outline="black")
        




    
    ###
    ###Now starts the clock cycle loop
    ###
        text=[0]*50#make a bunch of textboxes. Fill with actual mem content.
                #text[i] willbe cell names.
        #make a bunh of text in regfiles

        #make a bunch of text in units
        
        for i in range(len(mem)):
            #delete mem
            for...
            #redraw whith new vale
            for ...

            ##delete and refill reg

            ##delete and refil units
            

            input()#wait for unser input to progress
    

vis()
