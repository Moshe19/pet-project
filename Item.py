import csv

class Item:  
    pay_rate = 0.8 # ставка зп после 20% скидки
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
    # проверка требований
        assert price >= 0, f"Цена {price} меньше нуля!"
        assert quantity >= 0, f"Количество товара {quantity} меньше нуля!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # Действия для выполнения
    
        Item.all.append(self)
        
    def calculate_total_price(self):  # Метод
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate  #получаем доступ к ставке зп

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f, quotechar="'", skipinitialspace=True)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
        
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

Item.instantiate_from_csv()
print(Item.all)

# item1.apply_discount()

# item2.pay_rate = 0.7
# item2.apply_discount()


# print(item2.price)
# print(item1.price)
# print(item1.calculate_total_price())
# print(Item.__dict__)        # посмотреть все атрибуты класса 
# print(item1.__dict__)