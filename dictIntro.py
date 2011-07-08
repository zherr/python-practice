# This shows the basics of dictionaries

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print(D)

print('The value of "food": ',D['food']) #uses a key to retrieve a value
D['quantity'] += 1 #adds one to the quantity value
print(D)

D = {} #re-define 'D'
D['name'] = 'Bob' #shows how dictionaries are mutable
print(D)

