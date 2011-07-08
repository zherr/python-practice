# This program shows how to sort through a dictionary

D = {'a': 1, 'b': 2, 'c': 3}

Ks = list(D.keys()) #to retrieve a list of the keys

for key in Ks:
    print(key, '=> ', D[key]) #long way

for key in sorted(D):
    print(key, '=> ', D[key]) #short way
    
for c in 'spam':
    print(c.upper()) # 'for each character in 'spam', print char in upper case'

i = 0
while(i<6):
    print('spam' * i)
    i += 1      #this shows the basics of a while loop

squares = []
for x in [1,2,3,4,5]:
    squares.append(x ** 2) #shows both iterations of x and appending
print(squares)

if not 'f' in D:         #test to avoid error messages
    print('missing')

print(D['f']) #error for something not there
