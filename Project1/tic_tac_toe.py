# импорт модуля рандома
from random import choice

def draw_board(board):
    print(" ..... ..... ..... ")
    for i in range(3):
        print("   " + board[0 + i * 3] + "  :  " + board[1 + i * 3] + "  :  " + board[2 + i * 3] + "   ")
        print(" ..... ..... ..... ")

def get_player_move(board, figure, options, name):
    print("Укажите номер клетки, на которую вы хотите походить. Вы можете ввести 0, чтобы сдаться.")
    print(name + ', ', end='')
    move = input("ваш ход: ")
    while move not in '1234567890' or (move not in options and move != '0'):
        move = input("Эта клетка недоступна, введите новую: ")
    if int(move) == 0:
        return 0, options
    else:
        board[int(move) - 1] = figure
        options.remove(move)
        return board, options


def get_computer_move(board, figure, options, name):
    move = choice(tuple(options))
    options.remove(move)
    board[int(move) - 1] = figure
    return board, options

def check_win(board):
    for i in range(3):
        if len(set([board[i * 3], board[i * 3 + 1], board[i * 3 + 2]])) == 1:
            return board[i * 3]
        if len(set([board[i], board[i + 3], board[i + 6]])) == 1:
            return board[i]
    if len(set([board[0], board[4], board[8]])) == 1 or len(set([board[2], board[4], board[6]])) == 1:
        return board[4]
    return


def main(p1, p2, user1, user2):
    moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    free_cells = set("123456789")
    id = 1
    while not check_win(moves) and len(free_cells) > 0:
        if id % 2 == 1:
            moves, free_cells = p1(moves, 'x', free_cells, user1)
            if moves == 0:
                print(f"{user1} сдался, победитель - {user2}")
                return
            print(f"{user1} сделал ход.")
            draw_board(moves)
        else:
            moves, free_cells = p2(moves, '0', free_cells, user2)
            if moves == 0:
                print(f"{user2} сдался, победитель - {user1}")
                return
            print(f"{user2} сделал ход.")
            draw_board(moves)
        id += 1
    result = check_win(moves)
    if result == 'x':
        print(f"{user1} победил!")
    elif result == "0":
        print(f"{user2} победил!")
    else:
        print("Ничья!")


answer = input("Вы будете играть с человеком(1) или с компьютером(2)? ")
while answer != '1' and answer != '2':
    answer = input("Вам следует ввести '1' для игры с человеком или же '2' для игры с компьютером(2): ")
if answer == '2':
    player1 = choice([get_computer_move, get_player_move])
    name1 = "Игрок" if player1 == get_player_move else "Компьютер"
    player2 = get_computer_move if player1 == get_player_move else get_player_move
    name2 = "Игрок" if name1 == "Компьютер" else "Компьютер"
if answer == '1':
    player1, player2 = get_player_move, get_player_move
    name1, name2 = input("Введите имя первого игрока: "), input("Введите имя второго игрока: ")
again = '1'
while again == '1':
    main(player1, player2, name1, name2)
    again = input("Введите '1', чтобы сыграть снова: ")
    player1, player2 = player2, player1
    name1, name2 = name2, name1