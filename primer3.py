#!/usr/bin/env python3
# -- config: utf-8 --

def score():
    while True:
        p = 1
        a = float(input("Введите число а: "))
        b = float(input("Введите число b: "))

        if a == 0 or b == 0:
            print("Работа функции прекращена.")
            break

        p *= a
        p *= b
        print(f"Результат умножения: {p}")


if __name__ == '__main__':

    score()
