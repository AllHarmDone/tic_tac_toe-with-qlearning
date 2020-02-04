import time
from random import randint
#qlearning
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
from itertools import product
import threading as thread


EMTYBOARD=['','',''],['','',''],['','','']
board=['','',''],['','',''],['','','']

def printBoard(board):
    board
    print('\n',
        board[0][0],"|", board[0][1],"|", board[0][2],'\n',
        "-.--.-",'\n',
        board[1][0],"|", board[1][1],"|", board[1][2],'\n',
        "-.--.-", '\n',
        board[2][0],"|", board[2][1],"|", board[2][2]
        )

def winner():
    global board
    colums = [board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]],[board[0][2],board[1][2],board[2][2]]
    for rows in board:
        if rows.count('x')== 3:
            return 'win_x'
        if rows.count('o')== 3:
            return 'win_o'
    for colum in colums:
        if colum.count('x')== 3:
            return 'win_x'
        if colum.count('o')== 3:
            return 'win_o'
    #diagonal
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        return 'win_x'
    if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        return 'win_o'
    #other diagonal
    if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        return 'win_x'
    if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        return 'win_o'
    if board[0].count("") == 0 and board[1].count("") == 0 and board[2].count("") == 0:
        return 'tie'
    else:
        return False

def user_move(board):
    print("where do you want to place your x")
    movedone=False
    while movedone!=True:
        inp = int(input())
        if inp <=3:
            if board[0][inp-1] == '':
                board[0][inp-1]='x'
                movedone=True
                return board
            else:
                print("not viable")
        elif inp >=4 and inp<=6:
            if board[1][inp-4] == '':
                board[1][inp-4]='x'
                movedone=True
                return board
            else:
                print("not viable")
        elif inp >=7 and inp <=9:
            if board[2][inp-7] == '':
                board[2][inp-7]='x'
                movedone=True
                return board
            else:
                print("not viable")
        else:
            print("not viable")
def ai_move(move):
    movedone=False
    while movedone!=True:
        inp = move
        if inp <=3:
            if board[0][inp-1] == '':
                board[0][inp-1]='x'
                movedone=True
                return board
            else:
                print("not viable", move)
                break
        elif inp >=4 and inp<=6:
            if board[1][inp-4] == '':
                board[1][inp-4]='x'
                movedone=True
                return board
            else:
                print("not viable", move)
                break
        elif inp >=7 and inp <=9:
            if board[2][inp-7] == '':
                board[2][inp-7]='x'
                movedone=True
                return board
            else:
                print("not viable", move)
                break
        else:
            break

