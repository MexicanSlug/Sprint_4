from api.food import Food

# Create a food item
fries = Food("French Fries")
fries.add_topping("Chili")
fries.add_topping("Cheese")

# Print details
print(fries.get_food_type())  # Output: French Fries
print(fries.get_toppings())   # Output: ['Chili', 'Cheese']
print(fries.get_total())      # Output: 4.00
print(fries)                  # Output: Food: French Fries, Toppings: Chili, Cheese
