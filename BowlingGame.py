#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is
#provided in project assessment.
class BowlingGame:
    def __init__(self):
        self.rolls_done=[]

    def a_roll(self,pins):
        self.rolls_done.append(pins)

    def score(self):
        total_score = 0
        rollIndex=0

        for frameIndex in range(10):
            if self.isStrike(rollIndex): #this if statement was corrected.
                total_score += self.strikeScore(rollIndex) #corrected method name for strikeScore()
                rollIndex +=1
            elif self.isSpare(rollIndex):
                total_score += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                total_score += self.frameScore(rollIndex)
                rollIndex +=2 #indented this line of code so that its included in the else condition
        
        return total_score #return statement taken out of for loop

    #modified function definitions of... 
    # ... (5 below) isStrike, isSpare, strikeScore, spareScore, frameScore
    # ...to check indices exist before accessing them

    def isStrike(self, rollIndex): 
        return rollIndex < len(self.rolls_done) and self.rolls_done[rollIndex] == 10

    def isSpare(self, rollIndex):
        return (
            rollIndex + 1 < len(self.rolls_done)
            and self.rolls_done[rollIndex] + self.rolls_done[rollIndex + 1] == 10
        )

    def strikeScore(self, rollIndex):
       # A strike is 10 + the sum of the next two rolls_done
        return 10 + self.rolls_done[rollIndex + 1] + self.rolls_done[rollIndex + 2]

    def spareScore(self, rollIndex):
        # A spare is 10 + the next roll
        return 10 + self.rolls_done[rollIndex + 2]

    def frameScore(self, rollIndex):
        # A regular frame is just the sum of two rolls_done
        return self.rolls_done[rollIndex] + self.rolls_done[rollIndex + 1]

