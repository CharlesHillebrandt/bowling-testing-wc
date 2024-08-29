#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is
#provided in project assessment.
class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex=0

        for frameIndex in range(10):
            if self.isStrike(rollIndex): #this if statement was corrected.
                result += self.strikeScore(rollIndex) #corrected method name for strikeScore()
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2 #indented this line of code so that its included in the else condition
        
        return result #return statement taken out of for loop
        
    #modified function definitions of... 
    # ... (5 below) isStrike, isSpare, strikeScore, spareScore, frameScore
    # ...to check indices exist before accessing them

    def isStrike(self, rollIndex): 
        return rollIndex < len(self.rolls) and self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return (
            rollIndex + 1 < len(self.rolls)
            and self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
        )

    def strikeScore(self, rollIndex):
       # A strike is 10 + the sum of the next two rolls
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        # A spare is 10 + the next roll
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        # A regular frame is just the sum of two rolls
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]

