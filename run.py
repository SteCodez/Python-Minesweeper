import random

def get_user_name():
        """
        Gets user name.
        """
        print("Welcome to Minesweeper! Watch your step!")
        name_str = input("Enter your name here: ")
    
        print(f"Best of luck {name_str}!")
        
class Game:
    def __init__(self, bomb_num, game_sze):
   
        self.bomb_num = bomb_num
        self.game_sze = game_sze
        """
        The game Game_game class allows us to easily replicate objects using OOP tools.
        """
        self.game = self.make_game()
        self.assign_values()
        """
        adding an empty set that we will use to store which locations we 
        have already dug for bombs using tuples (row, col)
        """
        self.already_dug = ()
        
    def generate_new_game(self):
        """
        generates a game by defined dimenion size.
        """
        game = [[None for _ in range(self.game_sze)] for _ in range(self.game_sze)]
        """
        planting bombs by using an equation to return random intergers
        """
        bombs_plnted = 0
        while bombs_plnted < self.bomb_num:
            loc = random.randint(0, self.game_sze**2 - 1)
            row = loc // self.game_sze
            col = loc % self.game_sze
            
            if game[row][col] == '*':
                #bomb already there so continue on with loop
                continue
           
            game[row][col] == '*' #plants the bomb
            bombs_planted += 1
        
        return game    
     
    def assign_values(self):
        for c in range(self.game_sze):
            for r in range(self.game_sze):
                if self.Game[r][c] == '*':
                    continue
                self.Game[r][c] = self.highlight_adjacent_bombs(r, c)
    
    def highlight_adjacent_bombs(self, row, col):
        """
         iterating through adjacent positions, making sure not to go out of bounds by using rhe min and max.
        """  
        bombs_beside = 0
        for r in range (max(0, row-1), min(self.game_sze-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_sze-1, col+1)+1):
                if r == row and c == col:
                    
                    continue
                if self.Game_game[r][c] == '*':
                    bombs_beside += 1
    
        return bombs_beside
    
    def search(self, row, col):
        self.search.add((row,col))
        
        if self.game[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        """
        This function keeps track of what we have searched. Using repeat logic
        """
        for r in range (max(0, row-1), min(self.game_sze-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_sze-1, col+1)+1):
                if (r, c) in self.search:
                    continue
                self.search(r, c)
        
        return True
        
def __str__(self):
    shown_board = [[None for _ in range(self.game_sze)] for _ in range(self.game_sze)]
    for row in range (self.game_sze):
        for col in range(self.game_sze):
            if (row, col) in self.already.dug:
                shown_board[row][col] = str(self.game[row][col])
            else:
                shown_board[row][col] = ' '
                   
def play(game_sze= 20, bomb_num=20):
     game = Game(game_sze, bomb_num)
     
     while len(game.search) < game.game_sze ** 2 - bomb_num:
         print(game)
         user_input
   
play()
  
get_user_name()  
