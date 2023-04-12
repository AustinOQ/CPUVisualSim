'''Convert File.simpleAsm to memory representation.
    Legal instructions-->
        add  intReg1 intReg2 destinationReg
        mult intReg1 intReg2 destinationReg
        and  intReg1 intReg2 destinationReg
        not  intReg1 intReg2 destinationReg
        saver sourceReg destinationMemAddress
        loadr sourceMemAddress destinationReg
        savel literal destinationMemAddress
        branch condition newPC
        out register
'''

from cmpl import *

#branch predictor says allways taken.
#no reordering.
#no dependency handling. Leave that to the programer.
#programs start at address 0 
#jump to end of memory or address 9999 to quit. 
#fetch, decode, execute, save all use unique components. 
#all instructions take 4 cycle.
#branch resolved in store phase
#cpu is pipelined and forwarded.
def processing():
    clock=0
    pc=0 #points to next instruction to start.
    r0,r1,r2,r3,r4,r5,r6=0,0,0,0,0,0,0

    statequeue=[]#used to flash back to last known legal state. 

    

   
    file=input("Enter assembly file name:")
    #mem=[[address, [instruction], flag array]...]. flag=1 when execution is speculative.
    mem=cmpl(file)
    
    fetch,decode,execute=None,None,None
    fetchTemp,decodeTemp,executeTemp,storeTemp=None,None,None,None

    #START MAIN EVENT LOOP
    while(pc!=len(mem)+3 and pc!=9999):

        #fetch unit
        if(pc<len(mem)):
            print("fetch", mem[pc][1], "from memory location",pc,'.','At time:',clock)
            fetchTemp=mem[pc]
            

        #decode unit
        if(fetch!=None and pc<len(mem)+1):
            print("decode",fetch[1], "from memory location",fetch[0],'.','At time:',clock)
            decodeTemp=fetch
            #if this is a data access, cache the data.
            #if this is a branch, save all running data in case mispredict. 
                #running data is registers

        #execute unit
        if(decode!=None and pc<len(mem)+2):
            print("execute",decode[1], "from memory location",decode[0],'.','At time:',clock)
            executeTemp=decode
            #this is where out command is executed.

        #store unit
        if(execute!=None):
            print("store",execute[1], "from memory location",execute[0],'.','At time:',clock)
            storeTemp=execute
            #if branch fails,
                #delete all temp files, clear components, set pc to branch specified
                #reload registers with saved data. 
        
        #clock ticks and everything moves forward in exe cycle.
        pc+=1
        clock+=1
        fetch=fetchTemp
        decode=decodeTemp
        execute=executeTemp
        print('r0=',r0,', r1=',r1,', ,r2=',r2,', r3=',r3,', r4=',r4,', r5=',r5,', r6=',r6)
        

        
     
processing()