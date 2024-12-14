class Food:
    def __init__(self, food_type):
        self.food_type = food_type
        self.toppings = []

    def get_food_type(self):
        return self.food_type

    def add_topping(self, topping):
        self.toppings.append(topping)

    def get_toppings(self):
        return self.toppings

    def get_total(self):
        return 3.00 + 0.50 * len(self.toppings)

    def __str__(self):
        return f"Food: {self.food_type}, Toppings: {', '.join(self.toppings)}"
