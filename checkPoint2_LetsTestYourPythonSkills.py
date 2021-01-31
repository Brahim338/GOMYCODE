import numpy as np
								# Check point 2 Lets test your python skills 
def question1() : 
	print()
# Question 1 : 

		# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
		# between 2000 and 3200 (both included). The numbers obtained should be printed in a list. 
# Create an empty  list :
	result =[] 
	for i in range(2000,3200) : 
		# if the condition match append those number to the list 
		if (i % 7 == 0) and (i % 5 != 0) : 
			result.append(i)
	# print the result in a  list format 
	print('# All such numbers which are divisible by 7 but are a multiple of 5: ')
	print(result)  
	choice = input('\n\nPress Enter ◄──┘ to continue..... or press "R" to repeat : ')
	if choice =='r' or choice =="R" : 
		question1()



def question2() :
	print()
	# Question 2 : 
	'''
	Write a program which can compute the factorial of a given number.
	(the factorial of n is the product of all positive integers less than or equal to n). 
	for example factorial(5)= 5 x 4 x 3 x 2 x 1 the result is 120.  (i.e. factorial (0)=1)
	'''
	given_number = int(input('\tenter a number to compute its factorial: ')) 
	result =1
	for i in range(1,given_number+1) : 
		result *=i 
	print(f'\t\nThe factorial of {given_number} is: {result}')
	choice = input('\n\nPress Enter ◄──┘ to continue..... or press "R" to repeat : ')
	if choice =='r' or choice =="R" : 
		question2()
def question3() : 
	print()
	# Question 3 
	'''
With a given integer number n, write a program to generate a dictionary that contains (i, i*i) such that 
is an integral number between 1 and n (both included). and then the program should print the dictionary. 
Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}  

	'''
	dic={}
	given_number = int(input('Enter an integer number: '))
	for i in range(1,given_number+1) :
		dic[i] =i*i

	print(dic)
	choice = input('\n\nPress Enter ◄──┘ to continue..... or press "R" to repeat : ')
	if choice =='r' or choice =="R" : 
		question3()

def question4() : 
	print()
	''' 
	Question 4 

	Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
	The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 

	missing_char('kitten', 1) → 'ktten'    for example here we remove "i" which is located in the index 1

	missing_char('kitten', 0) → 'itten'   here we remove "k" which is in the index 0

	missing_char('kitten', 4) → 'kittn'   here we remove "e" which is in the index 4
	''' 
	with_missing_char=''
	string= input('Enter a string : ') 

	index = int(input('Enter the index : ')) 

	for i in (range(len(string))) : 
		if i != index : 
			with_missing_char +=string[i] 
	 
	
	print(f"missing_char('{string}', {index}) -► {with_missing_char}") 
	choice = input('\n\nPress Enter ◄──┘ to continue..... or press "R" to repeat : ')
	if choice =='r' or choice =="R" : 
		question4()



def question5() : 
	print()
	'''
		Question 5 

		Write a NumPy program to convert a NumPy array into a Python list structure.

		Expected Output: 

		Original array elements: [[0 1] [2 3] [4 5]] 

		Array to list: [[0, 1], [2, 3], [4, 5]] 
	'''
	 
	_list = []
	data = np.array([[0,1],[2,3],[4,5]]) 
	# for element in data : 
	# 	_list.append(data[element])
	print(f'The NumPy Array is: \n{data}')
	print(f'\n The converted NumPy array to a Python list structure is: {data.tolist()}')    
	input('\n\nPress Enter ◄──┘ to continue.....')
def question6() : 
	print()

	# Write a NumPy program to compute the covariance matrix of two given arrays. 
	# Original array1: [0 1 2] 
	# Original array2: [2 1 0] 
	# Covariance matrix of the said arrays: [[ 1. -1.] [-1. 1.]]
	list1 = [0,1,2] 
	list2 = [2,1,0]
	array1 = np.array(list1) 
	array2 = np.array(list2) 
	print('''
		# Original array1: [0 1 2] 
		# Original array2: [2 1 0] 
		''')
	print('The Covariance matrix of said arrays is: ')
	print(np.cov(array1,array2))
	choice = input('\n\nPress Enter ◄──┘ to continue..... or press "R" to repeat : ')
	if choice =='r' or choice =="R" : 
		question6()


