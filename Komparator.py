#komparator

T1 = '''Text 1
'''
T2 = '''Text 2
'''
#T3 = '''Text 3
#'''

test1 = T1[:].replace(' ','').split('\n')
test2 = T2[:].replace(' ','').split('\n')
#test3 = T3[:].replace(' ','').split('\n')
helper = 0
for el in test1:
    if (el == test2[helper]): # el == test2[helper] == test3[helper]
        pass
    else:
        print("Line:\n",helper)
        print(test1[helper])
        print(test2[helper])
        #print(test2[helper])
    helper+=1

print('fin')
#assert test1[helper] == test2[helper] #== test3
#raise "Good"
