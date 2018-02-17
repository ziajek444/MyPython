#List operations

#print
MyList = [1,2,3,'spam',4,5,6,'eggs']
print(MyList)
#assignement
TempList = MyList
print(TempList)
#Addition and multiply
TempList = MyList * 2
print(TempList)
TempList = MyList + [444]
print(TempList)
#Addition is also .append() but .remove() is substraction specify object
TempList.remove(444) #List without '444'
print(TempList)
#oposite of remove is insert
TempList.insert(len(TempList),'snake')
print(TempList)
#'in' operator and 'not'
var = (444 in TempList)
print(var)#True
var = (not 444 in TempList)
print(var)#False
var = ('python' in TempList)
print(var)#False
var = (not 'python' in TempList)
print(var)#True
#Another function:
#max()
print max(TempList)
#min()
print min(TempList)
#Another methods:
#   .append()
print TempList.append('snake')#nothing to return (void)
#   .count()
print TempList.count('snake')#2 already
#   .reverse()
TempList.reverse()
print TempList

del MyList,TempList
print '\t\n\t@Marcin Ziajkowski'

