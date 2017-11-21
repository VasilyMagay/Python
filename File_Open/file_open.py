def read_recepts(filename):
  book = {}
  with open(filename) as f:
    while True:
      recept = f.readline()
      recept = recept.strip()
      recept = recept.lower()
      ingredient_num = int(f.readline())
      if recept not in book:
        book[recept] = []
        for s in range(ingredient_num):
          product = f.readline()
          product = product.strip()
          product_list = product.split(" | ")
          book[recept].append({'ingridient_name': product_list[0].lower(), 'quantity': int(product_list[1]), 'measure': product_list[2].lower()})
      else:
        # Повторный рецепт не добавляем
        for s in range(ingredient_num):
          f.readline()
      if not f.readline():
        break
  return book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  cook_book = read_recepts('recepts.txt')
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)

create_shop_list()