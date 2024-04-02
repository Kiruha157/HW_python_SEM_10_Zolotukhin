import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
        #print(list_1)
    result = []
    result = [i for i in list_1 if data in i]
    #print(result)
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, data: str):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
    with open(source, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    #print(list_1)
    result = []
    result = [i for i in list_1 if data in i]
    #print(result)
    if not result:
        return "По указанному значению совпадений не найдено"
    with open(dest, "r", encoding="utf-8") as file:
        list_2 = file.read().split("\n")
    #print(list_1)
    
    #Проверка наличия искомого в dest и запись в случае отсутсвтия
    new_line = '\n' if read_all(dest) != "" else ''
    count = 0
    for i in result:
        if i not in list_2:
            with open(dest, "a", encoding="utf-8") as copy:
                copy.write(f"{new_line}{i}")
                count += 1
            return f"{line}---Скопировано из {source} в {dest} {count} контактов"
        else:
            return f"{line}Контакт уже есть в файле {dest}"
    


    


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
5 - остановить выполнение программы 
"""
line = '\n'

file_1 = 'Numbers_1.txt'
file_2 = 'Numbers_2.txt'
if (file_1 or file_2) not in os.listdir():
    print("указанное имя файла отсутсвует")
    print(os.listdir())
    sys.exit()


while True:
    mode = int(input(f"{INFO_STRING} {line}"))
    if mode == 1:
        print(read_all(file_1))
    elif mode == 2:
        name = input(f"{line}Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file_1)
    elif mode == 3:
        data = input(f"{line}Введите значение: ")
        print(search_user(file_1, data))
    elif mode == 4:
        data = input(f"{line}Введите значение для поиска и копирования: ")
        print(transfer_data(file_1, file_2, data))
    elif mode == 5:
        sys.exit()