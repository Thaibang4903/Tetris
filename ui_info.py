import pygame
import config
pygame.init()
mid_x=config.mid_x
mid_y = config.mid_y
s_width = config.s_width
s_height = config.s_height
play_width = config.play_width
play_height = config.play_height
block_size = config.block_size
top_left_x = config.top_left_x
top_left_y = config.top_left_y
def info_page(surface):
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    info = False

        surface.fill((0,0,0))
        pygame.draw.line(surface, (255, 255, 255), (s_width / 2, 75), (s_width / 2, s_height-40))
        pygame.draw.line(surface, (255, 255, 255), (0, 75), (s_width, 75))
        pygame.draw.line(surface, (255, 255, 255), (0, s_height-40), (s_width, s_height-40))
        font = pygame.font.SysFont('Consolas', 50, bold=True,italic=True)
        small_font = pygame.font.SysFont('Consolas', 22, bold=True, italic=True)

        info_text = font.render("INFO",True,(255,255,255))
        surface.blit(info_text,(mid_x-info_text.get_width()/2,20))

        quit_text = small_font.render("( PRESS Q TO QUIT INFO PAGE )",True,(255,255,255))
        surface.blit(quit_text,(mid_x-quit_text.get_width()/2,s_height-30))

        p1_head_text = font.render("PLAYER 1",True,(255,255,255))
        p1_info_text_1 = font.render("W  - ROTATE",True,(255,255,255))
        p1_info_text_2 = font.render("A  - MOVE LEFT", True, (255, 255, 255))
        p1_info_text_3 = font.render("S - MOVE DOWN", True, (255, 255, 255))
        p1_info_text_4 = font.render("D - MOVE RIGHT", True, (255, 255, 255))
        p1_info_text_5 = font.render("SPACE - PAUSE", True, (255, 255, 255))


        surface.blit(p1_head_text,(mid_x/2-p1_head_text.get_width()/2,mid_y/2-50))
        surface.blit(p1_info_text_1, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width()/32, mid_y / 2 + p1_info_text_1.get_height()*2-100))
        surface.blit(p1_info_text_2, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 3.5-100))
        surface.blit(p1_info_text_3, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 5-100))
        surface.blit(p1_info_text_4, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 6.5-100))
        surface.blit(p1_info_text_5, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 8-100))
        pygame.draw.line(surface, (255, 255, 255), (mid_x / 2 - p1_head_text.get_width() / 2, mid_y-100),(mid_x/1.5,mid_y-100))

        p2_head_text = font.render("PLAYER 2", True, (255, 255, 255))
        p2_info_text_1 = font.render("UP  - ROTATE", True, (255, 255, 255))
        p2_info_text_2 = font.render("LEFT  - MOVE LEFT", True, (255, 255, 255))
        p2_info_text_3 = font.render("DOWN - MOVE DOWN", True, (255, 255, 255))
        p2_info_text_4 = font.render("RIGHT - MOVE RIGHT", True, (255, 255, 255))
        p2_info_text_5 = font.render("SPACE - PAUSE", True, (255, 255, 255))

        surface.blit(p2_head_text, (mid_x / 2 - p1_head_text.get_width() / 2 + mid_x - 50, mid_y / 2-50))
        surface.blit(p2_info_text_1, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 2-100))
        surface.blit(p2_info_text_2, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 3.5-100))
        surface.blit(p2_info_text_3, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 5-100))
        surface.blit(p2_info_text_4, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 6.5-100))
        surface.blit(p2_info_text_5, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x - 50,mid_y / 2 + p1_info_text_1.get_height() * 8-100))
        pygame.draw.line(surface, (255, 255, 255), (mid_x / 2 - p1_head_text.get_width() / 2 +mid_x -50, mid_y - 100),(mid_x / 1.5 +mid_x -50, mid_y - 100))

        pygame.display.update()

    surface.fill((0, 0, 0))
    resumeFont = pygame.font.SysFont('Consolas', 30, bold=True, italic=True)
    resumeText = resumeFont.render("BACK TO MAIN MENU......", True, (255, 255, 255))
    surface.blit(resumeText, ((mid_x - resumeText.get_width() / 2, mid_y - resumeText.get_height() / 2)))
    pygame.display.update()
    pygame.time.delay(1000)

