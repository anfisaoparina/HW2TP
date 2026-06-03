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
        return f'Ingredient("{self.name}", {self.quantity}, "{self.unit}")'

    def __eq__(self, notself):
        if self.name == notself.name and self.unit == notself.unit:
            return True
        return False

ing = Ingredient('oisk', 100, 'g')
a = Ingredient('oisk', 30, 'g')

# print(ing)
# print(ing == a)

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
# print(rec.ingredients)
# print(rec)

class ShoppingList():
    def __init__(self, _items_):
        self.itemss = _items_

    def addrec(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        for i in recipe.ingredients:
            self.itemss += [(i, recipe.title)]

    def remove_recipe(self, title):
        for i in self.itemss.copy():
            if i[1] == title:
                self.itemss.remove(i)

    def get_list(self):
        d = dict()
        for i in self.itemss:
            if (i[0].name, i[0].unit) in d.keys():
                d[(i[0].name, i[0].unit)] += i[0].quantity
            else:
                d[(i[0].name, i[0].unit)] = i[0].quantity
        m = []
        for i in d.keys():
            m += [Ingredient(i[0], d[i], i[1])]
        m =sorted(m, key = lambda x: x.name)
        return m

    def __add__(self, notself):
        new  = ShoppingList([])
        for i in self.itemss:
            new.itemss += [i]
        for j in notself.itemss:
            new.itemss += [j]
        return new

s = ShoppingList([(ing, 'smskm'), (a, 'jssj')])
g = ShoppingList([(ing, 'jnjwnls'), (a, 'lwlk')])
s.addrec(rec, 5)
print(s.itemss)
s.remove_recipe('jnjm')
print(s.itemss)
print(s.get_list())
print((s + g).itemss)












