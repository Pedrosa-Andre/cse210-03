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

    def compareValues(self):  
        
        val1 = self.firstCard
        val2 = self.secondCard

        if (val2 > val1): 
            return 'h'
        if (val2 < val1):
            return 'l'

    def computeScore(self):

        if not self.is_playing:
            return

        player = Player()

        score = player.getScore()
        userAnsw = self.card_guess
        compAnsw = self.compareValues()

        if (userAnsw == compAnsw):
            score = player.correctScore
        if (userAnsw != compAnsw):
            score = player.incorrectScore
            
        print(f"Next card was: {self.secondCard}")
        print(f"Your score is: {score}")

    def keepPlaying(self):   
        playGame = input("Play game? [y/n] ")
        self.is_playing = (playGame == "y")
