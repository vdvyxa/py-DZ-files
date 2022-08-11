import os

# Получение словаря рецептов из файла
# PARAMS
#   FILENAME - имя файла (формат txt)
# RETURN
#   словарь рецептов в формате
#   {'имя_рецепта':  [
#       {'ingredient_name', 'quantity', 'measure'},
#       {'ingredient_name', 'quantity', 'measure'},
#       ...
#       ],
#   ...
#   }
def load_recipes_book(filename):
    # результат
    cook_book = {}
    # работа с файлом
    with open(filename) as file:
        line = file.readline().strip()
        # цикл пока не конец файла
        while line != '':
            # 1-я строка - название рецепта
            recipe_name = line
            # 2-я строка - кол-во ингредиентов
            ingredient_number = int(file.readline().strip())
            ingredients = []
            # цикл по считыванию ingredient_number строк из файла
            for i in range(ingredient_number):
                # разбиваем строку по разделителю: ' | '
                data = file.readline().split(' | ')
                # добавляем новый элемент в рецепт
                ingredients += [{
                    'ingredient_name': data[0].strip(),
                    'quantity': int(data[1]),
                    'measure': data[2].strip()
                }]
            # добавляем в результат новый рецепт
            cook_book[recipe_name] = ingredients

            # считываем пустую строку - разделитель рецептов
            line = file.readline().strip()
            # считываем имя нового рецепта (или пустая строка, если конец)
            line = file.readline().strip()
    # возвращаем результат
    return cook_book

# Получение необходимых ингредиентов для указанных блюд для определенного числа порций
# PARAMS
#   COOK_BOOK - книга рецептов
#   DISHES - список рецептов []
#   PERSON_COUNT - число порций
# RETURN
#   словарь ингредиентов в формате
#   {'ингредиент1':  {'measure', 'quantity'},
#    'ингредиент2':  {'measure', 'quantity'},
#    ...
#   }
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    result = {}
    for dish in dishes:
        # получение списка ингредиентов для очередного рецепта
        ingredients = cook_book.get(dish, [])
        # цикл по каждому ингредиенту
        for ingredient in ingredients:
            # получаем информацию об очередном ингредиенте
            ingredient_name = ingredient['ingredient_name']
            ingredient_quantaty = ingredient['quantity']
            ingredient_measure = ingredient['measure']
            # проверка, если ингредиент уже есть в результате и его размерность (measure) совпадает
            # то сохраняем старое количество (чтобы потом добавить)
            if ingredient_name in result and result[ingredient_name]['measure'] == ingredient_measure:
                prev_quantaty = result[ingredient_name]['quantity']
            else:
                prev_quantaty = 0
            # добавляем/обновляем запись с ингредиентом
            # (с учетом старого значения количества)
            result[ingredient_name] = {
                'measure': ingredient_measure,
                'quantity': prev_quantaty + ingredient_quantaty * person_count
            }
    return result
  

###########################################################
###########################################################

def __main__():
    #filename = input('Имя файла с рецептами: ')
    filename = 'recipes.txt'  

    # ДЗ 1
    cook_book = load_recipes_book(filename)
    print(cook_book)

    # ДЗ 2
    dishes = ['Омлет', 'Пашот', 'Фахитос']
    ingredients =  get_shop_list_by_dishes(cook_book, dishes, 2)
    print(ingredients)

###########################################################
###########################################################

__main__()
