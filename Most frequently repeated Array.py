# Most frequently repeated number in Arrey

def most_frequent(given_list):
    max_count = -1 # number of times this number was acquire in the list.
    max_item = None # Item from the list
    count = {}  # dictionary with the number and count it appears
    for i in given_list:
        if i not in count: # item from the list is not added in dic.
            count[i] = 1  # add 1 count for the item with respective #
        else:
            count[i] += 1 # if item appear multiple time add 1 by in count
        if count[i] > max_count: # count mostly appear item
            max_count = count[i]  # Max time os repeatition
            max_item = i # most of the time appeared number
    return max_count

list1 = [1, 3, 1, 3, 2, 1,3]
print (list1)

list2 = most_frequent(list1)

print (list2)


# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1.
#list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3.
#list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None.
#list3 = []
# most_frequent(list4) should return 0.
#list4 = [0]
# most_frequent(list5) should return -1.
#list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
