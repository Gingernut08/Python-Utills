##  cd my drive/a-levels/cs/cs nea

def linear_search(array, item):
	for i in range(len(array)):
		if item == array[i]:
			return i

	return False

def binary_search(array, item):
	left = 0
	right = len(array) - 1
	while left <= right :
		mid = (left + right) // 2

		if array[mid] == item:
			return mid

		elif array[mid] < item:
			left = mid + 1

		elif array[mid] > item:
			right = mid - 1

	return False