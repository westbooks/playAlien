# -*- coding: utf-8 -*-

__author__ = 'shixiaofeng'
__version__ = 'V1.0'

import pygame
from pygame.sprite import Sprite


class Ailen(Sprite):
    def __init__(self, ai_settings, screen):
        '''初始化外星人，并设置其位置'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # 加载外星人图像，并且设置rect属性
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        #每个外星人一开始都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''如果外星人处于屏幕边缘，就返回true'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        '''向左或者向右移动外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x