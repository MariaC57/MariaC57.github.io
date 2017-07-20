#grocery = [ "apples", "cereal", "milk" ]
#print (grocery[0])
#print (grocery[1])
#print (grocery[2])

#numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#index = 0 

#for n in numbers:
	#print ("index" + str(index) + "numbers there =" + str(n))
	#index 

from random import *

names= ["Bob","Lily", "Nina", "John", "Kim", "Dell", "Nicole", "Dan", "Julie", "Jose", "Steven", "Mary", "Brian", "Joan"]
last_names=[ "b","c","f","g","p","o","r","q","t","m","l","h","u","v"]

names_used = []
last_names_used = []


for index in range(len(names)):
	random_num1 = randient(0, len(names)-1)
	random_num2 = randient(0, len(last_names)-1)

	random_first = names[random_num1]
	random_last = last_names[random_num2]

	while random_first in names_used:
		random_first= names[randient(0, len(names)-1)]

	while random_last in last_names_used:
		random_last = last_names[randient(0, len(last_names)-1)]

		names_used.append(random_first)
		last_names_used.append(random_last)

		print(random_first + " " + random_last)
			
#index=0
#user_input = input( pick a number between 0 and 13)
#if "0" print (name[0])


#for n in names:
	#print ("index" + str(index)+ "almost there =" + str(n))


