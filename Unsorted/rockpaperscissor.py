# Rock , paper , scissor game
import os
import random

# globals0
rps = ('r', 'p', 's')
choiceYes = ('Y', 'y')
choiceNo = ('N', 'n')

# game
class rpsGame:
    playerScore = 0
    aiScore = 0
       
    def getPlayerName(self):
        rpsGame.playerName = input('Enter your name: ')
    
    def showScore(self):
        # clearScreen()
        print('***********S*C*O*R*E*******************')
        print()
        print(f'{self.playerName}  won {self.playerScore} rounds')
        print(f'AI won {self.aiScore} rounds')
        print()
        print('***************************************')
        print()
        
    def playerTurn(self):
        self.playerChoice = (input(f'Your turn {self.playerName} Rock,Paper,Scissor (r / p / s) ')).lower()
        while self.playerChoice not in rps:
            self.playerChoice = (input(f'Your turn {self.playerName} Rock,Paper,Scissor (r / p / s) ')).lower()
        

    def aiTurn(self):
        for i in range(5): self.aiChoice = random.choice(rps)
        print(f'AI choice {self.aiChoice}')


    def playerWon(self):
        rpsGame.playerScore += 1


    def aiWon(self):
        rpsGame.aiScore += 1        
        

    def whoWon(self):

        if self.playerChoice == 'r':    # Rock
            
            if self.aiChoice == 'p':
                print('Paper covers Rock. AI Won')
                self.aiWon()
            else:
                print(f'Rock blunt Scissors. {self.playerName} won')
                self.playerWon()
        
        elif self.playerChoice == 'p':  # Paper

            if self.aiChoice == 'r':
                print(f'Paper covers Rock. {self.playerName} won')
                self.playerWon()
            else:
                print('Scissors cut Paper. AI Won')
                self.aiWon()

        else:                           # Scissor
            if self.aiChoice == 'r':
                print('Rock blunt Scissors.  AI Won')
                self.aiWon()
            else:
                print(f'Scissors cut Paper. {self.playerName} won')
                self.playerWon()

    
    def __init__(self):
        # initialize
        rpsGame.playerScore = 0
        rpsGame.aiScore = 0   
        
        self.getPlayerName() # get player name

        i = 0
        while i < 5:
            print()
            self.playerTurn()
            self.aiTurn()
            if self.playerChoice == self.aiChoice: # it's a tie
                print('It\'s a tie. Try again')
            else:    
                self.whoWon()    
                i += 1

        
        
            

# Show rules
def showRules():
    clearScreen()
    print('***************************************')
    print('*** Welcome to Rock Paper Scissors ***')
    print('***************************************')
    print()
    print('Rules ')
    print('1. Rock blunt Scissors')
    print('2. Paper coverd Rock')
    print('3. Scissors cut Paper')
    print('4. Each game has 3 turns')
    print()


 
# clear screen
def clearScreen():
    os.system('CLS')


def main():
    # show the rules    
    showRules()

    # Ask the user if they want to play
    gameChoice = 'y'
    while gameChoice in choiceYes:
        gameChoice = input('Do you want to play a game (Y/N)')

        if gameChoice in choiceYes:
            # start new game
            newGame = rpsGame()
            
            # show score
            newGame.showScore()
            
            # reset game state for next round
            gameChoice = 'y'

        elif gameChoice in choiceNo:
            # exit
            print('Have a nice day !!!')
            exit
        else:
            continue    

    

if __name__ == "__main__":
    main()
