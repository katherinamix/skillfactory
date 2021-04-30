board = list(range(1, 10))
x = 'X'
o = 'O'


# Функция отрисовки ячеек. Значения ячеек от 1 до 9 - для удобства игроку ставить свой знак
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


# Игрок выбирает очередность. Если выбирает "да", то начинает первым. Первыми, как правило, играют крестиками
def choiceFirstStep():
    choice = ""
    while choice not in ('да', 'нет'):
        print('Скажи "да" или "нет":  ')
        choice = input().lower()
    if choice == 'да':
        print('Ты первый, значит играешь крестиками - X')
        player = x
        comp = o
    else:
        print('Понятно, ты предоставил первый ход профессионалу, играешь ноликами - O')
        player = o
        comp = x
    return player, comp


# Проверка на пустоту интересуемой ячейки, т.е. в ней не хранятся переменные X или O
def isCellEmpty(board, step):
    return str(board[step]) not in (x, o)


# Проверка победиля
def checkWinner(board):
    # listCheck - кортеж с индексами выигрышных кобминаций
    listCheck = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2))
    for i in listCheck:
        # Проверяем каждую комбинацию в сетке на равенство значений
        if board[i[0]] == board[i[1]] == board[i[2]]:
            winner = board[i[0]]
            return winner
    return False


# Ход игрока
def inputPlayer(board, player_symbol):
    step = 0
    valid = False
    # Будем выполнять, пока не пройдем все проверки
    while not valid:
        step = input('Напиши номер ячейки (1-9): ')
        # Проверка число ли ввели или что-то другое
        if not step.isdigit():
            print('Некорректный ввод!')
            continue
        else:
            step = int(step)
            # Проверка на диапазон от 1 до 9
            if step not in range(1, 10):
                print('Некорректный диапазон!')
            else:
                # Проверка на занятую ячейку
                if not isCellEmpty(board, step - 1):
                    print('Ячейка занята! Выбери другую')
                else:
                    # Ход игрока засчитан
                    board[step - 1] = player_symbol
                    # Проверки пройдены
                    valid = True


# Проверка на наличие свободных ячеек
def fullBoard(board):
    for i in range(0, 9):
        if isCellEmpty(board, i):
            return False
    return True


# Собираем список пустых ячеек для хода компьютера
def emptyCells(board):
    cells = []
    for i in range(0, 9):
        if str(board[i]) not in (x, o):
            cells.append(i)
    return cells


# Ход компьютера
def inputComp(board, comp_symbol):
    # Получаем символ игрока в зависимости от символа компьютера
    if comp_symbol == x:
        player_symbol = o
    else:
        player_symbol = x
    # Если компьютер может выиграть следующим ходом, то выбираем именно этот ход
    for cell in emptyCells(board):
        # Получаем копию рабочей сетки для внутренних махинаций компьютера
        board_copy = board[:]
        board_copy[cell] = comp_symbol
        if checkWinner(board_copy):
            return cell
    # Если игрок может выиграть следующим ходом, то выбираем именно этот ход, чтоюы не дать ему выиграть
    for cell in emptyCells(board):
        board_copy = board[:]
        board_copy[cell] = player_symbol
        if checkWinner(board_copy):
            return cell

    # Выбираем центральную ячейку как преимущество (если она пустая)
    if isCellEmpty(board, 4):
        return 4
    # Если ничего не остается, то дадим человеку шанс выиграть и ставим в любую свободную ячейку
    for cell in emptyCells(board):
        return cell


print("""Добро пожаловать в игру Крестики-нолики!
Для того, чтобы сделать ход, надо ввести номер ячейки от 1 до 9.
Твоим соперником будет компьютер. Ты хочешь первым начать игру (ответь "да" или "нет")?
""")


# Главная программа
def main(board):
    player_symbol, comp_symbol = choiceFirstStep()
    priority = x
    # Флаг окончания игры
    endGame = False
    draw_board(board)
    while not endGame:
        if priority == player_symbol:  # ход игрока
            print('Твой ход!')
            inputPlayer(board, player_symbol)
            draw_board(board)
            if checkWinner(board):
                draw_board(board)
                print('На этот раз ты победил!!!')
                endGame = True
            else:
                if fullBoard(board):
                    draw_board(board)
                    print('Ничья!')
                    break
                else:
                    priority = comp_symbol
        else:  # ход компьютера
            print('Ходит компьютер... ' + str(board[inputComp(board, comp_symbol)]))
            board[inputComp(board, comp_symbol)] = comp_symbol
            draw_board(board)
            if checkWinner(board):
                draw_board(board)
                print('Компьютер победил!!!')
                endGame = True
            else:
                if fullBoard(board):
                    draw_board(board)
                    print('Ничья!')
                    break
                else:
                    priority = player_symbol
    print('Конец!')


# Запускаем игру
main(board)
