# -*- coding: utf-8 -*-

# 程序主入口

'''
创建pygame窗口响应以及用户输入
'''

import pygame
from settings import Settings
from ship import Ship
from button import Button
from game_state import GameStates
from scoreboard import Scoreboard
from pygame.sprite import Group
import game_functions as gf


def run_game():

    # 初始化游戏并且创建一个屏幕对象
    pygame.init()

    # 加载配置参数
    ai_settings = Settings()

    # 根据配置参数，初始化窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建play 按钮
    play_button = Button(ai_settings, screen, 'PLAY')

    # 创建游戏存储统计
    stats = GameStates(ai_settings)

    # 创建得分榜
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一个ship
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星人
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
