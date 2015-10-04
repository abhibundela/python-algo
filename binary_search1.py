# binary search using concept of recursion
def binary_search(data,target): #data is list of items
	low = 0
	high = len(data)-1
	mid = (low+high)/2
	try:
		if data[mid]==target:
			return True
		elif data[mid]>target:
			data = data[:mid]
			return binary_search(data,target)
		else:
			data = data[mid+1:]
			return binary_search(data,target)
	except IndexError:
		return False



