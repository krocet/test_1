from os import path
img_dir = path.join(path.dirname(__file__), 'paint')
class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует стаистику"""
        self.reset_stats()
        self.run_game = True
        with open(path.join(img_dir, 'highscore.txt'), 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.cans_left = 2
        self.score = 0
