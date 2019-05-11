from random import randint


def diceGame(amt=100):
    win = 0
    count = 0
    while amt > 0:
        count += 1
        (a,b)=(randint(1,6),randint(1,6))
        if (a+b) == 7:
            amt += 4
            win += 1
        else:
            amt -= 1
    print('Not sufficient amount for next roll\n')
    print(count,'times you played the game and '+str(win)+'times you win and only wining amount is :'+str(win*4))
    return 0

if __name__ == '__main__':
    print('--------Welcome on Dice game-----------')
    while 1:
        amount=int(input('Enter the amount of money wish to invest:'))
        diceGame(amount)
        if input('Do you want to play again(Y or N):') !='Y':
            break
    print('.......Thanks for playing....')
