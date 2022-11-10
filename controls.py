import pygame, sys
from baunt import Baunt
from inopl import Inopl
import time

def events(screen, can, baunts):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                can.mright = True
            elif event.key == pygame.K_a:
                can.mleft = True
            elif event.key == pygame.K_SPACE:
                new_baunt = Baunt(screen, can)
                baunts.add(new_baunt)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                can.mright = False
            elif event.key == pygame.K_a:
                can.mleft = False

def update(bg_color, screen, stats, sc, can, inopls, baunts):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for baunt in baunts.sprites():
        baunt.draw_baunt()
    can.output()
    inopls.draw(screen)
    pygame.display.flip()

def update_baunts(screen, stats, sc, inopls, baunts):
    """обновлять позиции пуль"""
    baunts.update()
    for baunt in baunts.copy():
        if baunt.rect.bottom <= 0:
            baunts.remove(baunt)
    collisions = pygame.sprite.groupcollide(baunts, inopls, True, True)
    if collisions:
        for inopls in collisions.values():
            stats.score += 10 * len(inopls)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_cans()
    if len(inopls) == 0:
        baunts.empty()
        create_army(screen, inopls)

def can_kill(stats, screen, sc, can, inopls, baunts):
    """столкновение пушки и армии"""
    if stats.cans_left > 0:
        stats.cans_left -= 1
        sc.image_cans
        inopls.empty()
        baunts.empty()
        create_army(screen, inopls)
        can.create_can()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inopls(stats, screen, sc, can, inopls, baunts):
    """обновляет позиции инопланитян"""
    inopls.update()
    if pygame.sprite.spritecollideany(can, inopls):
        can_kill(stats, screen, sc, can, inopls, baunts)
    inopls_check(stats, screen, sc, can, inopls, baunts)


def inopls_check(stats, screen, sc, can, inopls, baunts ):
    """проверка, добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for inopl in inopls.sprites():
        if inopl.rect.bottom >= screen_rect.bottom:
            can_kill(stats, screen, sc, can, inopls, baunts)
            break



def create_army(screen, inopls):
    """создание армии пришельцев"""
    inopl = Inopl(screen)
    inopl_width = inopl.rect.width
    number_inopl_x = int((600 - 2 * inopl_width) / inopl_width)
    inopl_height = inopl.rect.height
    number_inopl_y = int((650 - 300 - 2 * inopl_height) / inopl_height)

    for row_number in range(number_inopl_y - 1 ):
        for inopl_number in range(number_inopl_x):
            inopl = Inopl(screen)
            inopl.x = inopl_width + (inopl_width * inopl_number)
            inopl.y = inopl_height + (inopl_height * row_number)
            inopl.rect.x = inopl.x
            inopl.rect.y = inopl.rect.height + (inopl.rect.height * row_number)
            inopls.add(inopl)


def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))



