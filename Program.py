from IngredientsList import pantry, recipes
from colorama import Fore, Style

valid = None
recipeChoice = {}
select = None
itemsBuy = []

for no, recipe in enumerate(recipes,1):
	recipeChoice[str(no)] = recipe

while valid != '0':
	print(Fore.BLUE + "\nThe recipes available are:")   #Listing Available Recipes
	print(Fore.WHITE + "--------------------------")

	for no, recipe in enumerate(recipes,1):
		print(Fore.WHITE + f"{no}: {recipe}")

	valid = input("\n>")

	if valid in recipeChoice:		#Validating User's Selection
		select = recipeChoice[valid]
		print(Fore.GREEN + f"Selected: {select}\n")
		print(Fore.YELLOW + f"Listing Ingridents for {select}")
		print(Fore.YELLOW + "-----------------------------------------------------")

		for item in recipes[select]:	#Listing the key Ingredients and checking its Availablity
			print(Fore.YELLOW + item, end=":")
			if item in pantry:
				print(Fore.GREEN + "OK")
			else:
				print(Fore.RED + "OUT OF STOCK!!")
				if not item in itemsBuy:	#Add to Shopping Cart
					itemsBuy.append(item)

if itemsBuy == []:
	print(Fore.YELLOW +"No need for shoping")
else:
	print(Fore.YELLOW + "Items to shop for:")
	print(Fore.YELLOW + "-------------------")
	for sn, items in enumerate(itemsBuy,1):
		print(Fore.BLUE + f"{sn}: {items}")
