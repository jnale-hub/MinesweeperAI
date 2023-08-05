import unittest
from minesweeper import MinesweeperAI, Minesweeper, Sentence

class TestMinesweeperAI(unittest.TestCase):

    def setUp(self):
        self.game = Minesweeper(height=8, width=8, mines=6)
        self.ai = MinesweeperAI(height=8, width=8)

    def test_mark_safe(self):
        cell = (2, 3)
        self.ai.mark_safe(cell)
        self.assertIn(cell, self.ai.safes)
        self.assertNotIn(cell, self.ai.mines)

    def test_mark_mine(self):
        cell = (4, 1)
        self.ai.mark_mine(cell)
        self.assertIn(cell, self.ai.mines)
        self.assertNotIn(cell, self.ai.safes)

    def test_add_knowledge(self):
        pass # tbd

if __name__ == '__main__':
    unittest.main()

