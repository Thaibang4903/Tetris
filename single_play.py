
from shapes import Shapes
from pieces import Piece
import  config
import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()
#khai báo thông số đầu vào cho giao diện
mid_x=config.mid_x+200
mid_y = config.mid_y+200
s_width = config.s_width
s_height = config.s_height
play_width = config.play_width
play_height = config.play_height
block_size = config.block_size
top_left_x = config.top_left_x+350
top_left_y = config.top_left_y
background = config.background


# pause game function
def pause(surface,clock):

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        surface.fill((0,0,0))
        pauseFont = pygame.font.SysFont('Consolas', 50, bold=True,italic=True)
        pauseText = pauseFont.render("PAUSE", True, (255, 255, 255))
        instructionFont = pygame.font.SysFont('Consolas', 20, bold=True, italic=True)
        instructionText = instructionFont.render("Press SPACE to continue. Press Q to quit.",True,(255,255,255))
        surface.blit(pauseText, (mid_x - pauseText.get_width()/2 , mid_y - pauseText.get_height()/2))
        surface.blit(instructionText, ((mid_x - instructionText.get_width()/2, mid_y + instructionText.get_height()/2 + 150 )))

        pygame.display.update()
        clock.tick(5)

    surface.fill((0,0,0))
    resumeFont = pygame.font.SysFont('Consolas', 30, bold=True, italic=True)
    resumeText = resumeFont.render("RESUME IN 2 SECONDS...", True, (255, 255, 255))
    surface.blit(resumeText, ((mid_x - resumeText.get_width()/2 , mid_y - resumeText.get_height()/2)))
    pygame.display.update()
    pygame.time.delay(2000)
    clock.tick(5)

# create grid function
def create_grid(locked_positions={}):
    # create a blank (black) 2-d array grid
    #            x-part                       y-part
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    # locked_positions --> a dict which contains colors(values) of position of tetris blocks(keys) that already in the grid
    #               pos     color
    # example --> {(1,1):(0,255,255)}

    # section of code to detect and update color of grid based on locked positions
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # (j,i) --> j is x-coordinate , i is y-coordinate
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c

    return grid

# to convert Piece object to real shapes
def convert_shape_format(shape):
    # shape --> Piece object
    positions = []

    # to determine the which rotation of shape format to be used
    format = shape.shape[shape.rotation % (len(shape.shape))]

    # loop through list of lists to locate the position of '0'
    for i,line in enumerate(format):
        for j, column in enumerate(line):
            if column == '0':
                # let the positions stick with the shape x and y coordinates
                positions.append((shape.x+j,shape.y+i))

    # to offset(cancel off)/adjust the position displayed
    for i,pos in enumerate(positions):
        positions[i] = (pos[0]-2,pos[1]-4)

    return positions

# to detect whether a space for Piece object is valid
def valid_space(shape, grid):
    # create a list of accepted positions from (0,0) to (9,19) and only if the position is not occupied by existed block (color equal to (0,0,0))
    accepted_pos = [(j,i) for j in range(10) for i in range(20) if grid[i][j] == (0,0,0)]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            # when the block is spawned, the y position will always be upper than the screen so y-coordinates will be negative and it is not a valid position
            # if pos[1] > -1 means we only check if it is in the valid position of not after the block is inside the play section
            if pos[1] > -1:
                return False
    return True

# to check whether a player is lost
def check_lost(positions):
    for pos in positions:
        x,y = pos
        # if y-coordinates less than 1 (0 or negative) --> the block is at top of play screen which means lost
        if y < 1:
            return True

    return False

# get random Piece object
def get_shape():
    return Piece(5,0,random.choice(Shapes.shapes))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("Consolas",size,bold=True)
    label = font.render(str(text),True,color)

    surface.blit(label,(top_left_x + play_width/2 - label.get_width()/2, top_left_y + play_height/2 - label.get_height()/2))