def computer_move(board,show=True):
    #comp is 'o'
    corners= board[0][0],board[0][2],board[2][0],board[2][2]
    sides=board[0][1],board[1][0],board[1][2],board[2][1]
    middle=board[1][1]
    colums = [board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], \
        [board[0][2],board[1][2],board[2][2]]
    #winning move
    for rows in board:
        if rows.count('o') == 2 and rows.count("") == 1:
            board[board.index(rows)][board[board.index(rows)].index("")]='o'
            return board
    for colum in colums:
        if colum.count('o') == 2 and colum.count("") == 1:
            board[colums[colums.index(colum)].index("")][colums.index(colum)]='o'
            return board
    diagonalLeft=board[0][0],board[1][1],board[2][2]
    if diagonalLeft.count('o') == 2 and diagonalLeft.count("") == 1:
        if board[0][0] == "":
            board[0][0]='o'
            return board
        if board[1][1] == "":
            board[1][1]='o'
            return board
        if board[2][2] == "":
            board[2][2]='o'
            return board
    diagonalRight = board[0][2], board[1][1], board[2][0]
    if diagonalRight.count('o') == 2 and diagonalRight.count("") == 1:
        if board[0][0] == "":
            board[0][0]='o'
            return board
        if board[1][1] == "":
            board[1][1]='o'
            return board
        if board[2][2] == "":
            board[2][2]='o'
            return board
    #blocking move
    for rows in board:
        if rows.count('x') == 2 and rows.count("") == 1:
            board[board.index(rows)][board[board.index(rows)].index("")]='o'
            if show==True:
                print("computer is blocking you")
            return board
    for colum in colums:
        if colum.count('x') == 2 and colum.count("") == 1:
            board[colums[colums.index(colum)].index("")][colums.index(colum)]='o'
            return board
    diagonalLeft=board[0][0],board[1][1],board[2][2]
    if diagonalLeft.count('x') == 2 and diagonalLeft.count("") == 1:
        if board[0][0] == "":
            board[0][0]='o'
            if show == True:
                print("computer is blocking you")
            return board
        if board[1][1] == "":
            board[1][1]='o'
            if show == True:
                print("computer is blocking you")
            return board
        if board[2][2] == "":
            board[2][2]='o'
            if show == True:
                print("computer is blocking you")
            return board
    diagonalRight = board[0][2], board[1][1], board[2][0]
    if diagonalRight.count('x') == 2 and diagonalRight.count("") == 1:
        if board[0][2] == "":
            board[0][2]='o'
            return board
        if board[1][1] == "":
            board[1][1]='o'
            return board
        if board[2][0] == "":
            board[2][0]='o'
            return board
    #corner pick
    if "" in corners:
        if corners.count("") == 4:
            loc=randint(0,3)
            if loc == 0:
                board[0][0]='o'
                return board
            elif loc == 1:
                board[0][2] = 'o'
                return board
            elif loc == 2:
                board[2][0] = 'o'
                return board
            else:
                board[2][2]
                return board
        if corners.count("") == 3:
            next = False
            while next != True:
                loc = randint(0, 3)
                if corners[loc] =="":
                    if loc == 0:
                        board[0][0] = 'o'
                        return board
                        break
                    elif loc == 1:
                        board[0][2] = 'o'
                        return board
                        break
                    elif loc == 2:
                        board[2][0] = 'o'
                        return board
                        break
                    else:
                        board[2][2] = 'o'
                        return board
                        break
        next = False
        while next != True:
            loc = randint(0, 3)
            if corners[loc] == "":
                if loc == 0:
                    board[0][0] = 'o'
                    return board
                    break
                elif loc == 1:
                    board[0][2] = 'o'
                    return board
                    break
                elif loc == 2:
                    board[2][0] = 'o'
                    return board
                    break
                else:
                    board[2][2] = 'o'
                    return board
                    break
    #middle
    if middle == "":
        board[1][1] = 'o'
        return board
    #sides
    if sides.count("") >=1:
        while True:
            loc = randint(0, 4)
            if loc == 1 and board[0][1] == "":
                board[0][1] = "o"
                return board
            if loc == 2 and board[1][0] == "":
                board[0][1] = "o"
                return board
            if loc == 3 and board[1][2] == "":
                board[0][1] = "o"
                return board
            if loc == 4 and board[2][1] == "":
                board[0][1] = "o"
                return board

    print("computer did not move",'\n',board)
    time.sleep(3)
    return board
def new_game():
    print('new game? press y for yes and n for no:')
    new_Game=False
    next = False
    while next == False:
        inp = input()
        if inp == 'y':
            new_Game=True
            next = True
        elif inp == 'n':
            new_Game=False
            next =True
        else:
            print('did not understand your choice')
    return new_Game

def main():
    global board
    global colums
    print("start user is x and computer is o")
    won=False
    while won != True:
        printBoard(board)
        print('x is up:')
        board=user_move(board)
        #colums might be needed
        winning=winner()
        if winning != False:
            board = ['','',''],['','',''],['','','']
            if winning == 'win_x':
                print("user wins! after input")
                n = new_game()
                if n == True:
                    continue
                else:
                    exit()
                    break
            elif winning == 'win_o':
                print("computer wins")
                n = new_game()
                if n == True:
                    continue
                else:
                    exit()
                    break
            elif winning == 'tie':
                print("tie")
                n = new_game()
                if n == True:
                    continue
                else:
                    exit()
                    break
        board=computer_move(board)
        print("computers move:")
        printBoard(board)
        winning=winner()
        if winning != False:
            board = ['','',''],['','',''],['','','']
            if winning == 'win_x':
                print("user wins!")
                n=new_game()
                if n == True:
                    continue
                else:
                    exit()
                    break
            elif winning == 'win_o':
                print("computer wins")
                n = new_game()
                if n == True:
                    continue
                else:
                    exit()
                    break
            elif winning == 'tie':
                print("tie")
                n = new_game()
                if n == True:
                    continue
                else:
                    exit()
                    break

"""
while True:
    main()
"""
def plot(array):
    plt.plot(array)
    plt.ylabel(f"Reward {SHOW_EVERY}ma")
    plt.xlabel("episode #")
    plt.show()
#AI LEARING
HM_EPISODES = 25000
MOVE_PENALTY = 1
FILLED_SPACE_PENALTY = 100
LOSING_PENALTY = 10
WINNING_REWARD = 10
TIE=0

epsilon = 0.9
EPS_DECAY = 0.9998

SHOW_EVERY=10000

start_q_table = None # or filename

