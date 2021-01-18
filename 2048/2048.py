import pygame
import pygame_menu
import tkinter as tk
import colors as co
import random

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.main_grid = tk.Frame(
            self, bg = co.GRID_COLOR, bd = 3, width = 400, height = 400
        )
        self.main_grid.grid(pady = (100,0))
        self.make_GUI()
        self.start_2048()

        self.master.bind("<Left>",self.move_left)
        self.master.bind("<Right>",self.move_right)
        self.master.bind("<Up>",self.move_up)
        self.master.bind("<Down>",self.move_down)

        self.mainloop()
    
    def make_GUI(self):
        #grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=co.EMPTY_CELL_COLOR,
                    width=100,
                    height=100)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=co.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        #score_header
        score_frame = tk.Frame(self)
        score_frame.place(relx = 0.5, y = 40, anchor = "center")
        tk.Label(
            score_frame,
            text = "Score",
            font = co.SCORE_LABEL_FONT
        ).grid(row = 0)
        self.score_label = tk.Label(score_frame,text ="0",font = co.SCORE_FONT)
        self.score_label.grid(row = 1)

    def start_2048(self):
        #create matrix
        self.matrix = [[0]*4 for _ in range(4)]

        #fill 2 random cells with 2s
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg = co.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg = co.CELL_COLORS[2],
            fg = co.CELL_NUMBER_COLORS[2],
            font = co.CELL_NUMBER_FONTS[2],
            text = 2 #ADD PICS HERE IF YOU WANT 
        )

        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=co.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=co.CELL_COLORS[2],
            fg=co.CELL_NUMBER_COLORS[2],
            font=co.CELL_NUMBER_FONTS[2],
            text="2")

        self.score = 0

    #Matrix Manipulation
    def stack(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix
    
    def sum_up(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j+1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] = 0
                    self.score += self.matrix[i][j]

    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    #Add a new 2 or 4 tile
    def generate_tile(self):
        #fill 2 random cells with 2s
        if any(0 in row for row in self.matrix):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            while(self.matrix[row][col] != 0):
                row = random.randint(0, 3)
                col = random.randint(0, 3)
            self.matrix[row][col] = random.choice([2,4])
    
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_val = self.matrix[i][j]
                if cell_val == 0:
                    self.cells[i][j]["frame"].configure(bg = co.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg = co.EMPTY_CELL_COLOR,text = "")
                else:
                    self.cells[i][j]["frame"].configure(bg = co.CELL_COLORS[cell_val])
                    self.cells[i][j]["number"].configure(
                        bg=co.CELL_COLORS[cell_val],
                        fg=co.CELL_NUMBER_COLORS[cell_val],
                        font=co.CELL_NUMBER_FONTS[cell_val],
                        text=str(cell_val)
                    )
        self.score_label.configure(text = self.score)
        self.update_idletasks()

    #ARROW FUNCTIONS
    def move_left(self, event):
        self.stack()
        self.sum_up()
        self.stack()
        self.generate_tile()
        self.update_GUI()
        self.is_game_over()


    def move_right(self, event):
        self.reverse()
        self.stack()
        self.sum_up()
        self.stack()
        self.reverse()
        self.generate_tile()
        self.update_GUI()
        self.is_game_over()


    def move_up(self, event):
        self.transpose()
        self.stack()
        self.sum_up()
        self.stack()
        self.transpose()
        self.generate_tile()
        self.update_GUI()
        self.is_game_over()


    def move_down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.sum_up()
        self.stack()
        self.reverse()
        self.transpose()
        self.generate_tile()
        self.update_GUI()
        self.is_game_over()

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        return False
    
    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False

    def is_game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="You win!",
                bg=co.WINNER_BG,
                fg=co.GAME_OVER_FONT_COLOR,
                font=co.GAME_OVER_FONT).pack()
            return True
        
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="Game over!",
                bg=co.LOSER_BG,
                fg=co.GAME_OVER_FONT_COLOR,
                font=co.GAME_OVER_FONT).pack()
            return True


def main():
    Game()
    
def start_game():
    main()


pygame.init()
surface = pygame.display.set_mode((400, 500))

menu = pygame_menu.Menu(500, 400, 'Welcome to 2048',theme=pygame_menu.themes.THEME_BLUE)
menu.add_button('Play', start_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)