class order:
    def __init__(self,name):
        self.name = name
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    def get_price(self):
        price = 0.0
        for item in self.items:
            price = price + item.get_price()
        return price
    def __str__(self):
        s = [str(item) for item in self.items]
        return "\n".join(s)
    def display(self):
        print("==========================================")
        print("Here is a summary of your order")
        print("Order for " + self.name)
        print("Here is a list of items in the order")

        for item in self.items:
            print("-----------")
            print(str(item))
        print("-----------")
        print("Total Order Amount :$" + str(self.get_price()))
        print("==========================================")

