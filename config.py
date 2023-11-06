import  pygame
# background picture of main menu
background = pygame.image.load('bgp.jpg')
# global vars
# screen(window) width and height
s_width = 1400
s_height = 700

# play section width and height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

# x and y coordinates for top-left position of play section
top_left_x = (s_width/2 - play_width) // 2
top_left_y = s_height - play_height

# coordinates for middle of screen
# use as parameter for second grid
mid_x = (s_width/2)
mid_y = (s_height/2)

