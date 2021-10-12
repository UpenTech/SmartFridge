from IngredientsList import pantry, recipes
from colorama import Fore, Style

valid = None
recipeChoice = {}
select = None

for no, recipe in enumerate(recipes,1):       #Avaiable Recipes Listing
	recipeChoice[str(no)] = recipe

while valid != '0':
	print(Fore.BLUE + "\nThe recipes available are:")
	print(Fore.WHITE + "--------------------------")

	for no, recipe in enumerate(recipes,1):
		print(Fore.WHITE + f"{no}: {recipe}")

	valid = input("\n>")

	if valid in recipeChoice:		#Validating User's Selection
		select = recipeChoice[valid]
		print(Fore.GREEN + f"Selected: {select}\n")
		print(Fore.YELLOW + f"Listing Ingridents for {select}")
		print(Fore.YELLOW + "-----------------------------------------------------")

		for item in recipes[select]:	#Listing the key Ingredients
			print(Fore.YELLOW + item, end=":")
			if item in pantry:
				print(Fore.GREEN + "OK")
			else:
				print(Fore.RED + "OUT OF STOCK!!")
