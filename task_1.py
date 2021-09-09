b_true=True
b_false=False
a='Alc'
b='Bic'
c= 1
d=2
e=3
f=4
g=4.1
i=5.5
h=6.3

result= d!=3
print(result)
result= e==1
print(result)
result= d!=3
print(result)
result= f!=3
print(result, type(result))
result= g>=3
print(result)

result= g==3.5
print(result)
result= g!=3.5
print(result)
result= g>h
print(result)
result= g<=2
print(result, type(result))
result= g!=300
print(result)
result= g!=3.5
print(result)

result= d!=3 and g!=5
print('3-', result)
result= d==3 and g==5
print('3-', result)
result= d>=3 or g!=10
print('3-', result)
result= d<=3 or g==10
print('3-', result)
result= not e!=5
print('3-', result)
result= not d==3 and g==5
print('3-', result)

a= int(input())
if a> 30:
    print('вы ввели число =', a, 'которое больше 30')
elif a< 30:
    print('вы ввели число =', a, 'которое меньше 30')
else:
    print('вы ввели число =', a, 'которое равно 30')


import random
b= random.randint(1, 100)
a= int(input())

if a > b:
        print('вы ввели число =', a, 'которое больше', b)
elif a< b:
    print('вы ввели число =', a, 'которое меньше', b)
else:
    print('вы ввели число =', a, 'которое равно', b)

import random
c= random.randint(1, 100)
b= random.randint(1, 100)
a= int(input())

if a > b:
        if a >c:
                print('вы ввели число =', a, ', которое больше', b, 'и больше', c)
        elif a <c:
                print('вы ввели число =', a, ', которое больше', b, 'и меньше', c)
        else:
                print('вы ввели число =', a, ', которое больше', b, 'и равно', с)
if a < b:
        if a >c:
                print('вы ввели число =', a, ', которое меньше', b, 'и больше', c)
        elif a <с:
                print('вы ввели число =', a, ', которое меньше', b, 'и меньше', c)
        else:
                print('вы ввели число =', a, ', которое меньше', b, 'и равно', с)

if a == b:
        if a >c:
                print('вы ввели число =', a, ', которое равно', b, 'и больше', c)
        elif a <c:
                print('вы ввели число =', a, ', которое равно', b, 'и меньше', c)
        else:
                print('вы ввели число =', a, ', которое равно', b, 'и равно', с)










