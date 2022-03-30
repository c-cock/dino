import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping dino')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 30

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
#이미지 로드

    i = 0
    imgDino1 = pygame.image.load('dino1.png')
    imgDino2 = pygame.image.load('dino2.png')
    dino_height = imgDino1.get_size()[1]
    dino_bottom = SCREEN_HEIGHT - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False

    imgTree = pygame.image.load('tree.png')
    tree_height = imgTree.get_size()[1]

#죽었을 때
    game_over_img = pygame.image.load('game_over.png')

    quit = False

    while not quit:
        game_over = False
        game_over_delay = FPS * 2

        dino_x = 50
        dino_y = dino_bottom
        jump_top = 200
        leg_swap = True
        is_bottom = True
        is_go_up = False

        tree_x = SCREEN_WIDTH
        tree_y = SCREEN_HEIGHT - tree_height

#스크린색
        while not quit and (not game_over or game_over_delay > 0):
            screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     quit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if is_bottom:
                            is_go_up = True
                            is_bottom = False
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        quit = True
                        
            if game_over:
                screen.blit(game_over_img, (0, 0))
                i = 0
            else:
                if is_go_up:
                    dino_y -= 10.0
                elif not is_go_up and not is_bottom:
                    dino_y += 10.0

                if is_go_up and dino_y <= jump_top:
                    is_go_up = False

                if not is_bottom and dino_y >= dino_bottom:
                    is_bottom = True
                    dino_y = dino_bottom
#나무
                tree_x -= 12.0
                if tree_x <= 0:
                    tree_x = SCREEN_WIDTH

                if leg_swap:
                    leg_swap = False
                else:
                    leg_swap = True
                    

            screen.blit(imgTree, (tree_x, tree_y))

            if leg_swap:
                screen.blit(imgDino1, (dino_x, dino_y))
            else:
                screen.blit(imgDino2, (dino_x, dino_y))
                
            if game_over:
                game_over_delay -= 1
            elif abs(tree_x - dino_x) <= 30 and abs(tree_y - dino_y) <= 30:
                game_over = True

            pygame.display.update()
            fps.tick(FPS)
            i += 1
            if i % 10 == 0:
                print(i)

        pygame.quit()
        
main()















