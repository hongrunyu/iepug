list = ['tim',
        'guido',
        'larry']

for programer in list:
    print 'programer ' + programer

list_2 = [1,2,3,4,5]
empty_list = []
for x in list_2:
    print x**2
    empty_list.append(x**2)
    
for y in empty_list:
    print y
    
print empty_list
