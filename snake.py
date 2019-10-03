import pygame
import random

UP    = (0, -1)
DOWN  = (0,  1)
RIGHT = (1,  0)
LEFT  = (-1,  0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN  = (0, 255, 0)
SIZE = [400, 400]
GRID = 10

def draw_rect(surface, position, colour):
    r = pygame.Rect((position[0]+1, position[1]+1), (GRID - 1, GRID - 1))
    pygame.draw.rect(surface, colour, r)

class Snake:

    def __init__(self, surface, size, colour):
        self.surface = surface
        self.size = size
        a = random.randint(size[0]/GRID/4, size[0]/GRID/4*3)
        b = random.randint(size[1]/GRID/4, size[1]/GRID/4*3)
        start_location = (a*GRID, b*GRID)
        self.body = [start_location]
        self.head = self.body[0]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.check_alive = True
        self.length = 1
        self.colour = colour

    def move(self, food):

        if self.check_alive:
            self.head = self.body[0]
            if self.direction != (0,0):
                x, y = self.direction
                new = ((self.head[0] + x * GRID) % SIZE[0], (self.head[1] + y * GRID) % SIZE[1])
                if len(self.body) > 2 and new in self.body[2:]:
                    self.check_alive = False
                else:
                    self.body.insert(0, new)
                    if not new == food.location:
                        self.body.pop()
                    else:
                        self.length += 1
                        food.location = None

    def heading(self, dir):

        if (dir[0] * -1, dir[1] * -1) == self.direction:
            return

        else:
            self.direction = dir



    def draw(self):

        for p in self.body:
            draw_rect(self.surface, p, self.colour)

class Food:

    def __init__(self, surface, snake_list):

        self.surface = surface
        self.snake_list = snake_list
        self.location = None
        self.spawn_food()

    def spawn_food(self):

        while self.location is None:
            temp = (random.randint(0, (SIZE[0]/GRID) - 1) * GRID, random.randint(0, (SIZE[1]/GRID) - 1) * GRID)
            for i in range(len(self.snake_list)):
                for j in range(len(self.snake_list[i].body)):
                    if temp == self.snake_list[i].body[j]:
                        self.location = None
                    else:
                        self.location = temp

    def draw(self):

        f = self.location

        if self.location is not None:
            pygame.draw.circle(self.surface, WHITE, (f[0]+5, f[1]+5), 4, 3)

def gameover(surface, snake_list):

    player1 = snake_list[0]
    player2 = snake_list[1]
    font = pygame.font.SysFont('Comic Sans MS', 20)

    """"# check if player 1 hits the wall
    if not player1.alive():
        text = font.render('Player 2 won the game!', False, RED)
        surface.blit(text, (100, 200))
        return True
    # check if player 2 hits the wall
    if not player2.alive():
        text = font.render('Player 1 won the game!', False, RED)
        surface.blit(text, (100, 200))
        return True"""

    # check if either one hits others body
    if player1.length > 1 and player2.length > 1:
        # check if player 1 hits player 2
        for i in range(len(player2.body)):
            if i != 0:
                if player1.head == player2.body[i]:
                    player1.check_alive = False
                    player2.check_alive = False
                    text = font.render('Player 2 won the game!', False, RED)
                    surface.blit(text, (100, 200))
                    return True

        # check if player 2 hits player 1
        for j in range(len(player1.body)):
            if j != 0:
                if player2.head == player1.body[j]:
                    player1.check_alive = False
                    player2.check_alive = False
                    text = font.render('Player 1 won the game!', False, RED)
                    surface.blit(text, (100, 200))
                    return True

    # check if they hit themselves head by head
    if player1.head == player2.head:
        text = font.render('DRAW!', False, RED)
        surface.blit(text, (100, 100))
        if player1.length > player2.length:
            text1 = font.render('Player 1 won the game!', False, RED)
            surface.blit(text1, (100, 200))
        elif player2.length > player1.length:
            text2 = font.render('Player 2 won the game!', False, RED)
            surface.blit(text2, (100, 200))
        return True

    return False

def restart():

    snake1 = Snake(surface, SIZE, WHITE)
    snake2 = Snake(surface, SIZE, GREEN)
    snake = [snake1, snake2]
    food = Food(surface, snake)
    return snake1, snake2, snake, food

if __name__ == '__main__':

        pygame.init()
        pygame.font.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(SIZE)
        surface = pygame.Surface(screen.get_size())
        surface.convert()
        surface.fill((0,0,0))
        fps = 5
        done = False
        snake1 = Snake(surface, SIZE, WHITE)
        snake2 = Snake(surface, SIZE, GREEN)
        snake = [snake1, snake2]
        food = Food(surface, snake)
        counter = 0
        mytext = pygame.font.SysFont('Comic Sans MS', 20)
        ended = False

        while not done:

            if ended:
                # wait for the winner announcement
                pygame.time.wait(800)

                # restarting texts
                surface.fill((0,0,0))
                restarting = mytext.render('Restarting in...', False, RED)
                surface.blit(restarting, (100, 200))
                screen.blit(surface, (0,0))
                pygame.display.flip()
                pygame.time.wait(800)

                surface.fill((0,0,0))
                Three = mytext.render('3', False, RED)
                surface.blit(Three, (200, 200))
                screen.blit(surface, (0,0))
                pygame.display.flip()
                pygame.time.wait(800)

                surface.fill((0,0,0))
                Two = mytext.render('2', False, RED)
                surface.blit(Two, (200, 200))
                screen.blit(surface, (0,0))
                pygame.display.flip()
                pygame.time.wait(800)

                surface.fill((0,0,0))
                One = mytext.render('1', False, RED)
                surface.blit(One, (200, 200))
                screen.blit(surface, (0,0))
                pygame.display.flip()
                pygame.time.wait(800)

                surface.fill((0,0,0))
                snake1, snake2, snake, food = restart()
                counter = 0
                fps = 5
                ended = False

            if counter < 5:

                clock.tick(fps)

                description1 = 'Player 1 is white in colour'
                text1 = mytext.render(description1, False, WHITE)
                surface.blit(text1, (100, 125))

                description2 = 'Controlled by arrows'
                text2 = mytext.render(description2, False, WHITE)
                surface.blit(text2, (100, 160))

                description3 = 'Player 2 is green in colour'
                text3 = mytext.render(description3, False, GREEN)
                surface.blit(text3, (100, 240))

                description4 = 'Controlled by W,A,S,D'
                text4 = mytext.render(description4, False, GREEN)
                surface.blit(text4, (100, 275))

                counter += 0.5

            else:
                fps += 0.03
                clock.tick(fps)

                surface.fill((0,0,0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True
                            break
                        if event.key == pygame.K_UP:
                            snake1.heading(UP)
                        if event.key == pygame.K_DOWN:
                            snake1.heading(DOWN)
                        if event.key == pygame.K_LEFT:
                            snake1.heading(LEFT)
                        if event.key == pygame.K_RIGHT:
                            snake1.heading(RIGHT)
                        if event.key == pygame.K_w:
                            snake2.heading(UP)
                        if event.key == pygame.K_s:
                            snake2.heading(DOWN)
                        if event.key == pygame.K_a:
                            snake2.heading(LEFT)
                        if event.key == pygame.K_d:
                            snake2.heading(RIGHT)

                if not gameover(surface, snake):
                    food.spawn_food()
                    snake1.move(food)
                    snake1.draw()
                    snake2.move(food)
                    snake2.draw()
                    food.draw()

                else:
                    ended = True

            screen.blit(surface, (0,0))
            pygame.display.flip()
            pygame.display.update()