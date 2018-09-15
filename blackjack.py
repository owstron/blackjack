import random

class Card:
    def __init__(self, shortName, value, fullName):
        self.shortName = shortName
        self.chosenValue = value
        self.initialValue = value
        self.fullName = fullName
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.totalPoints = 0
    
    def calcTotalPoints(self):
        self.totalPoints = 0
        for card in self.hand:
            if card.shortName == 'A':
                while (True):
                    card.chosenValue = eval(input('You have an Ace, do you want to value it to 1 or 10? '))
                    if card.chosenValue == 1 or card.chosenValue == 10:
                        break
            self.totalPoints += card.chosenValue

    def initialRound(self, deck):
        self.hand = [deck.pop() for _ in range(2)]
    
    def hit(self, deck):
        self.hand.append(deck.pop())
    
    def showHand(self):
        print(f'{self.name}\'s hand::')
        for card in self.hand:
            print(card.fullName)
        self.calcTotalPoints()
        print(f'Your total points is:: {self.totalPoints}')

class Dealer(Player):
    def __init__(self):
        Player.__init__(self, 'Dealer')
    
    # Not sure what redo does here
    # Perhaps you need a different strategy for picking the value of aces,
    # like generating all possible permutations (since there may be two) and
    # returning the one closest to 21.
    def calcTotalPoints(self, redo=False):
        self.totalPoints = 0
        ace = ''

        for card in self.hand:
            if card.shortName == 'A':
                ace = card
            self.totalPoints += card.chosenValue
        
        if ace != '' and not redo:
            if self.totalPoints >= 21:
                ace.chosenValue = 1
            else:
                ace.chosenValue = random.choice([1, 10])
            self.calcTotalPoints(True)
    
    def hit(self, deck):
        pickedCard = deck.pop()
        print(f'Dealer picked {pickedCard.fullName}')
        self.hand.append(pickedCard)
        self.calcTotalPoints()
        

def initializeDeck():
    deck = []
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suits = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
    for i in range(0, len(cards)):
        card = cards[i]
        name = names[i]
        for suit in suits:
            shortName = card
            fullName = '{} of {}'.format(name, suit)
            if card in ['A', 'J', 'Q', 'K']:
                value = 10
            else:
                value = int(card)
            deck.append(Card(shortName, value, fullName))
    return deck

def initializePlayer(name=''):
    if name == '':
        name = input('Enter your name: ')
    return Player(name)

def Game():
    deck = initializeDeck()
    random.shuffle(deck)

    player = initializePlayer()
    dealer = Dealer()

    player.initialRound(deck)
    dealer.initialRound(deck)

    print(f'\n----{player.name}\'s Turn-----')
    player.showHand()
    while (True):
        if player.totalPoints == 21:
            return 'Woohooo! BlackJack!! You win!!!'
        elif player.totalPoints > 21:
            return 'Busted! You lose!!'
        else:
            choice = input('Do you want to hit(Y/N)?')
            if (choice.upper() == 'Y'):
                print('You chose to hit.')
                player.hit(deck)
                player.showHand()
            else:
                print('You chose to stand.')
                break
            
    print('\n----Dealer\'s Turn----')
    dealer.showHand()
    # When does this end?
    while(True):
        if dealer.totalPoints < 17:
            dealer.hit(deck)
            dealer.showHand()
        elif dealer.totalPoints > 21:
            return('Dealer is busted! YOU WIN!!!')
        elif dealer.totalPoints > player.totalPoints:
            return('Dealer has higher points! YOU LOSE!!!')
        elif dealer.totalPoints <= player.totalPoints:
            dealer.hit(deck)
            dealer.showHand()

prompt = Game()
print(prompt)
