from points import Points
from card import Cards


class Director:
    """A entity which directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        TODO add atributes
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        self.card = Cards()
        while self.is_playing:
            self.getAnswer()
            self.compareValues()
            self.computeScore()

            if self.total_score <= 0:
                self.keepPlaying()

    def getAnswer(self):
        """ Displays the number of the card played
        Asks the player to guess if the next card is higher or lower

        Args:
            self (Director): an instance of Director.
        """

        self.lastCard = self.card.lastCard()
        self.newCard = self.card.pullFirstCard()

        print(f"The card is: {self.lastCard}")
        while True:
            self.card_guess = input("Higher or Lower? [h/l] ")
            if self.card_guess.lower() not in ('h', 'l'):
                print(f"Not an aprropriate input.")
            else:
                break
        return self.card_guess

    def compareValues(self):
        """Compare two numeric values, 
        if the second is bigger returns'h' (higher)
        if the second is smaller returns 'l'(lower)

        Args:
            val1 (int): The value from showNumberCard()
            val2 (int): The value from showNextCard()
        """

        if not self.is_playing:
            return

        val1 = self.lastCard
        val2 = self.newCard

        if (val2 > val1):
            return 'h'
        if (val2 < val1):
            return 'l'

    def computeScore(self):
        """Compare two answers, if they're equal adds 100 points to the user,
        if not substract 75 points from the user.
        Displays the score.

        Arg:
            userAnsw: The answer from the user (getAnswer())
            compAnsw: The answer from compareValues()
        """

        if not self.is_playing:
            return

        points = Points()

        self.score = points.getScore()
        userAnsw = self.card_guess
        compAnsw = self.compareValues()

        if (userAnsw == compAnsw):
            self.score = points.correctScore
        if (userAnsw != compAnsw):
            self.score = points.incorrectScore

        self.total_score += self.score

        print(f"Next card was: {self.newCard}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

    def keepPlaying(self):
        """Ask the player if they want to play again
        """

        playGame = input("Play game? [y/n] ")

        if playGame.lower() == "y":
            self.is_playing = True
        else:
            self.is_playing = False
