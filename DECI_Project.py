# text adventure game
import random
import time

# List for used in the game
adjectives = ["Good", "Great", "Nice", "Wonderful"]

# Function to pause the programme for 0.7s & print the message
def print_pause(p):
    time.sleep(0.7)
    print(p)


# Function for player score & Determine the player wins or loses
def player_score(your_score, adventurer_name, adjectives):
    if your_score >= 3:
        print_pause("Congratulations!! You Won")
    else:
        print_pause(
            f"Game Over! {random.choice(adjectives)} For Getting To This Level, {adventurer_name}"
        )

# function to allow the player to play again
def play_again():
    while True:
        play_again_input = input("Do You Want To Play Again? (y/n): ")
        if play_again_input == "y":
            play_game()
        elif play_again_input == "n":
            print_pause("Thank you for playing the Adventure Game!")
            break
        else:
            print_pause("invalid input ! please choose y or n")

# Function for the path choice
def path_choice(adjectives, your_score, adventurer_name):
    print_pause("Good Choice")
    your_score += 1
    print_pause(f"{random.choice(adjectives)} Your Score Now is {your_score}")
    print_pause("You Walk On The Path And You Meet The Deep River")
    print_pause("You Can Swim Or Search for A Bridge To Cross")
    print_pause("Enter 1 To Swim In The Water")
    print_pause("Enter 2 To Search for A Bridge")
    inp1 = input("Which Do You Choose? (1 / 2): ")
    while True:
        # If the player choose swim
        if inp1 == str(1):
            print_pause("There Are Many Crocodiles & They Eat You")
            break
        # If the player choose search for a bridge
        elif inp1 == str(2):
            print_pause("Good choice")
            print_pause("You Walk Along The River And You Find The Bridge")
            your_score += 1
            print_pause(f"{random.choice(adjectives)} Your Score Now is {your_score}")
            print_pause("Now , You Cross The River & Walk For 30 min")
            print_pause("You Find The Bad House")
            print_pause("Enter 1 To Go To It")
            print_pause("Enter 2 To Keep Walking")
            inp2 = input("Which Do You Choose? (1 / 2): ")
            while True:
                # If the player choose to go to the bad house
                if inp2 == str(1):
                    print_pause(
                        "The house is deserted, there are ghosts and they killed you"
                    )
                    break
                # If the player choose to keep walking
                elif inp2 == str(2):
                    print_pause("Good choice")
                    print_pause("The house is deserted and there are ghosts")
                    print_pause("You Keep Walking For 1 Hour & Come Out From Desert")
                    your_score += 1
                    print_pause(
                        f"{random.choice(adjectives)} Your Score Now Is {your_score}"
                    )
                    break
                inp2 = input("Which Do You Choose? (1 / 2): ")
            break
        inp1 = input("Which Do You Choose? (1 / 2): ")
    # Function for player score & Determine the player wins or loses
    player_score(your_score, adventurer_name, adjectives)


# Function for the cave choice
def cave_choice(adjectives, your_score, adventurer_name):
    print_pause("Good choice")
    your_score += 1
    print_pause(f"{random.choice(adjectives)} Your Score Now Is {your_score}")
    print_pause("You Go To The Cave Then Meet The Monster")
    print_pause("You Can Fight It Or Sneak From It")
    print_pause("Enter 1 To Fight The Monster")
    print_pause("Enter 2 To Sneak From It")
    inp1 = input("Which Do You Choose? (1 / 2): ")
    # Meeting the monster
    while True:
        # If the player choose to fight the monster
        if inp1 == str(1):
            print_pause("You Face The Monster And It ate You")
            break
        # If the player choose to sneak from the monster
        elif inp1 == str(2):
            your_score += 1
            print_pause("You came over The Monster And Continue Into The Cave")
            print_pause(f"{random.choice(adjectives)} Your Score Now Is {your_score}")
            print_pause("Now There Are Two Roads In Front Of You")
            print_pause("One Of Them Emits Light And Other Is Calm")
            print_pause("Enter 1 To Walk From The First Way")
            print_pause("Enter 2 To Walk From The Second Way")
            inp2 = input("Which Do You Choose? (1 / 2): ")
            # Two roads choices
            while True:
                # If the player choose The first road
                if inp2 == str(1):
                    your_score += 1
                    print_pause("You Walk In The First Way & You Find A Tribe There")
                    print_pause("They Show You The Way & You Come Out From The Desert")
                    print_pause(
                        f"{random.choice(adjectives)} Your Score Now Is {your_score}"
                    )
                    break
                # If the player choose the second road
                elif inp2 == str(2):
                    print_pause("You Walk A Long Distance & You Are Lost")
                    break
                inp2 = input("please choose 1/2 :")
            break
        inp1 = input("please choose 1/2 :")
    # function for player score & Determine the player wins or loses
    player_score(your_score, adventurer_name, adjectives)

# function to play the game
def play_game():
    your_score = 0
    # to take adventurer_name
    adventurer_name = input("Enter The Adventurer Name :")
    print_pause(f"Welcome {adventurer_name} , This Is The Adventure Game")
    print_pause("You Should Get 3 Points to win")
    print_pause("You Are Lost In The Desert")
    print_pause("There Is In Front Of You Cave And a Long Path")
    print_pause("Enter 1 To Walk On The Path")
    print_pause("Enter 2 To Go To The Cave")
    inp = input("Which Do You Choose? (1 / 2): ")
    while True:
        # path choice
        if inp == str(1):
            path_choice(adjectives, your_score, adventurer_name)
            break
        # cave choice
        elif inp == str(2):
            cave_choice(adjectives, your_score, adventurer_name)
            break
        inp = input("please choose 1/2 :")
    # function to allow the player to play again
    play_again()
play_game()
