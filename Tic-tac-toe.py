def welcome():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: a b ")
    print(" a - номер строки  ")
    print(" b - номер столбца ")

area = [[" ", "1", "2", "3"],
        ["1", "-", "-", "-"],
        ["2", "-", "-", "-"],
        ["3", "-", "-", "-"]
        ]
empty_area = [[" ", "1", "2", "3"],
        ["1", "-", "-", "-"],
        ["2", "-", "-", "-"],
        ["3", "-", "-", "-"]
        ]


def show_area(f):
    for i in range(len(area)):
        print(*area[i])


def win_position():
    win = (((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
           ((1, 1), (2, 1), (3, 1)), ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)),
           ((1, 1), (2, 2), (3, 3)), ((1, 3), (2, 2), (3, 1)))
    for cord in win:
        symbols = []
        for c in cord:
            symbols.append(area[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


def input_user():
    while True:
        user_get = input("Введите через пробел координаты матрицы: ").split()

        if len(user_get) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = user_get

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)

        if 1 <= x <= 3 and 1 <= y <= 3:
            if area[x][y] == "-":
                return x, y
            else:
                print("Клетка уже занята, используйте другую!")
                continue
        else:
            print("Координаты вне матрицы, введите их снова.")
            continue

        return x, y


welcome()
# show_area(area)
new_area = show_area(area)
step = 0
answer = "Y"
while answer == "Y":
    step += 1

    if step % 2 == 1:
        print("Ходит крестик 'X'")
    else:
        print("Ходит нолик 'O'")

    x, y = input_user()

    if step % 2 == 1:
        area[x][y] = "X"
    else:
        area[x][y] = "O"

    show_area(area)

    if win_position():
        print("Ничья")
        answer = input("Хотите сыграть еще раз?. Введите 'Y', если хотите повторить. Введите 'N', если хотите закончить")
        if answer == "Y":
            show_area(empty_area)
            continue
        else:
            break

    if step == 9:
        print("Ничья")
        answer = input("Хотите сыграть еще раз?. Введите 'Y', если хотите повторить. Введите 'N', если хотите закончить")
        if answer == "Y":
            show_area(empty_area)
            continue
        else:
            break
