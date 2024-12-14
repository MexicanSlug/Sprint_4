class IceStorm:
    BASE_COSTS = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }
    TOPPING_COSTS = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Storios": 1.00,
        "Dig Dogs": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50
    }

    def __init__(self, base_flavor):
        if base_flavor not in self.BASE_COSTS:
            raise ValueError(f"Invalid base flavor: {base_flavor}")
        self.base_flavor = base_flavor
        self.toppings = []
        self.flavors = [base_flavor]

    def get_flavors(self):
        return self.flavors

    def add_flavor(self, flavor):
        if flavor not in self.BASE_COSTS:
            raise ValueError(f"Invalid flavor: {flavor}")
        self.flavors.append(flavor)

    def get_base(self):
        return self.base_flavor

    def get_num_flavors(self):
        return len(self.flavors)

    def add_topping(self, topping):
        if topping not in self.TOPPING_COSTS:
            raise ValueError(f"Invalid topping: {topping}")
        self.toppings.append(topping)

    def get_toppings(self):
        return self.toppings

    def get_total(self):
        base_cost = sum(self.BASE_COSTS[flavor] for flavor in self.flavors)
        topping_cost = sum(self.TOPPING_COSTS[topping] for topping in self.toppings)
        return base_cost + topping_cost

    def __str__(self):
        return f"Ice Storm: {self.base_flavor}, Toppings: {', '.join(self.toppings)}. Total: ${self.get_total():.2f}"
