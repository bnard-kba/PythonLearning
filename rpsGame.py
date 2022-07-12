import random, sys

print('ROCK,PAPER,SCISSORS')

#keep track of wins/draws/losses

wins = 0
draws = 0
losses = 0


while True:  #loop for the game

    print('%s Wins, %s Losses, %s Draws' %(wins,losses,draws))

    #player loop
    while True:
        print('Make your move: (r)ock, (p)aper, (s)cissors, or (q)uit')

        playerMove = input()

        if playerMove =='q':
            sys.exit()
        
        if playerMove == 'r' or 'p' or 's':
            break
       



    #Display what player chose:

    if playerMove == 'r':
        print('ROCK versus....')
    
    elif playerMove == 'p':
        print('PAPER versus...')

    elif playerMove =='s':
        print('SCISSORS versus...')
    
   

    

    #Computer selecting a choice
    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')

    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    
    else:
        print('SCISSORS')

     # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        draws = draws + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1