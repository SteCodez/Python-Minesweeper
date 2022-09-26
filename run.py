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
   
        self.bomb_num
        self.board_size
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
        board = [[None for _ in range(self.board_size)] for _ in range(self.dim_size)]
        """
        planting bombs
        """
def play(board_size= 20, bomb_num=20):


    
    
    play()
get_user_name()  