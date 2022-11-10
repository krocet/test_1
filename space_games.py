import pygame
import controls
from can import Can
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():

    pygame.init()
    screen = pygame.display.set_mode((600, 650))
    pygame.display.set_caption("Бей пришельцев")
    bg_color = 250, 250, 250
    can = Can(screen)
    baunts = Group()
    inopls = Group()
    controls.create_army(screen, inopls)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, can, baunts)
        if stats.run_game:
            can.update_can()
            controls.update(bg_color, screen, stats, sc, can, inopls, baunts)
            controls.update_baunts(screen, stats, sc, inopls, baunts)
            controls.update_inopls(stats, screen, sc, can, inopls, baunts  )


run()
