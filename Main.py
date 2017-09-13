import pygame
from Python import Python
from Food import Food

pygame.init()
pygame.display.set_caption('Python')
screen_width, screen_height = (640, 480)
screen = pygame.display.set_mode((640, 480))

python = Python((200, 200))
food = Food()

pygame.font.init()
game_over_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
game_over_text = game_over_font.render('GAME OVER', 16, (255, 255, 0))

max_score = 50
score = 0
score_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
score_text = score_font.render("Score: 0/{0}".format(max_score), 16, (255, 255, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key != pygame.K_ESCAPE:
                python.move_python(event.key)
            else:
                pygame.quit()
                quit()

    if score >= max_score:
        game_over_text = game_over_font.render("YOU WIN!", 16, (255, 255, 0))
        pygame.display.get_surface().blit(game_over_text,
                                          game_over_text.get_rect(center=(screen_width/2, screen_height/2)))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            pygame.display.update()

    screen.fill((0, 0, 0))
    food.draw()
    if not python.draw():
        pygame.display.get_surface().blit(game_over_text,
                                          game_over_text.get_rect(center=(screen_width/2, screen_height/2)))

    if food.is_eaten(python.head_rect()):
        python.add_tail_segment()
        score += 1
        score_text = score_font.render("Score: {0}/{0}".format(score, max_score), False, (255, 255, 0))
        food = Food()
    pygame.display.get_surface().blit(score_text, (screen_width - score_text.get_width() - 50,
                                                   screen_height - score_text.get_height() - 10))
    pygame.display.update()
    pygame.time.delay(250)
