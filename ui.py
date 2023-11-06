import config
import  pygame
import ui_info
import single_play
import main
#khai báo thông số đầu vào cho giao diện
mid_x=config.mid_x
mid_y = config.mid_y
s_width = config.s_width
s_height = config.s_height
play_width = config.play_width
play_height = config.play_height
block_size = config.block_size
top_left_x = config.top_left_x
top_left_y = config.top_left_y
background = config.background
def main_menu(win):
    run = True
    while run:
        win.fill((255, 178, 102))
        win.blit(background,(0,-70))
        font = pygame.font.SysFont('Consolas', 40,bold=True,italic=True)
        label = font.render('T E T R I S', True, (255, 255, 255))
        win.blit(label,(mid_x - label.get_width()/2, mid_y - label.get_height()/2 - 250))
        draw_text_bottom("PRESS ANY KEY TO START THE GAME",40,(255,255,255),win)

        small_font = pygame.font.SysFont('Consolas', 20, bold=True, italic=True)
        small_label = small_font.render('( PRESS I FOR INFO )', True, (255, 255, 255))
        win.blit(small_label,(mid_x - small_label.get_width()/2,mid_y + small_label.get_height()/2 + 310))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    ui_info.info_page(win)
                else:
                    win.fill((0,0,0))
                    wait_font = pygame.font.SysFont('Consolas', 40,bold=True,italic=True)
                    wait_text = wait_font.render('STARTING GAME......', True, (255, 255, 255))
                    win.blit(wait_text,(mid_x-wait_text.get_width()/2,mid_y))
                    pygame.display.update()
                    pygame.time.delay(1500)
                    choose(win)
    pygame.display.quit()
def choose(surface):
    run = True

    while run:
        surface.fill((0, 0, 0))

        font = pygame.font.SysFont('Consolas', 40, bold=True, italic=True)
        label = font.render('T E T R I S', True, (255, 255, 255))
        label1 = font.render('1. Single Player', True, (255, 255, 255))
        label2 = font.render('2. Player VS Player', True, (255, 255, 255))
        label3 = font.render('3. Player VS Computer', True, (255, 255, 255))
        label4 = font.render('4. Computer vs Computer', True, (255, 255, 255))
        surface.blit(label, (mid_x - label.get_width() / 2, mid_y - label.get_height() / 2 - 250))
        surface.blit(label1, (mid_x - label.get_width(), mid_y - label.get_height() / 2 - 100))
        surface.blit(label2, (mid_x - label.get_width(), mid_y - label.get_height() / 2 - 50))
        surface.blit(label3, (mid_x - label.get_width(), mid_y - label.get_height() / 2))
        surface.blit(label4, (mid_x - label.get_width(), mid_y - label.get_height() / 2+50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    single_play.main(surface)
                    run=False
                elif event.key == pygame.K_2:
                    main.main(surface)
                    run=False
                elif event.key == pygame.K_3:
                    run = False
                elif event.key == pygame.K_4:
                    run = False
