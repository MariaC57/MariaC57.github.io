start = "You deal in exotic and endangered animals. What kind of animals do you specialize in?"

elephant = "African elephants' tusks can weigh dozens of kilograms, and are used for ivory ornaments and jewellery."
elephant1 = "African elephants are an endangered species because of human encroachment on their territory, as well as poaching."
elephant2 = "Visit the WWF for more information abou African elephants, and ways to help their cause."

panda = "To learn about panda poaching and donate to the cause visit WWF.com."

tiger = "China's tigers are heavily endangered. To learn more about their poaching and donate to the cause visit WWF.com"

print(start)

#choice one
user_input = input("Type 1 for tigers, 2 for elephants, and 3 for pandas. ")

#if mean user
while user_input != "1" and user_input != "2" and user_input != "3":
	print(start)
	user_input = input("Type 1 for tigers, 2 for elephants, and 3 for pandas. ")
#tigers
if user_input == "1":
	print("You hunt China's tigers, which are prized for their beautiful pelts, but their bones and all other body parts are considered to hold magical properties.")
	print("Do you sympathize for the tigers?")
	user_input = input("If you feel bad for them type 1, if not type 2.")
	
	while user_input != "1" and user_input != "2":
		print("You hunt China's tigers, which are prized for their beautiful pelts, but their bones and all other body parts are considered to hold magical properties.")
		print("Do you sympathize for the tigers?")
		user_input = input("If you feel bad for them type 1, if not type 2.")

	if user_input == "1":
			print("I hate the hunt, I hate that stealing the beauty of life, and I especially hate the blood.")
			print("Tigers truly are magical, but their magic exists in their grace and beauty. Dead, their magic is gone.")
			print("I hate my jon, but we all gotta pay the bills, ya know?")
			print(tiger)

	if user_input == "2":
			print("Who cares? Poaching gets me FILTHY rich as well as status in the black market and access to many luxuries.")
			print(tiger)

#elephants
if user_input == "2":
	print("You hunt African Elephants for their ivory.")
	print("Why do you do it?")

	user_input = input("If you do it for the money, type 1. If you do it because of familial obligation, type 2.")

	while user_input != "1" and user_input != "2":
		print("You hunt African Elephants for their ivory.")
		print("Why do you do it?")

		user_input = input("If you do it for the money, type 1. If you do it because of familial obligation, type 2.")

	
	if user_input == "1":
		user_input = input("Type 1 if you need the money to care for your family. Type 2 if the money is for personal gain.")

		while user_input != "1" and user_input != "2":
			user_input = input("Type 1 if you need the money to care for your family. Type 2 if the money is for personal gain.")

		if user_input == "1":
			print("You have a family of five, and there's a baby on the way.") 
			print("You heard that elephant poaching was lucrative, and you don't find it difficult.")
			print("It makes you sick to your stomach, but you suffer through the guilt to care for your family.")
			print(elephant)
			print(elephant1)
			print(elephant2)

		if user_input == "2":
			print("Everyone knows money rules the world. Elephants will be poached no matter what, why shouldn't it benefit me?")
			print(elephant)
			print(elephant1)
			print(elephant2)

	if user_input == "2":
		print("My family has dealt in poaching for decades.")
		user_input = input("Do you like poaching? Type 1 if you hate it, type 2 if you don't mind")
		
		while user_input != "1" and user_input != "2":
			print("My family has dealt in poaching for decades.")
			user_input = input("Do you like poaching? Type 1 if you hate it, type 2 if you don't mind")			

		if user_input == "1":
			print("I hate poaching and wish that we could protect these animals, but I owe it to my family.")
			print(elephant)
			print(elephant1)
			print(elephant2)


		if user_input == "2":
			print("I've helped in the family bussiness for as lont as I can remember.")
			print("I can't imagine a different life for myself.")
			print(elephant)
			print(elephant1)
			print(elephant2)



if user_input == "3":

	print("you work in China in the forest where most of the pandas live and you are going hunting for them .")
	print("You walk into the forest and hanging in the banboo you see a mother panda and her baby.")
	print(" You take out your gun and you are getting ready to fire at one of them.")
	user_input = input ("Type 1 to kill the baby, type 2 to kill the mother.")
	
	while user_input != "1" and user_input != "2":
		print("you work in China in the forest where most of the pandas live and you are going hunting for them .")
		print("You walk into the forest and hanging in the banboo you see a mother panda and her baby.")
		user_input = input(" You take out your gun and you are getting ready to fire at one of them.Type 1 to kill the baby, type 2 to kill the mother.")
	


	if user_input == "1":
		print("There is one less panda in China and that has caused the fall of the forest ")
		user_input = input("Do You help re-build the forest. Type 1 for yes and 2 for no. ")
		
		while user_input != "1" and user_input != "2":
			print("There is one less panda in China and that has caused the fall of the forest ")
			user_input = input("Do You help re-build the forest. Type 1 for yes and 2 for no. ")

		if user_input == "1":
			print (" You have helped recreate the enviorment for the pandas and now more pandas are apperaing and the people of China are happy")
			print(panda)
		if user_input == "2":
			print (" You not only caused the deaths of the panda population but the rest of the animals in the forest as well as the snub-nosed monkey")
			print(panda)


	if user_input == "2":
		print("You have left a baby panda as an orphan to fend for itself")
		user_input = input ("will you help raise the baby panda. Type 1 for yes and 2 for no.")

		while user_input != "1" and user_input != "2":
			print("You have left a baby panda as an orphan to fend for itself")
			user_input = input ("will you help raise the baby panda. Type 1 for yes and 2 for no.")

		if user_input == "1":
			print ("Although you killed its mother you have helped the panda grows strong and you gave up your job of killing animals")
			print(panda)
		if user_input == "2":
			print (" The panda grows up alone in the forest not knowing how to survive and ends up dying")
			print(panda)
