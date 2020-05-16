import random
import pygame
import time

def create_board():
    return([['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']])

def make_play(board, row, col,token):
    board[row][col] = token
    
#checks if the user chose a valid slot to make the play
def is_valid_play(board, row, col):
    if board[row][col] == '_':
        return True
    else:
        return False
    
def user_turn(board, row, col):
    if is_valid_play(board, row, col):
        make_play(board, row, col, 'X')
        return True
    else:
        return False
        
def pc_turn(board):
    poss = []
    for row, items in enumerate(board):
        for col, item in enumerate(items):
            if item=='_':
                poss.append([row, col])
    row, col = random.choice(poss)
    make_play(board, row, col, 'O')
    return row, col
    
def check_win(board, token):
    if row_check(board, token) or col_check(board, token) or diag_check(board, token):
        return True
    return False

#checks for a complete row 
def row_check(board, token):
    for row in board:
        result = True
        for item in row:
            if item != token:
                result = False
                break
        if result == True:
            return True
    return False

#checks for a complete column
def col_check(board, token):
    for row in range(len(board)):
        result = True
        for col in range(len(board)):
            if board[col][row] !=token:
                result = False
                break
        if result == True:
            return True
    return False

#checks for a complete diagonal
def diag_check(board, token):
    px, py = 0, 0
    result = True
    for _ in range(len(board)):
        if board[px][py] != token:
            result = False
            break
        px+=1
        py+=1
    if result == True:
        return True
    px = len(board)-1
    py = 0
    for _ in range(len(board)):
        if board[px][py] != token:
            result = False
            break
        px-=1
        py+=1
    if result == True:
        return True
    return False
        
#driver code
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Tic- Tac- Toe")

chars = pygame.font.Font('Fipps-Regular.otf', 50)
res_font = pygame.font.Font('Fipps-Regular.otf', 30)

def start_seq():
    board = create_board()
    curr_player = random.choice(['X', 'O'])
    line1_coords = [(100, 200), (400, 200)]
    line2_coords = [(100, 300), (400, 300)]
    line3_coords = [(200, 100), (200, 400)]
    line4_coords = [(300, 100), (300, 400)]

    screen.fill((0,0,255))
    pygame.draw.aalines(screen, (0,255,0), False, line1_coords)
    pygame.draw.aalines(screen, (0,255,0), False, line2_coords)
    pygame.draw.aalines(screen, (0,255,0), False, line3_coords)
    pygame.draw.aalines(screen, (0,255,0), False, line4_coords)
    pygame.display.update()

    return board, curr_player, False

board, curr_player, win = start_seq()

while win == False:
    save_curr_player = curr_player

    if curr_player == 'X':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        mouse = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        if mouse_press[0] == 1:
            if mouse[0] < 200:
                if mouse[1] < 200:
                    x, y = 0, 0
                elif mouse[1] > 200 and mouse[1] < 300:
                    x, y = 0, 1
                elif mouse[1] > 300:
                    x, y = 0, 2
            elif mouse[0] > 200 and mouse[0] < 300:
                if mouse[1] < 200:
                    x, y = 1, 0
                elif mouse[1] > 200 and mouse[1] < 300:
                    x, y = 1, 1
                elif mouse[1] > 300:
                    x, y = 1, 2
            elif mouse[0] > 300:
                if mouse[1] < 200:
                    x, y = 2, 0
                elif mouse[1] > 200 and mouse[1] < 300:
                    x, y = 2, 1 
                elif mouse[1] > 300:
                    x, y = 2, 2
            if user_turn(board, x, y):
                screen.blit(chars.render('X', True, (255,255,0)), [(100 * (x+1)) + 25, (100 * (y+1))])
                pygame.display.update()
                curr_player = 'O'
            else:
                curr_player = 'X'
        else: 
            continue

    elif curr_player == 'O':
        x, y = pc_turn(board)
        screen.blit(chars.render('O', True, (255,255,0)), [(100 * (x+1)) + 25, (100 * (y+1))])
        pygame.display.update()
        curr_player = 'X'
    win = check_win(board, save_curr_player)

    if win:
        player_dict = {'X':"You", 'O':"PC"}
        screen.blit(res_font.render(player_dict[save_curr_player]+" won!!", True, (255, 255, 0)), [120, 415])
        pygame.display.update()
        time.sleep(3)
        board, curr_player, win = start_seq()