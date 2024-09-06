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
        rollIndex = 0

        # Adding the try and except statement was my idea to refactor this code,
        # but ChatGPT wrote the modified code you see here.
        # This try and except statement catches errors of accessing an index out of bounds

        # Iterate through rolls_done array and tally total score of bowling game
        for frameIndex in range(10):
            try:
                if self.isStrike(rollIndex):  # this if statement was corrected
                    total_score += self.calculateStrikeScore(rollIndex)  # corrected method name for strikeScore()
                    rollIndex += 1
                elif self.isSpare(rollIndex):
                    total_score += self.calculateSpareScore(rollIndex)
                    rollIndex += 2
                else:
                    total_score += self.calculateFrameScore(rollIndex)
                    rollIndex += 2  # indented this line of code so that it's included in the else condition
            except IndexError:
                # Handle the case where rollIndex is out of bounds
                print(f"Error: rollIndex {rollIndex} is out of bounds.")
                break  # Exit the loop if an IndexError occurs
    
        return total_score  # return statement taken out of the for loop

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
        This function calculates the strike score and returns the result.

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of strike to calculate score of

        Returns:
        int: score of strike
        """

        #ChatGPT wrote this code for me after I prompted it asking
        #to add an if else chain to ensure that indexes
        #are only accessed if they exist when attempting to add
        #bonus rolls on to strike score

        # Base score for a strike is 10
        strike_score = 10

        # Check if there is at least one roll after the strike
        if rollIndex + 1 < len(self.rolls_done):
            strike_score += self.rolls_done[rollIndex + 1]
        
            # Check if there is a second roll after the strike
            if rollIndex + 2 < len(self.rolls_done):
                strike_score += self.rolls_done[rollIndex + 2]
            
        # Return the calculated score
        return strike_score


    def calculateSpareScore(self, rollIndex):
        """
        This function calculates the spare score and returns the result.

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of spare to calculate score of

        Returns:
        int: score of spare
        """

        #ChatGPT wrote this code for me after I prompted it asking
        #to add an if statement to check that a roll exists
        #after the spare before accessing the index
        spare_score = 10

        # Check if there is a roll after the spare
        if rollIndex + 2 < len(self.rolls_done):
            spare_score += self.rolls_done[rollIndex + 2]
        
        # Return the calculated score
        return spare_score


    def calculateFrameScore(self, rollIndex):
        """
        This function calculates the frame score and returns the result.

        Args:
        self(BowlingGame): the BowlingGame object
        rollIndex(int): index of frame to calculate score of

        Returns:
        int: score of frame
        """

        #ChatGPT wrote this code for me after I prompted it asking
        #to add an if statement to check that the second roll
        #exists in the frame before accessing the index
        frame_score = self.rolls_done[rollIndex]

        # Check if there is a second roll in the frame
        if rollIndex + 1 < len(self.rolls_done):
            frame_score += self.rolls_done[rollIndex + 1]
        
        # Return the calculated frame score
        return frame_score