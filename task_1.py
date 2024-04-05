from pprint import pprint

cook_book = {}
with open('example.txt', encoding='UTF8') as file:

    while True:
        dish = file.readline().rstrip()
        ingredient_count = file.readline().rstrip()
        if not dish or not ingredient_count:
            break
        cook_book[dish] = []
        for i in range(int(ingredient_count)):
            ingredient_name, quantity, measure = file.readline().split('|')
            cook_book[dish] += [{'ingredient_name': ingredient_name.strip(),
                                 'quantity': quantity.strip(),
                                 'measure': measure.strip()}]
        file.readline()
pprint(cook_book)