LEARNING_RATE = 0.1
DISCOUNT = 0.95

delay=0.4
if start_q_table is None:
    q_table = {}
    res = [ele for ele in product(["", "o", "x"], repeat=9)]
    for pos in range(len(res)):
        q_table[(res)[pos]]=[np.random.uniform(-5, 0) for i in range(9)]

else:
    with open(start_q_table, "rb") as f:
        q_table=pickle.load(f)

episode_rewards=[]
avg_reward=[]
for episode in range(HM_EPISODES):
    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True
    else:
        show = False
    won=False
    board = ['', '', ''], ['', '', ''], ['', '', '']
    #print("\033[1;30;47m","episode number", episode)
    if show == True:
        print("new episode")
    while won!=True:
        reward = None
        obs =(board[0][0],board[0][1],board[0][2],
              board[1][0],board[1][1],board[1][2],
              board[2][0],board[2][1],board[2][2])
        if np.random.random() > epsilon:
            #q_Ai action?
            action= np.argmax(q_table[obs])
            if show == True:
                print("regular action",action+1)
                time.sleep(delay)
        else:
            action = np.random.randint(0,9)
            if show == True:
                print("random action",action+1,":")
                time.sleep(delay)
        if action == 0 and board[0][0] == "":
            if show==True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 1 and board[0][1] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 2 and board[0][2] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 3 and board[1][0] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 4 and board[1][1] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 5 and board[1][2] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 6 and board[2][0] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 7 and board[2][1] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        elif action == 8 and board[2][2] == "":
            if show == True:
                print("\033[1;32;40m action is possible")
                time.sleep(delay)
        else:
            if show == True:
                print("\033[1;31;40m action not plossible", action+1)
                time.sleep(delay)
            reward= -FILLED_SPACE_PENALTY
        winning = winner()
        if winning == False and reward != -FILLED_SPACE_PENALTY:
            board = ai_move(action+1)
            if show == True:
                print("ai move:")
                printBoard(board)
                time.sleep(delay)
        winning = winner()
        if winning != False:
            board = ['', '', ''], ['', '', ''], ['', '', '']
        if winning == 'win_x':
            if show == True:
                print("Ai wins! after input")
                time.sleep(delay)
            reward=WINNING_REWARD
        elif winning == 'win_o':
            if show == True:
                print("computer wins")
                time.sleep(delay)
            reward=LOSING_PENALTY
        elif winning == 'tie':
            if show == True:
                print("tie")
                time.sleep(delay)
            reward = TIE
        if winning == False and reward != -FILLED_SPACE_PENALTY:
            board = computer_move(board,show)
            if show == True:
                print("computers move:")
                printBoard(board)
                time.sleep(delay)
        winning = winner()
        if winning != False:
            board = ['', '', ''], ['', '', ''], ['', '', '']
        if winning == 'win_x':
            if show == True:
                print("AI wins!",episode)
                time.sleep(delay)
            reward = WINNING_REWARD
        elif winning == 'win_o':
            if show == True:
                print("computer wins",episode)
                time.sleep(delay)
            reward = -LOSING_PENALTY
        elif winning == 'tie':
            if show == True:
                print("tie",episode)
                time.sleep(delay)
            reward = TIE

        new_obs=(board[0][0],board[0][1],board[0][2],
              board[1][0],board[1][1],board[1][2],
              board[2][0],board[2][1],board[2][2])
        max_future_q = np.max(q_table[new_obs])
        current_q = q_table[obs][action-1]

        if reward == WINNING_REWARD:
            new_q = WINNING_REWARD
        if reward == -FILLED_SPACE_PENALTY:
            new_q = -FILLED_SPACE_PENALTY
        if reward == -LOSING_PENALTY:
            new_q = -LOSING_PENALTY
        if reward == TIE:
            new_q = TIE
        else:
            if reward == None:
                reward=0
                new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
                reward=None
        q_table[obs][action]= new_q
        if reward == TIE or reward == -LOSING_PENALTY or reward == WINNING_REWARD:
            episode_rewards.append(reward)
            if show == True:
                print("the game is over")
                time.sleep(delay)
            break
    if episode == HM_EPISODES-1:
        print("I'm done my lord...")
    epsilon *=EPS_DECAY
    avg_reward.append(sum(episode_rewards)/len(episode_rewards))
    #if len(avg_reward) >= 10:
        #run=thread.Thread(target=plot(avg_reward),daemon=True)
        #run.start()
plot(avg_reward)
#epsilon in not decreasing?
#doesnt seem to learn...?
#length Q table?, should be adressed
with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)