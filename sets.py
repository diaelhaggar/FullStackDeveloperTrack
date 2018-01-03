groceries = {'milk','cheese','bread','spices','shampoo','bread'}
groceries.add('Tomato')
groceries.remove('milk')
groceries.clear()
groceries.add('Tomato')
print (groceries) # prints only bread once. sets can not contain dupicates
item=input('Checking item: ')

if item in groceries:
    print ('You already have '+item)
else:
    print('You need to have '+item)