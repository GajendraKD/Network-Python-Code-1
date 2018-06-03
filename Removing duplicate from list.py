# removing the dupplicate from list
# let'e define a function that will return new list with no duplicate elements
def removeDup1(inputList):
    # we need an empty list before the loop
    secondList = []
    for element in inputList:
        if element not in secondList:
            secondList.append(element)  # so if there is no such element - add it to the list

    return secondList


# let's check
myL = ['hello', 'youtube', 'hello', 'youtube']
print(myL)

myL = removeDup1(myL)
print(myL)
