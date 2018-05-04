# -*- coding: utf-8 -*-

__author__ = 'shixiaofeng'
__version__ = 'V1.0'

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    """Bullet类继承了我们从模块pygame.sprite中导入的Sprite类"""
    def __init__(self, ai_settings, screen, ship):
        '''在飞船的所在地方创建一个子弹'''

        '''为创建子弹实例，需要向__init()__传递ai_settings、screen和ship实例，还调用了super()来继承Sprite。'''
        super().__init__()
        self.screen = screen

        '''在（0.0）处创建一个表示子弹的矩形，再设置正确的位置
        我们创建子弹的rect， 子弹不是图形，因此我们必须使用pygame.Rect()
        类从空白处开始创建一个矩形'''

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx   #将子弹的centerx设置为飞船的rect.centerx
        self.rect.top = ship.rect.top    #子弹的rect的top属性设置为飞船的rect的top属性

        # 子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        # 更新表示移动子弹的y
        self.y -= self.speed_factor
        # 更新表示子弹rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)