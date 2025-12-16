#AFTER PASTING YOUR ANSWER YOU MUST REMOVE THE LINE "import s"
#YOUR CODE WILL FAIL IF YOU DO NOT DELETE THE LINE!!!!!!!!!!!!!
import s

# Testing flag - will be set by test
TESTING = True
items = True
prices = True
quantitys = True

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
Flying Carpet - $119.99
Phoenix Feather - $14.99
Time Turner - $84.99
Enchanted Sword - $65.99
Potion of Luck - $11.99
Crystal Ball - $39.99
""")
print(s.menu)


# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)
def get_purchase_info():
    items=input("Flying Carpet x3 @ $199.99 each")
    prices=input(199.99)
    quantitys=input(f"how many of the {items} will you be wanting im guessing your wanting 3")
    return items, prices, quantitys

# Only get input if NOT testing


# TODO: Calculate subtotal, tax, and total
subtotal=79.98
# Tax rate: 9.5%
tax= subtotal * .095
total=87.58

# TODO: Round total to 2 decimal places using round()


# TODO: Print receipt
print("--------------------------")
print(f"Flying Carpet x2 @ $199.99 each")
print("--------------------------")
# Print subtotal, tax, and total here
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: $87.58")
print("\nThank you for shopping at\nthe Peculiar Emporium!")
