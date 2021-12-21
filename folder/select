#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select():
    parts = command.split('', maxsplit=2)
    sel = (parts[1])

    count = 0
    for product in products:
        if products.get('name') == sel:
            count = "Цена"
            print(
                '{:>4}: {}'.format(count, products.get('cost', ''))
            )
            print('Название магазина:', products.get('nameShop', ''))
            print('Название товара:', products.get('name', ''))

    # Если счетчик равен 0, то рейсы не найдены.
    if count == 0:
        print("Товар не найден.")
