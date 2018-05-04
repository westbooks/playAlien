# -*- coding: utf-8 -*-

__author__ = 'shixiaofeng'
__version__ = 'V1.0'


class GameStates(object):
    '''游戏统计信息'''

    def __init__(self, ai_settings):

        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_start()
        # 游戏一开始就是非活动状态
        self.game_active = False
        # 在任何情况下都不应该重置最高分
        self.high_score = 0

    def reset_start(self):
        '''初始化在游戏运行期间可能变化的的统计信息'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


