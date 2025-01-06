##  cd my drive/a-levels/cs/python utills
from sorts import tim_sort

def abs(item):
	if item >= 0:
		return item
	elif item < 0:
		return item * -1

def arccos(item, iterations = 1000000):
	item = (sqrt(1 - power(item))) / item
	return arctan(item, iterations)

def arcsin(item, iterations = 1000000):
	item = item / (sqrt(1 - power(item)))
	return arctan(item, iterations)

def arctan(item, iterations = 1000000):
	arctan = 0
	for i in range(iterations):
		coefficient = (power(-1, i))
		numerator = power(item, 2 * i + 1)
		denominator = 2 * i + 1
		arctan += coefficient	* numerator / denominator
	return arctan

def ceil(item, dp = 1000):
	item, pos = __round_pre(item, dp)
	finalItem = []
	for i in range(dp + pos):
		finalItem.append(item[i])

	finalItem[-1] = str(int(finalItem[-1]) + 1)
	finalItem = __round_post(finalItem, pos)
	return finalItem

def cos(item, iterations = 10):
	global pi
	item += pi / 2
	return sin(item)

def deg(item):
	global pi
	item = 180 * item / pi
	return item

def exp(item):
	global e
	return power(e, item)

def floor(item, dp = 1000):
	item, pos = __round_pre(item, dp)
	finalItem = []
	for i in range(dp + pos):
		finalItem.append(item[i])

	finalItem = __round_post(finalItem, pos)
	return finalItem

def fact(item):
	if item == 0 or item == 1:
		return 1
	total = 1
	for i in range(1, item + 1):
		total *= i
	return total

def find_max(itemList):
	max = itemList[0]
	for i in range(len(itemList) - 1):
		if itemList[i] < itemList[i + 1]:
			max = itemList[i + 1]

	return max

def find_min(itemList):
	min = itemList[0]
	for i in range(len(itemList) - 1):
		if itemList[i] > itemList[i + 1]:
			min = itemList[i + 1]

	return min

def hcf(itemList):
	result = itemList[0]
	for i in range(1, len(itemList)):
		result = __hcf(result, itemList[i])
	return result

def hypot(itemOne, itemTwo):
	return(sqrt(power(itemOne) + power(itemTwo)))

def inverse(item):
	return item**-1

def lcm(itemList):
	result = itemList[0]
	for i in range(1, len(itemList)):
		result = __lcm(result, itemList[i])
	return result

def log(item, base = 10, iterations = 10000):
	return round(ln(item) / ln(base), 6)

def ln(item, iterations = 10000):
	ln = 0
	itemTwo = (item - 1) / (item + 1)
	for i in range(1, iterations * 2, 2):
		ln += (1/i) * (itemTwo ** i)
	return 2 * ln

def median(itemList):
	itemList = tim_sort(itemList)
	if mod(len(itemList), 2) == 1:
		return round(itemList[int((len(itemList) - 1) / 2)])
	return round(mean([itemList[int(len(itemList) / 2)], itemList[int(len(itemList) / 2) - 1]]))

def mean(itemList):
	total = 0
	itemNumber = len(itemList)
	for i in range(itemNumber):
		total += itemList[i]
	return total / itemNumber

def mod(itemOne, itemTwo):
	return itemOne // itemTwo

def modf(itemOne):
	return floor(itemOne, 0), remainder(itemOne)

def mode(itemList):
	frequency = {}
	for i in range(len(itemList)):
		if itemList[i] in frequency:
			frequency[itemList[i]] += 1
		else:
			frequency[itemList[i]] = 1
	maxCount = max(frequency.values())
	modes = [key for key, value in frequency.items() if value == maxCount]
	return round(mean(modes))

def perm(itemOne, itemTwo = None):
	if itemTwo > itemOne:
		return 0

	if k == None:
		itemTwo = itemOne

	return fact(itemOne) / fact(itemOne - itemTwo)

def power(item, spower = 2):
	return (item ** power)

def rad(item):
	global pi
	item = 2 * pi * item / 360
	return item

def remainder(itemOne, itemTwo = 1):
	return itemOne % itemTwo

def round(item, dp = 1000):
	item, pos = __round_pre(item, dp)
	if int(item[dp + pos]) < 5:
		finalItem = []
		for i in range(dp + pos):
			finalItem.append(item[i])

	elif int(item[dp + pos]) > 4:
		finalItem = []
		for i in range(dp + pos):
			finalItem.append(item[i])

		finalItem[-1] = str(int(finalItem[-1]) + 1)

	finalItem = __round_post(finalItem, pos)
	return finalItem

def rt(item, power = 2):
	return item**(1/power)

def set_max(item, max):
	if item > max:
		return max
	return item

def set_min(item, min):
	if item < min:
		return min
	return item

def set_range(item, min, max):
	item = set_max(item, max)
	return set_min(item, min)

def sin(item, iterations = 10):
	sine = 0
	for i in range(iterations):
		coefficient = (power(-1, i))
		numerator = power(item, 2 * i + 1)
		denominator = fact(2 * i + 1)
		sine += coefficient	* numerator / denominator
	return sine

def sqrt(item, tolerance = 1e-10):
	if item < 0:
		return False
	guess = item
	while True:
		newGuess = 0.5 * (guess + item / guess)
		if abs(newGuess - guess) < tolerance:
			return round(newGuess)
		guess = newGuess

def tan(item, iterations = 10):
	return sin(x) / cos(x)


def __hcf(itemOne, itemTwo):
	while itemTwo != 0:
		itemOne, itemTwo = itemTwo, itemOne % itemTwo
	return abs(itemOne)

def __round_post(item, pos):
	for i in range(len(item)):
		item[i] = int(item[i])

	for i in reversed(range(len(item))):
		if item[i] > 9:
			item[i - 1] += 1
			item[i] -= 10

	finalItem = '.'
	for i in range(len(item)):
		finalItem = finalItem + str(item[i])

	finalItem = float(finalItem) * (10 ** pos)
	if int(finalItem) == finalItem:
		finalItem = int(finalItem)

	return finalItem

def __round_pre(item, dp):
	item = list(str(item))
	msb = False
	pos = False
	for i in range(len(item)):
		match item[i]:
			case '0':
				if msb == False:
					if item[i + 1] != '.':
						item[i] = None

			case '.':
				item[i] = None
				pos = i
				break

			case _:
				msb = True

	if pos == False:
		pos = len(item)

	for i in reversed(range(len(item))):
		if item[i] == None:
			item.pop(i)

	while len(item) < pos + dp + 1:
		item.append('0')

	return item, pos

def __lcm(itemOne, itemTwo):
	return abs(itemOne * itemTwo) // __hcf(itemOne, itemTwo)

n = 10**4299
e =  2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679



