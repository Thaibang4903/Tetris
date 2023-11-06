import pygame
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