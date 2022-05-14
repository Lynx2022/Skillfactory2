game = [[" ", "1", "2", "3"],
        ["1", "x", "x", "x"],
        ["2", "-", "-", "-"],
        ["3", "-", "-", "x"]
       ]

def check_vin():
    comb_vin = [all(game[1][1],game[1][2],game[1][3])=="x",
                game[2][1]==game[2][2]==game[2][3]=="x",
                game[3][1]==game[3][2]==game[3][3]=="x",
                game[1][1]==game[2][1]==game[3][1]=="x",
                game[1][2]==game[2][2]==game[3][2]=="x",
                game[1][3]==game[2][3]==game[3][3]=="x",
                game[1][1]==game[2][2]==game[3][3]=="x",
                game[1][3]==game[2][2]==game[3][1]=="x",
                game[1][1] == game[1][2] == game[1][3] == "o",
                game[2][1] == game[2][2] == game[2][3] == "o",
                game[3][1] == game[3][2] == game[3][3] == "o",
                game[1][1] == game[2][1] == game[3][1] == "o",
                game[1][2] == game[2][2] == game[3][2] == "o",
                game[1][3] == game[2][3] == game[3][3] == "o",
                game[1][1] == game[2][2] == game[3][3] == "o",
                game[1][3] == game[2][2] == game[3][1] == "o"
                ]
    if any(comb_vin):
        print("есть")
    else:
        print("нет")
check_vin()