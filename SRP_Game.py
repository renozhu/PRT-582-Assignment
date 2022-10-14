import random
choices = ['rock', 'scissor', 'paper']
win_list = [['scissor', 'paper'], ['paper', 'rock'], ['rock', 'scissor']] #Winning Rules
player_choices = "Player please choose from 0:rock || 1:scissor || 2:paper or choose 9 to exit:" #Player make a choice

while True:
    #Record the winning points and total games
    computer_win = 0
    player_win = 0
    total = 0
    index = 0
    #Main game to play, exit while either player wins 5 times or player can exit anytime atfer pressed 9
    while computer_win < 5 and player_win < 5:
        computer = random.choice(choices) #computer make random choice from choices list
        try:
            index = int(input(player_choices)) #Ask player to make a choice
            player = choices[index]
            
        except:
            if index != 9:
                print('\nInvalid input!!!\n')
                continue
            else:
                break    
        print('Player choices: %s, Computer choices: %s \n' % (player,computer)) #print player's and computer's choice
      
        #Compare both choices and record it
        if player == computer:
            print("Both players choose the same one. It's a tie!\n")
            total += 1
        elif [player, computer] in win_list:
            player_win += 1
            print('Player wins: %d\n' % player_win)
            total += 1
        else:
            computer_win += 1
            print('Computer wins: %d\n' % computer_win)
            total += 1
    else:
        if computer_win == 5:
            print('Computer wins 5 games, Player lose! Total number of rounds is:', total)
        else:
            print('Player wins 5 games, Computer lose! Total number of rounds is:', total)
   
    play_again = input("Play again? (y/n):")
    if play_again.lower() != "y":
        break





        
