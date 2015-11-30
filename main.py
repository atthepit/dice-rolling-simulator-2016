__author__ = 'Pedro'

if __name__ == '__main__':
    NO_ANSWER = 'N'
    YES_ANSWER = 'Y'

    import random
    from DiceSimulator import Dice
    dice = Dice(random)

    answer = YES_ANSWER
    while(answer.capitalize() != NO_ANSWER):
        print(dice.roll())
        answer = input('Roll again (y/N):') or NO_ANSWER
