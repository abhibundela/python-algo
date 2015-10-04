#binary search 

def binary_search(data,target,low,high): #data is list of items
	if low>high:
		return False
	else:
		mid = (low+high)//2
	if target == data[mid]:
		return True
	elif target<data[mid]:
		return binary_search(data,target,low,mid-1)
	else:
		return binary_search(data,target,mid+1,high)
# algorithm analysis
# worst case performance O(log n)
# best case performance O(1)
# average case performance O(log n)
# worst case space complexity O(1)