def draw_text_bottom(text, size, color, surface):
    font = pygame.font.SysFont("Consolas",size,bold=True,italic=True)
    label = font.render(str(text),True,color)

    surface.blit(label,(mid_x - label.get_width()/2, mid_y + label.get_height()/2 + 250))


def draw_grid(surface,grid_1,add=0):
# def draw_grid(surface, grid_1, grid_2, add=0):
    for i in range(len(grid_1)):
        pygame.draw.line(surface,(128,128,128),(top_left_x ,top_left_y + i*block_size),(top_left_x+play_width , top_left_y+ i * block_size))
        for j in range(len(grid_1[i])):
            pygame.draw.line(surface, (128, 128, 128), (top_left_x + j*block_size, top_left_y),(top_left_x  + j*block_size, top_left_y + play_height))

def clear_rows(grid, locked_pos):

    # delete rows part

    # inc --> increment index
    inc = 0

    #  read the grid from bottom to top
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        # to check whether there are blank(black) spaces in row
        if (0,0,0) not in row:
            inc += 1
            # ind --> current index been looped (locate index)
            ind = i
            for j in range(len(row)):
                # delete the cells in the row which fulfill the conditions of being deleted
                try:
                    del locked_pos[(j,i)]
                except:
                    continue

    # to shift the rows
    # need to add back rows to the top after delete the row
    if inc > 0:
        # the sorted convert the list of locked_position dictionary keys to a list and sorted the values based on the second value of dict keys(tuple) in descending order
        # [(1, 0), (2, 0), (1, 1), (0, 0), (2, 1), (0, 1)] --> [(0, 1), (2, 1), (1, 1), (1, 0), (2, 0), (0, 0)]
        # the locked pos(after deleted some cells form code on top) will be accessed from bottom to top
        for key in sorted(list(locked_pos),key= lambda x:x[1],reverse=True):
            x,y = key
            # to only shift down the rows that above the row that been deleted
            if y < ind:
                newKey = (x,y+inc)
                locked_pos[newKey] = locked_pos.pop(key)

    return inc

# display next shape beside the play section

# def draw_next_shape(shape_1,shape_2, surface,add=0)
def draw_next_shape(shape_1, surface, add=0):

    font = pygame.font.SysFont('Consolas',20,bold=True)
    label = font.render('Next Shape: ',True,(255,255,255))


    x_coor = top_left_x + play_width + 50
    y_coor = top_left_y + play_height/2 - 100
    format_1 = shape_1.shape[shape_1.rotation % (len(shape_1.shape))]

    for i,line in enumerate(format_1):
        for j,column in enumerate(line):
            if column == '0':
                pygame.draw.rect(surface,shape_1.color,(x_coor + j*block_size , y_coor + i*block_size,block_size,block_size),0)
                pygame.draw.rect(surface, (128, 128, 128), (int(x_coor + j * block_size), int(y_coor + i * block_size), block_size, block_size), 1)


    surface.blit(label,(x_coor+10,y_coor-30))
    pygame.display.update()


def draw_window(surface,grid_1,score_1=0,level=1,speed = 0.27,add=0):

    surface.fill((33,29,29))

    # initialize font object before creating it
    pygame.font.init()
    font = pygame.font.SysFont('Consolas',20,italic=True)
    label = font.render("LEVEL : "+str(level)+ "   SPEED: "+ str(round(1/speed,2)),True,(255,255,255))
    surface.blit(label, ((top_left_x + play_width)-300, 30))

    # draw the blocks
    # last arg represent border radius (0 = fill)
    for i in range(len(grid_1)):
        for j in range(len(grid_1[i])):
            pygame.draw.rect(surface, grid_1[i][j],
                             (top_left_x + (block_size * j), top_left_y + (block_size * i), block_size, block_size), 0)


    # draw the border
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x , top_left_y, play_width, play_height), 4)

    # draw the score
    font_1 = pygame.font.SysFont('Consolas', 20,bold=False,italic=True)
    label_1 = font_1.render('Score: '+ str(score_1), True, (255, 255, 255))

    #

    x_coor = top_left_x + play_width + 50
    y_coor = top_left_y + play_height / 2 - 100

    # draw
    surface.blit(label_1, (x_coor + 10 , y_coor - 120))
    draw_grid(surface, grid_1, add=int(mid_x))
    pygame.display.update()

