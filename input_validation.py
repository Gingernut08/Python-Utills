##  cd my drive/a-levels/cs/cs nea



def intInput(prompt):
	userInput = input(prompt)
	if bool(userInput) == True:
		try:
			userInput = int(userInput)

		except ValueError:
			return intInput(prompt)

		return userInput

	else:
		return intInput(prompt)

def strInput(prompt):
	userInput = input(prompt)
	if bool(userInput) == True:
		try:
			userInput = str(userInput)

		except ValueError:
			return strInput(prompt)

		return userInput

	else:
		return intInput(prompt)

def floatInput(prompt):
	userInput = input(prompt):
	if bool(userInput) == True:
		try:
			userInput = float(userInput)

		except ValueError:
			return floatInput(prompt)

		return userInput

	else:
		return floatInput(prompt)



print(intInput('hellow World'))