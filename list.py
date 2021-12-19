#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list():
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "No",
            "Название товара",
            "Название магазина",
            "Цена",
        )
    )
    print(line)

    # Вывести данные о всех рейсах.
    for idx, product in enumerate(products, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                product.get('name', ''),
                product.get('nameShop', ''),
                product.get('cost', 0)
            )
        )

    print(line)