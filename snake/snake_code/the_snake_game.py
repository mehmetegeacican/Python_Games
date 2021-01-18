import pygame
import pygame_menu
import sys
import random


#GLOBAL VARIABLES
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRID_SIZE
GRID_HEIGHT = SCREEN_WIDTH / GRID_SIZE

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

class Snake(object):
    def __init__(self):
        self.length = 1
        self.pos = [((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
        self.color = (100,3,5)
        self.score = 0

    def get_head_position(self):
        return self.pos[0]

    def turn(self,point):
        if self.length > 1 and (point[0]*-1,point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        curr = self.get_head_position()
        x,y = self.direction
        new = ((( curr[0]+(x*GRID_SIZE) ) % SCREEN_WIDTH), ( curr[1]+ (y*GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.pos) > 2 and new in self.pos[2:]:
            self.reset()
        else:
            self.pos.insert(0,new)
            if len(self.pos) > self.length:
                self.pos.pop()
    def reset(self):
        self.length = 1
        self.pos = [((SCREEN_WIDTH)/2,(SCREEN_HEIGHT)/2)]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
        self.score = 0
    
    def draw(self,surface):
        for p in self.pos:
            r = pygame.Rect((p[0],p[1]),(GRID_SIZE,GRID_SIZE))
            pygame.draw.rect(surface,self.color,r)
            pygame.draw.rect(surface,(0,0,0),r,1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
    
class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRID_SIZE, random.randint(0, GRID_HEIGHT-1)*GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (0, 0, 0), r, 1)

def draw_grid(surface):
    for y in range(0,int(GRID_HEIGHT)):
        for x in range(0,int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRID_SIZE,y*GRID_SIZE),(GRID_SIZE,GRID_SIZE))
                pygame.draw.rect(surface,(50,60,70),r)
            else:
                rr = pygame.Rect((x*GRID_SIZE,y*GRID_SIZE),(GRID_SIZE,GRID_SIZE))
                pygame.draw.rect(surface,(60,70,80),rr)

#MAIN GAME LOOP

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    food = Food()
    score = 0
    run = True

    myfont = pygame.font.SysFont("monospace",16)

    while run:
        clock.tick(10)
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        #***EVENT HANDLER**
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

def start_game():
    main()


pygame.init()
surface = pygame.display.set_mode((480, 480))

menu = pygame_menu.Menu(480, 480, 'Welcome to Snake',theme=pygame_menu.themes.THEME_DARK)
menu.add_button('Play', start_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
