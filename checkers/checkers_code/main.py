
import pygame
from checkers_game.game import Game
#CONSTANTS
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
#COLORS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
#TIME
FPS = 60

#CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers Game')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row,col

def main():
    #GAME LOOP
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    #piece = board.get_piece(0,1)
    #board.move(piece,4,3)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)

                game.select(row,col)
                
        
        game.update()


    pygame.quit()

main()
