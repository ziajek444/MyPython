#Loops
#There is while and for
#infinite loop: while True

print("while var + counter")
var = 10
while var:
    print(var)
    var-=1
print("end loop")

print("while+range(var)")
var=10
while range(var):
    print(var)
    var-=1
print("end loop")

print("for+range(10)")
var=10
for i in range(10):
    print(var)
    var-=1
print("end loop")

print("List loop")
MyList = [1,2,3,4,5,6,7,8,9,10]
for i in MyList:
    MyList.reverse()#working at not copy !!
    print(i)
print("end loop")
print '\t\n\t@Marcin Ziajkowski'
