import sys
# Правила
rules = print("Правила игры:\n" + "Чтобы ввести Х или О, укажи их кооржинаты.\n" + "Сначала по горизонтали, потом по вертикали.")

# Игровое поле
row0 = [" ", 0, 1, 2]
row1 = [0, "-", "-", "-"]
row2 = [1, "-", "-", "-"]
row3 = [2, "-", "-", "-"]

# Вводим координаты для Х
def func_x(row0, row1, row2, row3):
    x = input("Введи Х: ")
    if x == "00" and row1[1] == "-":
        row1[1] = "X"
    elif x == "01" and row1[2] == "-":
        row1[2] = "X"
    elif x == "02" and row1[3] == "-":
        row1[3] = "X"
    elif x == "10" and row2[1] == "-":
        row2[1] = "X"
    elif x == "11" and row2[2] == "-":
        row2[2] = "X"
    elif x == "12" and row2[3] == "-":
        row2[3] = "X"
    elif x == "20" and row3[1] == "-":
        row3[1] = "X"
    elif x == "21" and row3[2] == "-":
        row3[2] = "X"
    elif x == "22" and row3[3] == "-":
        row3[3] = "X"
    else:
        print("Ты что-то не то ввёл...")
        func_x(row0, row1, row2, row3)
    return row0, row1, row2, row3

# Вводим координаты для О
def func_o(row0, row1, row2, row3):
    x = input("Введи О: ")
    if x == "00" and row1[1] == "-":
        row1[1] = "O"
    elif x == "01" and row1[2] == "-":
        row1[2] = "O"
    elif x == "02" and row1[3] == "-":
        row1[3] = "O"
    elif x == "10" and row2[1] == "-":
        row2[1] = "O"
    elif x == "11" and row2[2] == "-":
        row2[2] = "O"
    elif x == "12" and row2[3] == "-":
        row2[3] = "O"
    elif x == "20" and row3[1] == "-":
        row3[1] = "O"
    elif x == "21" and row3[2] == "-":
        row3[2] = "O"
    elif x == "22" and row3[3] == "-":
        row3[3] = "O"
    else:
        print("Ты что-то не то ввёл...")
        func_o(row0, row1, row2, row3)
    return row0, row1, row2, row3

# Печатаем поле
def print_field(row0, row1, row2, row3):
    print(*row0)
    print(*row1)
    print(*row2)
    print(*row3)

# Проверяем на победу
def win(row0, row1, row2, row3):
    if row1[1] == row1[2] == row1[3] != "-":
        print("Победа")
        sys.exit()
    elif row2[1] == row2[2] == row2[3] != "-":
        print("Победа")
        sys.exit()
    elif row3[1] == row3[2] == row3[3] != "-":
        print("Победа")
        sys.exit()
    elif row1[1] == row2[1] == row3[1] != "-":
        print("Победа")
        sys.exit()
    elif row1[2] == row2[2] == row3[2] != "-":
        print("Победа")
        sys.exit()
    elif row1[3] == row2[3] == row3[3] != "-":
        print("Победа")
        sys.exit()
    elif row1[1] == row2[2] == row3[3] != "-":
        print("Победа")
        sys.exit()
    elif row1[3] == row2[2] == row3[1] != "-":
        print("Победа")
        sys.exit()

print_field(row0, row1, row2, row3)

func_x(row0, row1, row2, row3)          # Первый ход Х
print_field(row0, row1, row2, row3)

func_o(row0, row1, row2, row3)          # Первый ход О
print_field(row0, row1, row2, row3)

func_x(row0, row1, row2, row3)          # Второй ход Х
print_field(row0, row1, row2, row3)

func_o(row0, row1, row2, row3)          # Второй ход О
print_field(row0, row1, row2, row3)

func_x(row0, row1, row2, row3)          # Третий ход Х
print_field(row0, row1, row2, row3)
win(row0, row1, row2, row3)

func_o(row0, row1, row2, row3)          # Третий ход О
print_field(row0, row1, row2, row3)
win(row0, row1, row2, row3)

func_x(row0, row1, row2, row3)          # Четвёртый ход Х
print_field(row0, row1, row2, row3)
win(row0, row1, row2, row3)

func_o(row0, row1, row2, row3)          # Четвёртый ход О
print_field(row0, row1, row2, row3)
win(row0, row1, row2, row3)

func_x(row0, row1, row2, row3)          # Пятый ход Х
print_field(row0, row1, row2, row3)
print("Ничья!")