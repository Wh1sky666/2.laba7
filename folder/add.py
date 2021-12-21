#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add():
    name = input("Название пункта назначения рейса ")
    nameShop = input("Номер рейса ")
    cost = input("Начального пункта ")

    # Создать словарь.
    product = {
        'name': name,
        'nameShop': nameShop,
        'cost': cost,
    }

    # Добавить словарь в список.
    products.append(product)
    # Отсортировать список в случае необходимости.
    if len(products) >> 1:
        products.sort(key=lambda item: item.get('name', ''))
