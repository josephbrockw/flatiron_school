class ShoppingCart:

    def __init__(self, employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

    def get_total(self):
        return self._total

    def set_total(self, amount):
        self._total = amount

    total = property(get_total, set_total)

    def get_items(self):
        return self._items

    def set_items(self, items):
        self._total = items

    items = property(get_items, set_items)

    def get_employee_discount(self):
        return self._employee_discount

    def set_employee_discount(self, amount):
        self._employee_discount = amount

    employee_discount = property(get_employee_discount, set_employee_discount)

    def add_item(self, item, cost, quantity=1):
        for i in range(quantity):
            self._items.append({'item': item,
                                'cost': cost,
                                'quantity': quantity})
        self._total += (cost * quantity)
        return self.total

    def price_list(self):
        result = []
        for item in self._items:
            result.append(item['cost'])
        return sorted(result, reverse=True)

    def mean_item_price(self):
        total = self.total
        num_items = len(self.items)
        return total / num_items

    def median_item_price(self):
        cost_list = self.price_list()
        if len(cost_list) % 2 == 0:
            return (cost_list[len(cost_list) // 2] + cost_list[(len(cost_list) // 2) - 1]) / 2
        else:
            return cost_list[len(cost_list) // 2]

    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount / 100
            return self.total * (1 - discount)
        else:
            return 'Sorry. There is no discount to apply.'

    def item_names(self):
        result = []
        for item in self._items:
            result.append(item['item'])
        return result

    def void_last_item(self):
        self.total -= self.items[-1]['cost']
        self._items.pop()
