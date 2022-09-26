import random

def get_user_name():
        """
        Gets user name.
        """
        print("Welcome to Minesweeper! Watch your step!")
        name_str = input("Enter your name here: ")
    
        print(f"Best of luck {name_str}!")
        
class Game_board:
    def __init__(self, bomb_num, board_sze):
   
        self.bomb_num = bomb_num
        self.board_size = board_sze
        """
        The board Game_board class allows us to easily replicate objects using OOP tools.
        """
        self.board = self.make_board()
        self.assign_values()
        """
        adding an empty set that we will use to store which locations we 
        have already dug for bombs using tuples (row, col)
        """
        self.already_dug = ()
        
    def generate_new_board(self):
        """
        generates a board by defined dimenion size.
        """
        board = [[None for _ in range(self.board_sze)] for _ in range(self.board_sze)]
        """
        planting bombs by using an equation to return random intergers
        """
        bombs_plnted = 0
        while bombs_plnted < self.bomb_num:
            loc = random.randint(0, self.board_sze**2 - 1)
            row = loc // self.board_sze
            col = loc % self.board_sze
            
            if board[row][col] == '*':
                continue
           
            board[row][col] == '*'
            bombs_planted += 1
        
        return board    
            
def play(board_sze= 20, bomb_num=20):


    
    
    play()
get_user_name()  
