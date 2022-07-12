

def cat(someList):
    someList = []
    while True:
        print('Enter list values: (enter nothing to stop).')
        name = input()
        if name == '':
            break
        someList.append(name)
    someList.insert(-1, 'and')
    print(someList)


spam = []
cat(spam)