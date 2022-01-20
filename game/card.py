import random

class Cards:
    '''
    A template for things in the Card category. The responsibility of 
    this class is to handle the random generation of card values.
    '''

    def __init__(self):
        '''
        Set intial value of variable via constructor
        '''
        self.cardGenerate = 0

    def showNumberCard(self):
        '''
        Generate and return random value between 1 and 13 
        '''
        self.cardGenerate = random.randint(1, 13)
        return self.cardGenerate


    

    
        