#import important modules
import random

# initialising variables (info we are storing/track)

# player state
player_name = input('Enter your name: ')
prod_points = 0
game_stage = 1  # Start at stage 1: Wake Up
bucket_points = 200     # current cumulated productivity points

# game state
game_state = True

## main game loop -- to keep game continously running
while game_state == True:
      
    ## branches (control flow)
    if game_stage == 1:

        print(f"Good morning, {player_name}")    #use f-string!
        print('Options: ')
        print('1: Stretching exercise')
        print('2: Reach for phone')
        q1 = int(input('What do you want to do now? (Enter 1 or 2):  '))
        
        if q1 == 1:
            print('You feel energized!')
            prod_points = prod_points + 1
            game_stage = 2  # Move to next stage (Time Check)
        elif q1 == 2:
            print('You wasted 30 minutes scrolling.')
            prod_points = prod_points - 1
            game_stage = 2 # Move to next stage (Time Check)
        else:
            print('Wrong Input')

    elif game_stage == 2:
        print("\nIt's time to check the clock and eat breakfast.")
        time_score = int(input('What time is it? ')) # simple variable for time

        if time_score < 9:
            print("It's early! You have time for a proper breakfast.")
            menu = ['Eggs & Toast', 'Oatmeal', 'Fruit Smoothie']
            meal = random.choice(menu)
            print(f'You decide to make {meal}.')
            prod_points += 1 # Add point for healthy homemade breakfast
            game_stage = 3 # Move to next stage
        
        else:
            print("It's late. You skip breakfast.")
            prod_points -= 1
            game_stage = 3 # Move to next stage
        
    elif game_stage == 3:
        print("It's 5 PM! Choose your after work activity")
        print("Option 1: Gym")
        print("Option 2: Sleep")
        q2 = int(input('After work activity: '))

        if q2 == 1:
            print('You feel energized!')
            prod_points += 1
            game_stage = 4
        elif q2 == 2:
            print('Not a good time to sleep')
            prod_points -= 1
            game_stage = 4
        else:
            print("Wrong Input")
        
    elif game_stage == 4:
        print("Your bed time is in 40 minutes: ")
        print("Option 1: Skincare and read")
        print("Option 2: Tiktok")
        q3 = int(input('Before sleeping: '))

        if q3 == 1:
            print('What a healthy way to end your evening!')
            prod_points += 1
            game_stage = 5
        elif q3 == 2:
            print('At least wash your face first next time!')
            prod_points -= 1
            game_stage = 5
        else:
            print("Wrong Input")
    
    elif game_stage == 5:
        print("\n--- End of the Day Summary ---")
        print(f"{player_name}, your productivity score is: {prod_points}")
        
        if prod_points >= 1:
            print("You had a healthy, productive routine today! Self-treat bucket list time!")
        else:
            print("You had a less productive day. Time to reset tomorrow.")
        
        game_state = False # This finally exits the main 'while' loop and ends the program

bucket_points = bucket_points + prod_points
shopping_points = 230
remaining_points = shopping_points - bucket_points
print('Your current balance in your productivity bank is ', bucket_points, ' points')
print(f"{remaining_points} points away to unlock your shopping perks!")
print("Keep going, stay healthy and stay productive!")










    