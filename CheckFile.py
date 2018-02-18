#check files
path = "D:/Dysk Google ziajkowski.marcin@gmail.com/GITREPOZYTORY/MyPython/blabla.txt"
with open(path,'r') as F:
    RL=F.read()
    print len( RL)
    print RL
RL = list(RL)
print RL

tempStr=""
for element in RL:
    var = ord(element)
    for i in range(10-len(bin(var))):
        tempStr+='0'
        
    #print('RL___: %s%s %c' %(tempStr, bin(var), element))
    tempStr=""
    var = var ^ 128
    #print('after: %s%c' %(bin(var),chr(var)))
print RL
F.close()
path = "D:/Dysk Google ziajkowski.marcin@gmail.com/GITREPOZYTORY/MyPython/blabla.hero"
with open(path,'w') as N:
    N.write(str(RL))
N.close()
