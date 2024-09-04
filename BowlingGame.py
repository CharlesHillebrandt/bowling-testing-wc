#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is
#provided in project assessment.
class BowlingGame:
    def __init__(self):
        self.rolls_done=[]

    #changed method name from roll() to record_roll()
    def record_roll(self,pins):
        self.rolls_done.append(pins)

    #changed method name from score() to calculate_score()
    def calculate_score(self):
        total_score = 0
        rollIndex=0

        for frameIndex in range(10):
            if self.isStrike(rollIndex): #this if statement was corrected.
                total_score += self.calculateStrikeScore(rollIndex) #corrected method name for strikeScore()
                rollIndex +=1
            elif self.isSpare(rollIndex):
                total_score += self.calculateSpareScore(rollIndex)
                rollIndex +=2
            else:
                total_score += self.calculateFrameScore(rollIndex)
                rollIndex +=2 #indented this line of code so that its included in the else condition
        
        return total_score #return statement taken out of for loop

    def isStrike(self, rollIndex): 
        return rollIndex < len(self.rolls_done) and self.rolls_done[rollIndex] == 10

    def isSpare(self, rollIndex):
        return (
            rollIndex + 1 < len(self.rolls_done)
            and self.rolls_done[rollIndex] + self.rolls_done[rollIndex + 1] == 10
        )

    def calculateStrikeScore(self, rollIndex):
       # A strike is 10 + the sum of the next two rolls
        return 10 + self.rolls_done[rollIndex + 1] + self.rolls_done[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        # A spare is 10 + the next roll
        return 10 + self.rolls_done[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        # A regular frame is just the sum of two rolls
        return self.rolls_done[rollIndex] + self.rolls_done[rollIndex + 1]

