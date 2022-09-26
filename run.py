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
        self.board_sze = board_sze
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
                #bomb already there so continue on with loop
                continue
           
            board[row][col] == '*' #plants the bomb
            bombs_planted += 1
        
        return board    
     
    def assign_values(self):
        for c in range(self.board_sze):
            for r in range(self.board_sze):
                if self.Game_board[r][c] == '*':
                    continue
                self.Game_board[r][c] = self.highlight_adjacent_bombs(r, c)
    
    
    def highlight_adjacent_bombs(self, row, col):
        
        bombs_beside = 0
        for r in range (max(0, row-1), min(self.board_sze-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_sze-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.Game_board[r][c] == '*':
                    bombs_beside += 1
        
        return bombs_beside
        
            
def play(board_sze= 20, bomb_num=20):
    


    
    
    play()
get_user_name()  
