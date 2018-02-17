#some kind of Iboolean's use

#To Bollean var u can to assign 2 values True (Logical 1) and False (Logical 0)

MyBool = True
#keyword 'not' inverted logic, not True = False and not False = True
print('bool var content: %s' % MyBool + ' and oposite is: %s' % (not MyBool))
#We can convert any content to almost every type
print(str(MyBool))
print(int(MyBool))

print('True as an integer + False as integer - 1 is equal: %d '%(int(MyBool)+int(not MyBool)-1)+'"1+0-1=0"')

# statements 'or' and 'and' are returns True or False as well
print('2==2 or 2==1 is: %s '%(2==2 or 2==1))
del MyBool #clean dle MyBool alias's reference
MyBool = (2==2 and 2==1)
print('2==2 and 2==1 is: %s '%MyBool)

# '==' has a higher precedence than or:

print(False == False or True) #True
print(False == (False or True)) #False
print((False == False) or True) #True

print('\nFrom higets precendance to lowest:\n')
ListOfOperators = ['**','~ + -','* / % //','+ -','>> <<','&','^ |','<= < > >=']
ListOfOperators+= ['<> == !=','= %= /= -= +=\n*= **=','is is not','in not in']
ListOfOperators+= ['not or and']
Description = ['Exponential (raise to the power)','Complement, unary plus and minus']
Description[1] += "\n(method names for the last two are +@ and -@)"
Description+= ['Multiply,divide,modulo and floor division','Addition and substraction']
Description+= ['Right and left bitwise shift',"Bitwise 'AND'","Bitwise exclusive"]
Description[6] += " 'OR' and regular 'OR'"
Description+= ['Comparison operators','Equality operators','Assignement operators']
Description+= ['Identity operators','Membership operators','Logical operators']
counter=0;
if len(ListOfOperators) == len(Description):
    for i in ListOfOperators:
        print('----------------\n%s'%i+"\t\t%s"%Description[counter])
        counter+=1;
    print("----------------")#16
else:
    print("Not Equal, Wrong length")

del MyBool,ListOfOperators,Description,counter

print '\t\n\t@Marcin Ziajkowski'
