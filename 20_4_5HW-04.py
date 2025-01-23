import json

with open(r"D:\Обучение тестировщик Python\20_1\orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
#1. Номер самого дорогого заказа
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1.Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
#2. Номер заказа с самым большим количеством товаров
max_quantity = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем кол-во товаров в заказе
    quantity = orders_data['quantity']
    # если кол-во товаров больше максимального - запоминаем номер и кол-во товаров
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'2.Номер заказа с самым большим количеством товаров: {max_order}, товаров в заказе: {max_quantity}')
#3. В какой день в июле было сделано больше всего заказов
date_dict = {}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1
max_orders_day = max(date_dict, key = date_dict.get)
print(f'3.День в июле, когда было сделано больше всего заказов: {max_orders_day}, всего {date_dict[max_orders_day]} заказов')
#4. Какой пользователь сделал самое большое количество заказов за июль?
max_user_orders = 0
user_dict = {}
user_id = 0
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + 1
    orders_1 = user_dict.get(user_id)
    if orders_1 > max_user_orders:
        max_user_orders = orders_1
print(f'4.Пользователь {user_id} сделал больше всего заказов: {max_user_orders}')
#5. У какого пользователя самая большая суммарная стоимость заказов за июль?
max_user_price = 0
user_dict1 = {}
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_dict1[user_id] = user_dict1.get(user_id, 0) + orders_data['price']
    all_price = user_dict1.get(user_id)
    if all_price > max_user_price:
        max_user_price = all_price
print(f'5.Пользователь {user_id} имеет самую большую стоимость заказов: {max_user_price}')
#6. Какая средняя стоимость заказа была в июле?
orders_dict = {}
sum_price = 0
sum_orders = 0
for order_num, orders_data in orders.items():
    orders_dict[order_num] = orders_dict.get(order_num, orders_data['price'])
    sum_price = sum(orders_dict.values())
    sum_orders = len(orders_dict.values())
mean_value = sum_price / sum_orders
print(f'6.Средняя стоимость заказа в июле: {mean_value}')
#7. Какая средняя стоимость товаров в июле?
sum_quantity = 0
orders_dict1 = {}
product_dict = {}
for order_num, orders_data in orders.items():
    orders_dict1[order_num] = orders_dict1.get(order_num, orders_data['price'])
    product_dict[order_num] = product_dict.get(order_num, orders_data['quantity'])
    sum_price = sum(orders_dict1.values())
    sum_quantity = sum( product_dict.values())
mean_value_product = sum_price / sum_quantity
print(f'7.Средняя стоимость товара в июле: {round(mean_value_product, 2)}')