def main(surface):
    run = True
    p1_locked_positions = {}
    p1_change_piece = False
    p1_current_piece = get_shape()
    p1_next_piece = get_shape()
    p1_score = 0


    clock = pygame.time.Clock()
    fallTime = 0
    level_time = 0
    level = 1
    fallSpeed = 0.27

    while run:

        # constantly update the grid while the program is running
        p1_grid = create_grid(p1_locked_positions)


        # gets the amount of time since last clock tick
        fallTime += clock.get_rawtime()
        level_time += clock.get_rawtime()
        # called once per frame
        clock.tick()

        # auto update the level after 15 seconds
        if level_time / 1000 > 15:
            level_time = 0
            if fallSpeed > 0.12:
                fallSpeed -= 0.01
                level += 1

        # to automatically move the piece down
        if fallTime/1000 >= fallSpeed:
            fallTime = 0
            p1_current_piece.y += 1

            # to detect the validity of piece and change it if it is not valid
            if not(valid_space(p1_current_piece,p1_grid)) and p1_current_piece.y > 0:
                p1_current_piece.y -= 1
                p1_change_piece = True


        # get user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # to detect the keys pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    p1_current_piece.rotation += 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.rotation -= 1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    p1_current_piece.x -= 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.x += 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    p1_current_piece.y += 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.y -= 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    p1_current_piece.x += 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.x -= 1
                # pause the game if space bar is pressed
                if event.key == pygame.K_SPACE:
                    pause(surface,clock)

        # to locate current_piece coordinates
        p1_shape_pos = convert_shape_format(p1_current_piece)

        for i in range(len(p1_shape_pos)):
            x,y = p1_shape_pos[i]
            # draw the color after it appears on play section
            if y > -1:
                p1_grid[y][x] = p1_current_piece.color
        # check for change_piece and update locked positions
        if p1_change_piece:
            for pos in p1_shape_pos:
                p = (pos[0],pos[1])
                p1_locked_positions[p] = p1_current_piece.color
                # locked_positions will look like this --> {(1,2):(0,255,255),......}
            # change current_piece to next_piece
            p1_current_piece = p1_next_piece
            p1_next_piece = get_shape()
            # change change_piece to False to prevent change_piece again
            p1_change_piece = False

            # only clear rows when next piece is generated
            p1_score += clear_rows(p1_grid,p1_locked_positions) * 10 * level




        # to break the loop if lost
        if check_lost(p1_locked_positions):
        #if check_lost(p1_locked_positions) or check_lost(p2_locked_positions):

            if check_lost(p1_locked_positions):
                font = pygame.font.SysFont("Consolas", 60, bold=True)
                label = font.render("YOU LOSE!!!", True, (255,255,255))
                label_2 = font.render("YOU WIN!!!", True, (255,255,255))

                surface.blit(label, (top_left_x + play_width / 2 - label.get_width() / 2 - 20,top_left_y + play_height / 2 - label.get_height() / 2))
                surface.blit(label_2, (top_left_x + play_width / 2 - label.get_width() / 2 + mid_x - 20,top_left_y + play_height / 2 - label.get_height() / 2))


            pygame.display.update()
            pygame.time.delay(3000)
            run = False

        # if there are multiple draw functions in one run, juz call pygame.display.update() in main loop once
        draw_window(surface,p1_grid,p1_score,level,fallSpeed,add=int(mid_x))
        draw_next_shape(p1_next_piece, surface, add=int(mid_x))
        pygame.display.update()




win = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Tetris Game")