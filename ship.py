# -*- coding: utf-8 -*-

__author__ = 'shixiaofeng'
__version__ = 'V1.0'

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化飞船，并设置其初始化位置'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # 加载飞船图形，并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')  # 加载图像
        self.rect = self.image.get_rect()   # 获取图像大小
        self.screen_rect = screen.get_rect()  # 获取屏幕大小

        # 飞船放置在底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''根据移动标志调整飞船位置'''

        # 更新飞船的center值， 而不是rect值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据center值更新 rect值
        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx


