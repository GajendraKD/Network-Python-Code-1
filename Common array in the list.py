#to define the common elements in the 2 list
def common_elements (A,B):
	p1 = 0
	p2 = 0
	result = [] #an empty list to add the common elements
	while p1 < len(A) and p2 < len(B):
		if A[p1] == B[p2]:
			result.append(A[p1])
			p1 += 1
			p2 += 1
		elif A[p1] > B[p2]:
		    p2 += 1
		else:
		    p1 += 1
	return result


# NOTE: The following input values will be used for testing your solution.
A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]

list3 = common_elements (A,B)

print (list3)
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).
