import pygame
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
    """显示得分的类"""

    def __init__(self,ai_game):
        """初始化显示得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game
        self.prep_ships()

        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分图像和最高分图像
        self.prep_score()
        self.prep_level()

    def prep_score(self):
        """将得分渲染成图像"""
        rounded_score = round(self.stats.score,-1)
        score_str = f"{rounded_score}"
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        #在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分和最高分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.level_image,self.level_rect)

    def prep_ships(self):
        """显示还剩下多少艘飞船"""
        self.ships = Group()
        for ship_number in range (self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x =10 + ship_number * ship.rect.width
            ship.rect.y =10
            self.ships.add(ship)

    def prep_level(self):
        """将等级渲染成图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        #将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10