catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) +
          ' (or enter nothing to stop it.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concat
print('The cat names are: ')
for name in catNames:
    print(' ' + name)
    
    
    """
    if I want to print items in a list, i can use:
        for i in range(len(listName)):
    """