import random
import re

def get_user_name():
        """
        Gets user name.
        """
        print("Welcome to Minesweeper! Watch your step!")
        name_str = input("Enter your name here: ")
    
        print(f"Best of luck {name_str}!")
        
class Game:
    def __init__(self, bomb_num, board_dim):
   
        self.bomb_num = bomb_num
        self.board_dim = board_dim
        """
        The game  class allows us to easily replicate objects using OOP tools.
        """
        self.game = self.generate_new_game()
        self.assign_values()
        """
        adding an empty set that we will use to store which locations we 
        have already search for bombs using tuples (row, col)
        """
        self.already_search = ()
        
    def generate_new_game(self):
        """
        generates a game by defined dimenion size.
        """
        game = [[None for _ in range(self.board_dim)] for _ in range(self.board_dim)]
        """
        planting bombs by using an equation to return random intergers
        """
        bombs_plnted = 0
        while bombs_plnted < self.bomb_num:
            loc = random.randint(0, self.board_dim**2 - 1)
            row = loc // self.board_dim
            col = loc % self.board_dim
            
            if game[row][col] == '*':
                #bomb already there so continue on with loop
                continue
           
            game[row][col] == '*' #plants the bomb
            bombs_plnted += 1
        
        return game    
     
    def assign_values(self):
        for c in range(self.board_dim):
            for r in range(self.board_dim):
                if self.game[r][c] == '*':
                    continue
                self.game[r][c] = self.highlight_adjacent_bombs(r, c)
    
    def highlight_adjacent_bombs(self, row, col):
        """
         iterating through adjacent positions, making sure not to go out of bounds by using rhe min and max.
        """  
        bombs_beside = 0
        for r in range (max(0, row-1), min(self.board_dim-1, row+1)+1):
            for c in range(max(0, col-1), min(self.board_dim-1, col+1)+1):
                if r == row and c == col:
                    
                    continue
                if self.game[r][c] == '*':
                    bombs_beside += 1
    
        return bombs_beside
    
    def search(self, row, col):
        self.already_search.add((row,col))
        
        if self.game[row][col] == '*':
            return False
        elif self.game[row][col] > 0:
            return True
        """
        This function keeps track of what we have searched. Using repeat logic
        """
        for r in range (max(0, row-1), min(self.board_dim-1, row+1)+1):
            for c in range(max(0, col-1), min(self.board_dim-1, col+1)+1):
                if (r, c) in self.already_search:
                    continue
                self.already_search(r, c)
        
        return True
        
    def __str__(self):
        """
        The below code creates a new array that represents what the user will see.
        """
        shown_board = [[None for _ in range(self.board_dim)] for _ in range(self.board_dim)]
        for row in range (self.board_dim):
            for col in range(self.board_dim):
                if (row, col) in self.already_search:
                    shown_board[row][col] = str(self.game[row][col])
                else:
                    shown_board[row][col] = ' '
                   
        string_rep = ''
                  
        # get max column widths for printing
        widths = []
        for idx in range(self.board_dim):
            columns = map(lambda x: x[idx], shown_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # printing the csv strings
        indices = [i for i in range(self.board_dim)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(shown_board)):
            row = shown_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.board_dim)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
               
def play(board_dim=10, bomb_num=10):
    game = Game(board_dim, bomb_num)
     
    safe = True
     
    while len(game.already_search) < game.board_dim ** 2 - bomb_num:
        print(game)
        user_input = re.split (',(\\s)', input("Choose your dig site! Choose well! Format as row, col:"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board_dim or col < 0 or col >= board_dim:
            print("Ooopsie, Try Again!")
            continue
        safe = game.already_search(row, col)
        if not safe:
            break
        
    if safe:
        print("You did it!! Well done :)")
    else:
        print("GAME OVER!!! :( ")
         
    print(game)
    
def main():
 
    get_user_name()  
    play()
    
main()