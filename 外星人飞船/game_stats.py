import  pygame

class GanemStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        self.level = 0
        #在任何情况下都不应该重置最高分
        self.high_score = 0
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit


    def prep_high_score(self):
        "''将最高分渲染成图像"
        high_score = round(self.stats.high_score,-1)
        high_score_str =f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        #将最高分放在屏幕中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

