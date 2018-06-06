import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一部飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 响应按键和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船位置
        ship.update()

        # 更新子弹位置
        bullets.update()

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
