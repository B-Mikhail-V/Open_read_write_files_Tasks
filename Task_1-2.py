import os
from pprint import pprint

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='utf-8') as dishes:
    cook_book = {}  # Окончательная книга рецептов
    for dish in dishes:
        dish_name = dish.strip()
        counter = int(dishes.readline().strip())
        temp_list = []
        for ingredient in range(counter):
            ingredient_name, ingredient_quantity, ingredient_measure = dishes.readline().split("|")
            temp_list.append({'ingredient_name': ingredient_name.strip(), 'quantity':  ingredient_quantity.strip(),
                              'measure': ingredient_measure.strip()})
        cook_book[dish_name] = temp_list
        dishes.readline()
    print('Книга рецетов:')
    pprint(cook_book)
    print()


def get_shop_list_by_dishes(dishes_order, person_count):
    """
    Функция получает на вход спиок блюд "dishes_order"
    и возвращает список продуктов с количеством и единицами измерений.
    """

    dishes_total = dishes_order * person_count
    dict_final = {}  # Окончательный словарь продуктов
    dict_new = {}  # Промежуточный словарь для наполнения в цикле
    for dish_order in dishes_total:
        for key, value in cook_book.items():
            if dish_order == key:
                for count in range(len(value)):
                    if value[count]['ingredient_name'] not in dict_new.keys():
                        dict_new[value[count]['ingredient_name']] = {'quantity': value[count]['quantity'],
                                                                     'measure': value[count]['measure']}
                        dict_final.update(dict_new)
                    else:
                        new_quality = int(value[count]['quantity']) + \
                                      int(dict_new[value[count]['ingredient_name']]['quantity'])
                        dict_new[value[count]['ingredient_name']] = \
                            {'quantity': new_quality, 'measure': value[count]['measure']}
                        dict_final.update(dict_new)

    return pprint(dict_final)

def check_order(dishes_order):
    """
    Попытка сделать проверку списка блюд заказа,
    но до конца не получилось: список корректируется,
    если в списке несуществующее блюдо, а вот сообщение
    выводится некорректно.
    """
    for dish in dishes_order:
        if dish not in cook_book.keys():
            print(f"В книге рецептов нет блюда {dish}")
            dishes_order.remove(dish)
    return dishes_order

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос', 'Фахитос_2'], 3)
