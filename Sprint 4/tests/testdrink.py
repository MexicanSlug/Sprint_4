from api.drink import Drink

# Create a drink
soda = Drink("Sbrite", "Medium")
soda.add_flavor("Lemon")
soda.add_flavor("Raspberry")

# Print details
print(soda.get_base())        # Output: Sbrite
print(soda.get_size())        # Output: Medium
print(soda.get_flavors())     # Output: ['Lemon', 'Raspberry']
print(soda.get_total())       # Calculate total
print(soda)                   # Output: Drink: Sbrite, Size: Medium, Flavors: Lemon, Raspberry
