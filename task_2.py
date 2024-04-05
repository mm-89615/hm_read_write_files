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


def get_shop_list_by_dishes(dishes: list[str], person_count: int) -> dict:
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']['quantity']] += (
                                int(ingredient['quantity']) * person_count)
                else:
                    shop_list[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': int(ingredient['quantity']) * person_count}
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
