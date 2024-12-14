class Drink:
    SIZE_COSTS = {"Small": 2.00, "Medium": 2.50, "Large": 3.00}

    def __init__(self, base, size):
        self.base = base
        self.size = size
        self.flavors = []

    def get_base(self):
        return self.base

    def get_size(self):
        return self.size

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def get_flavors(self):
        return self.flavors

    def get_total(self):
        return self.SIZE_COSTS[self.size] + 0.25 * len(self.flavors)

    def __str__(self):
        return f"Drink: {self.base}, Size: {self.size}, Flavors: {', '.join(self.flavors)}"
