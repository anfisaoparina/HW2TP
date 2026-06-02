class Ingredient():
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError('Количество должно быть положительным')
        self._quantity = float(value)

    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit}'

    def __repr__(self):
        return f'Ingredient("{self.name}"," {self.quantity}, "{self.unit}")'

    def __eq__(self, notself):
        if self.name == notself.name and self.unit == notself.unit:
            return True
        return False

ing = Ingredient('oisk', 100, 'g')
a = Ingredient('oisk', 30, 'g')

print(ing)
print(ing == a)

class Recipe():
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                break
        else:
            self.ingredients += [ingredient]

    @staticmethod
    def is_valid_ratio(ratio):
        if ratio > 0 and (int(ratio) == ratio or float(ratio) == ratio):
            return True
        return False

    def scale(self, ratio):
        ing = []
        for i in self.ingredients:
            ing += [Ingredient(i.name, i.quantity * ratio, i.unit)]
        return Recipe(self.title, ing)

    def __len__(self):
        return len(set(self.ingredients))

    def __str__(self):
        ing = ', '.join(str(x) for x in self.ingredients)
        return f'{self.title}: {ing}'

rec = Recipe('jnjm', [Ingredient('dss',30,'a'), Ingredient('jks',29, 'a')])
rec.add_ingredient(Ingredient('dss', 200,'a'))
print(rec.ingredients)
print(rec)