def question7() : 

	''' 
	# Question 7
	Question: Write a program that calculates and prints the value according to the given formula:
	Q = Square root of [(2 * C * D)/H] 
	Following are the fixed values of C and H: C is 50. H is 30. 
	D is the variable whose values should be input to your program in a comma-separated sequence. 
	(that means D contains more than value)
	Example Let's assume the following comma separated input sequence is given to the program: 100,150,180 The output 
	of the program should be: 18,22,24 
	To more understand we will obtain a result for each value of D:  Q1= Square root of [(2 * C * 100)/H] =18,
	Q2= Square root of [(2 * C * 150)/H] = 22 and Q3 = Square root of [(2 * C * 180)/H]  = 24
	Hints: If the output received is in decimal form, it should be rounded off to its nearest value 
	(for example, if the output received is 26.0, it should be printed as 26) 
	In case of input data being supplied to the question, it should be assumed to be a console input. 
	'''
	Q = []  # Q = Square root of [(2 * C * D)/H]
	C = 50 
	H = 30 
	D = input(f'''
	Q = Square root of [(2 * C * D)/H]\n 
	The fixed Value of C and H are C={C} ,H={H}

	Enter the Value of the Variable D in a comma-separated sequence 
			Exemple : 100,150,180 
	\nD Variable : ''')  


	# Create a list of the entred Values 
	D =D.split(',')
	converted =[]
	# Convert the entred value from string to float value
	for item in D : 
		converted.append(float(item))
	# Calculate every Variable of D and append them to the Q list 
	for var in converted : 
		Q.append(round(((2 * C * (var))/H) **.5))

	
	# print the different values of the calculated Q  
	for value in range(len(Q)) : 
		print(f'\nQ{value+1}= {Q[value]}')


	choice = input('\n\nPress Enter ◄──┘ to continue..... or "R" to repeat')
	if choice =='r' or choice =="R" : 
		question7()
def menu() : 
	import os 
	while True : 
		os.system('cls')
		print(''' 
	 ██████╗     ██████     ████  █████╗ ██    ██╗   ██████╗  ██████  █████╗   ███████╗
	██╔════╝    ██╔══╗██   ██╔═╗██╔═══██╗ ██  ██╔╝  ██╔════╝ ██╔══╗██ ██   ██╗ ██╔════╝
	██║ ██████  ██║  ║██   ██║ ╚══╝   ██║  ████╔╝   ██║      ██║  ║██ ██   ██║ █████╗
	██║   ██╔╝  ██╚══╝██   ██║        ██║   ██╔╝    ██║      ██╚══╝██ ██   ██║ ██╔══╝
	 ██████╔╝    ██████╗   ██║        ██║   ██║     ╚██████╗  ██████╗ █████╔═╝ ███████╗
	 ╚═════╝     ╚═════╝   ╚═╝        ╚═╝   ╚═╝      ╚═════╝  ╚═════╝ ╚════╝   ╚══════╝
	╔════════════════════════════════════════════════════════════════════════════════╗
	║          ╔════════════════════════════════════════════════════════════╗        ║
	║          ║            ───────────────────────────────────             ║        ║
	║          ║           │  Artificial Intelegence Training  │            ║        ║
	║          ║            ───────────────────────────────────             ║        ║
	║          ║    ───────────────────────────────────────────────────     ║        ║
	║          ║   │  Check Point2 : Let's Test Your Python Skill....  │    ║        ║ 
	║          ║    ───────────────────────────────────────────────────     ║        ║
	║          ╚════════════════════════════════════════════════════════════╝        ║
	║                                                                                ║
	║           ┌──────────────────┬───────────────────┬───────────────────┐         ║    
	║           │  1. Question1    │   2. Question2    │   3. Question3    │         ║
	║           ├──────────────────┼───────────────────┼───────────────────┤         ║
	║           │  4. Question4    │   5. Question5    │   6. Question6    │         ║
	║           ├──────────────────┴──────────┬────────┴───────────────────┤         ║
	║           │  	    7. Question7          │        8. Quit             │         ║
	║           └─────────────────────────────┴────────────────────────────┘         ║
	╚════════════════════════════════════════════════════════════════════════════════╝''') 
		choice = input('\t\tChoix :')

		while choice not in ['1','2','3','4','5','6','7','8'] : 
			print('\tyou should choice a number from the showing ones in the table') 
			choice = input('\tchoice : ')
			print()
		if choice =='1' : 
			question1()
		elif choice =='2' : 
			question2()
		elif choice =='3' : 
			question3()
		elif choice =='4' : 
			question4() 
		elif choice =='5' : 
			question5()
		elif choice =='6' : 
			question6()
		elif choice =='7' : 
			question7()
		elif choice =='8' : 
			break
menu() 







 