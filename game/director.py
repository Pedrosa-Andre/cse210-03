from player import Player
from card import Cards


class Director:
    """A entity which directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        TODO add atributes
    """
    def __init__(self):
        self.is_playing = True
    def start_game(self):
        while self.is_playing:
            self.getAnswer()
            self.compareValues()
            self.computeScore()
            self.keepPlaying()
    def getAnswer(self):
        card = Cards()
        self.firstCard = card.showNumberCard()
        self.secondCard = card.showNumberCard()
        print(f"The card is: {self.firstCard}")
        self.card_guess = input("Higher or Lower? [h/l]")
        return self.card_guess

    def compareValues(val1, val2):
        """Compare two numeric values, if the second is bigger returns
        'h' (higher) if the second is smaller returns 'l' (lower)

        Args:
            val1 (int): The value from showNumberCard()
            val2 (int): The value from showNextCard()
        """
        if (val2 > val1):
            return 'h'
        if (val2 < val1):
            return 'l'
            
    def computeScore(userAnsw, compAnsw):
        """Compare two answers, if they're equal adds 100 points to the
        user, if not subtract 75 points from the user.

        Args:
            userAnsw (char): The answer from the user (getAnswer())
            compAnsw (char): The answer from compareValues() 
        """
        
        currentScore = player.getScore() 
        if (userAnsw == compAnsw):
            player.setScore(currentScore + 100)
        if (userAnsw != compAnsw):
            player.setScore(currentScore -75)