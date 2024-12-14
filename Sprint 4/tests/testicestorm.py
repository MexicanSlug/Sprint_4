from api.ice_storm import IceStorm

# Create an Ice Storm
storm = IceStorm("Mint Chocolate Chip")

# Add flavors
storm.add_flavor("Chocolate")
storm.add_flavor("Banana")

# Add toppings
storm.add_topping("Cherry")
storm.add_topping("Whipped Cream")

# Check details
print("Base flavor:", storm.get_base())           # Output: Mint Chocolate Chip
print("Flavors:", storm.get_flavors())            # Output: ['Mint Chocolate Chip', 'Chocolate', 'Banana']
print("Toppings:", storm.get_toppings())          # Output: ['Cherry', 'Whipped Cream']
print("Total Cost: $", storm.get_total())         # Calculate total cost

# Print the string representation
print(storm)  # Output: Ice Storm: Mint Chocolate Chip, Toppings: Cherry, Whipped Cream. Total: $X.XX
