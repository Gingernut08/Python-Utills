##  cd my drive/a-levels/cs/python utills

import time

def calculate_min_run(arrayLength):
	r = 0
	while arrayLength >= 32:
		r |= arrayLength & 1
		arrayLength >>= 1

	return arrayLength + r

def insertion_sort(array, left, right):
	for i in range(left + 1, right + 1):
		j = i
		while j > left and array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
			j -= 1

def merge(array, left, mid, right):
	len1, len2 = mid - left + 1, right - mid
	leftLis, rightLis = [], []
	for i in range(0, len1):
		leftLis.append(array[left + i])

	for i in range(0, len2):
		rightLis.append(array[mid + 1 + i])

	i, j, k = 0, 0, left
	while i < len1 and j < len2:
		if leftLis[i] <= rightLis[j]:
			array[k] = leftLis[i]
			i += 1

		else:
			array[k] = rightLis[j]
			j += 1

		k += 1

	while i < len1:
		array[k] = leftLis[i]
		k += 1
		i += 1

	while j < len2:
		array[k] = rightLis[j]
		k += 1
		j += 1

def tim_sort(array):
	arrayLength = len(array)
	minRun = calculate_min_run(arrayLength)
	for start in range(0, arrayLength, minRun):
		end = min(start + minRun - 1, arrayLength - 1)
		insertion_sort(array, start, end)

	size = minRun
	while size < arrayLength:
		for left in range(0, arrayLength, 2 * size):
			mid = min(arrayLength - 1, left + size - 1)
			right = min((left + 2 * size - 1), (arrayLength - 1))
			if mid < right:
				merge(array, left, mid, right)

		size = 2 * size

	return array



