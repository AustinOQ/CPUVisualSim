#compiles asm to machine language.
def cmpl(fileName):
    file=open(fileName,'r')
    asm=file.readlines()
    for i in range(len(asm)):
        asm[i]=[i, asm[i].replace("\n",'').split(" ")]
    file.close()
    return(asm)


