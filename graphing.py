from tkinter import *
import tkinter as ttk
import time


   
def Format(arr):
    for i in range(len(arr)):
        arr[i]=arr[i].replace("\n","")
        arr[i]=arr[i].split(",")
    return arr



#Initialize graphics window.
master = Tk()
w = Canvas(master, width=2000, height=1200)
w.pack()
clock=0
clockTextUpdate=w.create_text(950,970,text=str(clock), font=("times",20))
    #Open and load memory and state files.
memory=open("memDump.txt",'r').readlines()
state=open("results.txt",'r').readlines()

    #Format lines form files:
memory=Format(memory)
state=Format(state)

    #make mem and state textboxes
pcTextUpdate=w.create_text(950,870,text='', font=("times",20))
memArr=[w.create_text(0,0,text='')]*len(memory[0])
fetchTextUpdate=w.create_text(0,0,text='')
decodeTextUpdate=w.create_text(0,0,text='')
executeTextUpdate=w.create_text(0,0,text='')
memTextUpdate=w.create_text(0,0,text='')
r0TextUpdate=w.create_text(0,0,text='')
r1TextUpdate=w.create_text(0,0,text='')
r2TextUpdate=w.create_text(0,0,text='')
r3TextUpdate=w.create_text(0,0,text='')
r4TextUpdate=w.create_text(0,0,text='')
r5TextUpdate=w.create_text(0,0,text='')
r6TextUpdate=w.create_text(0,0,text='')


def update():
    #globals to update
    global pcTextUpdate
    global clock
    global clockTextUpdate
    global memArr
    global memory
    global state
    global fetchTextUpdate
    global decodeTextUpdate
    global executeTextUpdate
    global memTextUpdate
    global r0TextUpdate
    global r1TextUpdate
    global r2TextUpdate
    global r3TextUpdate
    global r4TextUpdate
    global r5TextUpdate
    global r6TextUpdate
    
    #update memory
    w.delete(clockTextUpdate)
    clockTextUpdate=w.create_text(950,970,text=str(clock), font=("times",20))
    MinY=110
    for i in range(len(memArr)):
        w.delete(memArr[i])
        memArr[i]=w.create_text(200,MinY+i*20,text=memory[clock][i])
    

    #update state
    w.delete(fetchTextUpdate)
    fetchTextUpdate=w.create_text(750,240,text=state[clock][2], font=("times",30))

    w.delete(decodeTextUpdate)
    decodeTextUpdate=w.create_text(1150,240,text=state[clock][5], font=("times",30))

    w.delete(executeTextUpdate)
    executeTextUpdate=w.create_text(1150,640,text=state[clock][8], font=("times",30))

    w.delete(memTextUpdate)
    memTextUpdate=w.create_text(750,640,text=state[clock][11], font=("times",30))

    w.delete(r0TextUpdate)
    r0TextUpdate=w.create_text(1800,150,text=state[clock][13], font=("times",20))
    
    w.delete(r1TextUpdate)
    r1TextUpdate=w.create_text(1800,250,text=state[clock][14], font=("times",20))

    w.delete(r2TextUpdate)
    r2TextUpdate=w.create_text(1800,350,text=state[clock][15], font=("times",20))

    w.delete(r3TextUpdate)
    r3TextUpdate=w.create_text(1800,450,text=state[clock][16], font=("times",20))

    w.delete(r4TextUpdate)
    r4TextUpdate=w.create_text(1800,550,text=state[clock][17], font=("times",20))

    w.delete(r5TextUpdate)
    r5TextUpdate=w.create_text(1800,650,text=state[clock][18], font=("times",20))

    w.delete(r6TextUpdate)
    r6TextUpdate=w.create_text(1800,750,text=state[clock][19], font=("times",20))

    w.delete(pcTextUpdate)
    pcTextUpdate=w.create_text(950,870,text=state[clock][3], font=("times",20))

    
    clock+=1




    if clock>len(memory)-1:
        start["state"]="disabled"
    
    

    




    ##Draw Memory Cells
j=0
for i in range(100,1000,20):
    w.create_rectangle(10,i,100,i+100,fill="white",outline="black")
    w.create_text(50,i+10,text=str(j))
    j+=1
for i in range(100,1000,20):
    w.create_rectangle(100,i,300,i+100,fill="white",outline="black")

    ###Draw Fetch Unit
fu=w.create_rectangle(600,100,900,400,fill="white",outline="black")
fuText=w.create_text(750,200,text="Fetch", font=("times",30))

    ###Draw Control Unit
cu=w.create_rectangle(1000,100,1300,400,fill="white",outline="black")
cuText=w.create_text(1150,200,text="Decode", font=("times",30))
        
    ###Draw ALU
alu=w.create_rectangle(1000,500,1300,800,fill="white",outline="black")
aluText=w.create_text(1150,600,text="Execute", font=("times",30))

    ###Draw MemAccess Unit
mau=w.create_rectangle(600,500,900,800,fill="white",outline="black")
mauText=w.create_text(750,600,text="Memory Access", font=("times",30))

    ###Draw Clock
clk=w.create_rectangle(900, 910, 1000, 1010,fill="white",outline="black")
clckText=w.create_text(950,930,text="Clock", font=("times",20))

    ###Draw PC
pc=w.create_rectangle(900, 810, 1000, 910,fill="white",outline="black")
pcText=w.create_text(950,830,text="PC", font=("times",20))
        
    ###Draw register file
w.create_rectangle(1700,100,1900,200,fill="white",outline="black")
w.create_text(1800,120,text="r0", font=("times",20))
w.create_rectangle(1700,200,1900,300,fill="white",outline="black")
w.create_text(1800,220,text="r1", font=("times",20))
w.create_rectangle(1700,300,1900,400,fill="white",outline="black")
w.create_text(1800,320,text="r2", font=("times",20))
w.create_rectangle(1700,400,1900,500,fill="white",outline="black")
w.create_text(1800,420,text="r3", font=("times",20))
w.create_rectangle(1700,500,1900,600,fill="white",outline="black")
w.create_text(1800,520,text="r4", font=("times",20))
w.create_rectangle(1700,600,1900,700,fill="white",outline="black")
w.create_text(1800,620,text="r5", font=("times",20))
w.create_rectangle(1700,700,1900,800,fill="white",outline="black")
delMe=w.create_text(1800,720,text="r6", font=("times",20))
   
    ###Make button
start= Button(w, text= "Clock+=1", command= update)
start.place(x=920,y=1020)

    ###Draw arrows
w.create_line(900,250,1000,250)
w.create_line(990,260,1000,250)
w.create_line(990,240,1000,250)

w.create_line(1150,400,1150,500)
w.create_line(1160,490,1150,500)
w.create_line(1140,490,1150,500)

w.create_line(1000,650,900,650)
w.create_line(900,650,910,640)
w.create_line(900,650,910,660)


master.mainloop()


            
