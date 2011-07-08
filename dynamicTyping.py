L1 = [2, 3, 4]  # mutable object
L2 = L1         # makes a reference to the same object
L1[0] = 24      # an in-place change

print(L1)       # L2 is obviously different
print(L2)       # so is L2! This is because we changed a component of that object
                # It overwrites the object referenced
L1 = [2, 3,4]
L2 = L1[:]      # copies L1
L1[0] = 24

print(L1)
print(L2)       # L2 is not changed

'''Shared References and Equality'''
L = [1, 2, 3]
M = L
if L == M: print('True') # same value
if L is M: print('True') # same object
M = [1, 2, 3]
if L == M: print('True')
if not (L is M): print('False') # because they are referencing different objects

X = 42
Y = 42
if X == Y: print('True') 
if X is Y: print('True') # Python reuses small integers and strings
