#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is
#provided in project assessment.
class BowlingGame:
    #constructor for BowlingGame class
    def __init__(self):
        """
        This constructor initializes self aka the BowlingGame object

        Args:
        self(BowlingGame): the BowlingGame object to initalize
        """
        self.rolls_done=[] #rolls_done stores an array of integers representing pins knocked down in each roll

    #changed method name from roll() to record_roll()
    def record_roll(self,pins):
        """
        This function records a passed in roll into the rolls_done array

        Args:
        self(BowlingGame): the BowlingGame object
        pins(int): number of pins knocked down in roll
        """
        self.rolls_done.append(pins)

    #changed method name from score() to calculate_score()
    def calculate_score(self):
        """
        This function calculates the total score of the entire bowling game

        Args:
        self(BowlingGame): the BowlingGame object

        Returns:
        int: total score of the bowling game
        """
        total_score = 0
        rollIndex=0

        #iterate through rolls_done array and tally total score of bowling game
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
        """
        This function returns a boolean of whether the specified roll is a strike

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of roll to check for strike

        Returns:
        boolean: whether roll is a strike
        """
        return rollIndex < len(self.rolls_done) and self.rolls_done[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        This function returns a boolean of whether the specified frame is a spare

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of frame to check for spare

        Returns:
        boolean: whether frame is a spare
        """
        return (
            rollIndex + 1 < len(self.rolls_done)
            and self.rolls_done[rollIndex] + self.rolls_done[rollIndex + 1] == 10
        )

    def calculateStrikeScore(self, rollIndex):
        """
        This function calculates the strike score and returns the result

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of strike to calculate score of

        Returns:
        int: score of strike
        """
       # A strike is 10 + the sum of the next two rolls
        return 10 + self.rolls_done[rollIndex + 1] + self.rolls_done[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        """
        This function calculates the spare score and returns the result

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of spare to calculate score of

        Returns:
        int: score of spare
        """
        # A spare is 10 + the next roll
        return 10 + self.rolls_done[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        """
        This function calculates the frame score and returns the result

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of frame to calculate score of

        Returns:
        int: score of frame
        """
        # A regular frame is just the sum of two rolls
        return self.rolls_done[rollIndex] + self.rolls_done[rollIndex + 1]