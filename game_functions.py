import sys
import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 如果事件为退出事件,则执行退出
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen():
    pass
