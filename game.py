'''
Tic-Tac-Toe: A Solution
Author: Jared Martinez
'''

def main():
    print("\nWelcome to Tic-Tac-Toe on Python!")
    player = next_player("")
    board = create_board()
    while not (win(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    answer = input("That was an awesome game! Do you want to play again? ([Y]es / [N]o): ")
    if answer == "Y":
        main()
    elif answer == "N":
        print("Alright, thanks for playing! :)\n")

def create_board():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def draw(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True 
    
def win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    i = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[i - 1] = player

def next_player(current):
    if current == "" or current == "\033[96mo\033[00m":
        return "\033[91mx\033[00m"
    elif current == "\033[91mx\033[00m":
        return "\033[96mo\033[00m"

if __name__ == "__main__":
    main()