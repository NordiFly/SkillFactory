try:
    stroka = input("Введите любое число: ")
    if isinstance(stroka, (int, float)):
        stroka = int(stroka) or float(stroka)
except ValueError:
    print("Число введи додик")
else:
    print(stroka)
    print(type(stroka))
finally:
    print('Выход из программы')
