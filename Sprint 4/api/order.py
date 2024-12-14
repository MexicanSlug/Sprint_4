class Order:
    TAX_RATE = 0.0725

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Invalid index.")
        self.items.pop(index)

    def get_items(self):
        return self.items

    def get_num_items(self):
        return len(self.items)

    def get_total(self):
        return sum(item.get_total() for item in self.items)

    def get_receipt(self):
        receipt = {"items": [], "subtotal": 0.0, "tax": 0.0, "total": 0.0}
        for item in self.items:
            if hasattr(item, 'get_total'):  # Handle IceStorm, Food, Drink, etc.
                receipt["items"].append({
                    "type": type(item).__name__,
                    "details": str(item),
                    "price": item.get_total()
                })
        subtotal = self.get_total()
        receipt["subtotal"] = subtotal
        receipt["tax"] = subtotal * self.TAX_RATE
        receipt["total"] = subtotal + receipt["tax"]
        return receipt
