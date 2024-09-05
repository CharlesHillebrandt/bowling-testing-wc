#File 1 (Test.py)
#This file has information about test cases which you need to test.
import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.record_roll(0)
        assert self.game.calculate_score()==0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.calculate_score()==20

    def testOneSpare(self):
        self.game.record_roll(5)
        self.game.record_roll(5)
        self.game.record_roll(3)
        self.rollMany(0,17)
        assert self.game.calculate_score()==16

    def testOneStrike(self):
        self.game.record_roll(10)
        self.game.record_roll(4)
        self.game.record_roll(3)
        self.rollMany(0,16)
        assert self.game.calculate_score()==24

    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.calculate_score()==300

    def testOneSpare(self):
        self.rollMany(5,21)
        assert self.game.calculate_score()==150

    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.record_roll(pins)

    #THE FOLLOWING TEST CASES WERE WRITTEN BY ME

    def testOneRollAfterStrike(self):
        self.game.record_roll(10)
        self.game.record_roll(5)
        assert self.game.calculate_score() == 15

    #THE FOLLOWING TEST CASES WERE GENERATED BY CHAT GPT

    def testSingleFrameStrike(self):
        self.game.record_roll(10)  # Strike in the first frame
        assert self.game.calculate_score() == 10  # Should handle the strike with no further rolls

    def testLastFrameStrike(self):
        self.rollMany(0, 18)  # First 9 frames are gutter balls
        self.game.record_roll(10)  # Strike in the last frame
        self.game.record_roll(3)
        self.game.record_roll(6)  # Bonus rolls
        assert self.game.calculate_score() == 19


    def testLastFrameSpare(self):
        self.rollMany(0, 18)  # First 9 frames are gutter balls
        self.game.record_roll(5)
        self.game.record_roll(5)  # Spare in the last frame
        self.game.record_roll(3)  # Bonus roll
        assert self.game.calculate_score() == 13
