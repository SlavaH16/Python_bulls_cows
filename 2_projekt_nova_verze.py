from random import sample
oddelovac = "-" * 50

def heading() -> str:
    print("""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Miloslav Houška
email: slava.89@seznam.cz
    """)
    print(oddelovac)
    print("Hi there!")
    print(oddelovac)
    print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    print(oddelovac)

def number_for_game(low_number,high_number,many_numbers) -> str:
    """
    Description:
    Creates unique random number from enter attributes to the one number in format string.
    Every position is unique, you can not have same numbers on 2 positions.
    
    low_number = lowest number
    high_number = highest number
    many_numbers = how much numbers will be (max. 9)

    Example:
    attributes = (1,9,4)

    Result:
    "3195"
    """
    random_number = ''.join(map(str,sample(range(low_number,high_number), k=many_numbers)))
    return random_number

def user_guess() -> str:
    """
    Description:
    Input function for users to guess number for game.

    """
    return input("Enter a number: ")
           
def wrong_value() -> str:

    """
    Description:
    Information for users about wrong enter number or same number.
    """
    print('''Wrong value. You don't give 4 numeric characters 
or the first number can't be 0
or you've already guessed this number.''')
    print(oddelovac)

def game_function():

    heading()

    game_number = number_for_game(1,9,4)
    game_cont = True
    user_tips = []
    #print(game_number)

    while game_cont:
        user_tip = user_guess()
        
        if user_tip.isnumeric() and user_tip[0] != '0' and len(user_tip) == 4 and user_tip not in user_tips:
            user_tips.append(user_tip)
        
            if user_tip == game_number:
                game_cont = False
                break

            result = {'bulls': 0, 'cows': 0}
        
            for index, number in enumerate(game_number):
            
                if number in user_tip and user_tip[index] == number:
                    result['bulls'] += 1    
                elif number in user_tip and user_tip[index] != number:
                    result['cows'] += 1

            if result['bulls'] < 2 and result['cows'] < 2:
                print(f'bull: {result['bulls']}, cow: {result['cows']} ') 

            if result['bulls'] < 2 and result['cows'] > 1:
                print(f'bull: {result['bulls']}, cows: {result['cows']} ') 

            if result['bulls'] > 1 and result['cows'] < 2:
                print(f'bulls: {result['bulls']}, cow: {result['cows']} ') 

            if result['bulls'] > 1 and result['cows'] > 1:
                print(f'bulls: {result['bulls']}, cows: {result['cows']} ')  

            print(oddelovac) 
 
        else:
            wrong_value()
 
    print(f'''Correct, you've guessed the right number
in {len(user_tips)} corrects guesses!''')
    print(oddelovac)
    print("That's amazing")

if __name__ == '__main__':
    game_function()