#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть размещены в алфавитном порядке по названиям пунктов назначения; вывод на экран
# информации о поездах, отправляющихся после введенного с клавиатуры времени; если
# таких поездов нет, выдать на дисплей соответствующее сообщение.

import sys
import json


def add(train, time, name, num, trains):
        train = {
            'name': name,
            'num': num,
            'time': time,
        }

        trains.append(train)
        if len(trains) > 1:
            trains.sort(key=lambda item: item.get('num', ''))


def list(trains):
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )

        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)

        for idx, train in enumerate(trains, 1):
            print(
                '| {:>4} | {:<20} | {:<20} | {:<20} | {:>15} |'.format(
                    idx,
                    people.get('Название пункта назначения', ''),
                    people.get('Номер поезда: ', ''),
                    people.get('Время отправления', 0)
                )
            )
        print(line)

def select(trains):
        count = 0
        for train in trains:
            if train.get('surname') == sur:
                count += 1
                print('Название пункта назначения:', train.get('name', ''))
                print('Номер поезда:', train.get('nnum', ''))
                print('Время отправления:', train.get('time', ''))

        if count == 0:
            print("Таких фамилий нет !")


def load(parts):
        with open(parts, 'r') as f:
            return trains


def save(trains, parts):
        with open(parts, 'w') as f:
            json.dump(peoples, f)



import sys
import json

if __name__ == '__main__':

    trains = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = input("Номер поезда: ")
            time = input("Время отправления: ")

            train = {
                'name': name,
                'num': num,
                'time': time,
            }

            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('num', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 17
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        train.get('name', ''),
                        train.get('num', ''),
                        train.get('time', 0)
                    )
                )

            print(line)

        elif command.startswith('select'):

            parts = command.split(' ', maxsplit=2)

            times = parts[1]

            count = 0
            for train in trains:
                if train.get('time') == times:
                    count += 1
                    print('Время отправления:', train.get('time', ''))
                    print('Номер поезда:', train.get('num', ''))
                    print('Пункт назначения:', train.get('name', ''))

            if count == 0:
                print("Таких поездов нет!")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                trains = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(trains, f)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <Время> - запросить информацию о выбранном поезде;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
