import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一部飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 创建外星人群
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 响应按键和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            # 更新飞船位置
            ship.update()

            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)


run_game()
