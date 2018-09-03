def del_line(lista:list,s:str):
    #imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
    #ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9 
    l_tmp = []
    for i in lista:
        if not i.count(s): l_tmp.append(i)
        else: pass;
    return l_tmp;

def formatting(s:str):
    return s.replace(' ','').split('\n')

def compare(l:list,count:int):
    tmp_str = l[0][count]
    l_bool = []
    for e in l:
        if (tmp_str==e[count]): l_bool.append(True)
        else: l_bool.append(False)
    return all(l_bool)

#komparator


TEXT = []

TEXT.append('''
example 21
text text 12
//command () 13
text again 14
''')
TEXT.append('''
example 21
text text 22
//command () 23
text again 24
''')

TEXT.append('''
example 21
text text 32
//command () 33
text again 34
''')
TEXT.append('''
example 21
text text 42
//command () 43
text again 44
''')


#formatting section
test = map(formatting,TEXT)
test = list(test)


#deleting section
for i in range(0,len(TEXT)):
    test[i] = del_line(test[i],'//command()')


compare(test,2)

helper = 0
for el in test[0]:
    if (compare(test,helper)):
        pass
    else:
        print("Line:\n",helper)
        for i in range(0,len(TEXT)):
            print(test[i][helper])
    helper+=1


print('fin')
#assert test1[helper] == test2[helper] #== test3
#raise "Good"
