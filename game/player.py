

class Player:
    """The responsibility of Player is to keep track 
    of the points depending on the user input.
    
    Attributes:
        points (int): the starting points for the user
      """

    def __init__(self):
        """Constructs a new instance of Player with points attributes.

        Args:
            self (Player): An instance of Player.
        """

        # self.points = 0 not sure if this is necessary    

    def setScore (self): 
        """Sets the score for the player
        The player starts with 300 points
        Args:
            self (Player): An instance of Player."""
        
        self.points = 300
        return self.points


    def getScore(self):
        """ it gives a score based on the player guess, 
        The player earns 100 points if guessed correctly
        The player loses 75 points if guessed incorrrectly

        Args:
            self (Player): An instance of Player.
        """
        self.setScore ()
        self.correctScore = self.points + 100 
        self.incorrectScore = self.points -75 
        