def listIt(listValue):
    lastItem = listValue[len(listValue) - 1]
    listValue.remove(listValue[len(listValue) - 1])
    for item in listValue:
        print(item + ', ', end='')
    print('and ' + lastItem)
    listValue.append(lastItem)


listValue = ['milk', 'bacon', 'eggs', 'cereal', 'butter']
secondList = ['one', 'two', 'three', 'four', 'five']


listIt(listValue)
listIt(secondList)