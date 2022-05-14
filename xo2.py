game = [[" ", "1", "2", "3"],
        ["1", "-", "-", "-"],
        ["2", "-", "-", "-"],
        ["3", "-", "-", "-"]
       ]

def game_continue():
    for i in game:
        for j in i:
            print(j, end = " ")
        print()

def move_x():
    variants_move = ["11", "12", "13", "21", "22", "23","31", "32", "33"]
    move = str(input("Ход крестиков. Введите координаты хода(две цифры без пробела, номер строки и столбца)"))
    if move in variants_move:
        move = list(move)
        i, j = int(move[0]), int(move[1])
        if game[i][j] == "-":
                game[i][j] = "x"
                print()
                game_continue()
        else:
                print("Сюда нельзя. Выберите свободную игровую клетку")
                move_x()
    else:
        print("Введены некоректные координаты. Попробуйте еще раз")
        move_x()
		    
def move_o():
    variants_move = ["11", "12", "13", "21", "22", "23","31", "32", "33"]
    move = str(input("Ход ноликов. Введите координаты хода(две цифры без пробела, номер строки и столбца)"))
    if move in variants_move:
        move = list(move)
        i, j = int(move[0]), int(move[1])
        if game[i][j] == "-":
            game[i][j] = "o"
            print()
            game_continue()
        else:
            print("Сюда нельзя. Выберите свободную игровую клетку")
            move_o()
    else:
        print("Введены некоректные координаты. Попробуйте еще раз")
        move_o()

def check_vin():
    comb_vin = [game[1][1]==game[1][2]==game[1][3],
                game[2][1]==game[2][2]==game[2][3],
                game[3][1]==game[3][2]==game[3][3],
                game[1][1]==game[2][1]==game[3][1],
                game[1][2]==game[2][2]==game[3][2],
                game[1][3]==game[2][3]==game[3][3],
                game[1][1]==game[2][2]==game[3][3],
                game[1][3]==game[2][2]==game[3][1],
                ]
    if any(comb_vin):
        return True
    else:
        return False

print("Игра начинается!")
game_continue()

for x in range(1,11):
    if x % 2 != 0 and x <= 9:
        move_x()
        if x >=5:
            check_vin()
            if check_vin():
                print("Игра окончена! Выиграли крестики")
                break
    elif x % 2 == 0 and x <= 9:
        move_o()
        if x >= 6:
            check_vin()
            if check_vin():
                print("Игра окочена! Выиграли нолики")
                break
    else:
        print("Ничья... Играть научитесь")
	


