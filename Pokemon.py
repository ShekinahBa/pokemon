import requests
import random
from pprint import pprint
import csv
import os
import time

my_score = 0
comp_score = 0
your_points = 0
comp_points = 0

def intro ():
    print("WELCOME!!!")
    time.sleep(0.5)
    print("Today you'll be playing Fred, our resident player")
    time.sleep(1.5)
    print ('Let\'s get started...\n')
    time.sleep(1)

def random_pokemon():
    # Generate a random number between 1 and 151 to use as the Pokemon ID number
    pokemon_id = random.randint(1, 151)

    # Using the Pokemon API get a Pokemon based on its ID number
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()

    # Create a dictionary that contains the returned Pokemon's name, id, height and weight
    pokemon_info = {
        "name": pokemon['name'],
        "id": pokemon['id'],
        "height": pokemon['height'],
        "weight": pokemon['weight'],
        "points": pokemon['base_experience']


    }
    return pokemon_info

# print(random_pokemon())

# Get multiple random Pokemon and let the player decide which one that they want to use


def pick_from_multiple():
    multiple_pokemon = []

    for each_poke in range(1, 6):
        the_pokemons = random_pokemon()
        multiple_pokemon.append(the_pokemons)

    pick_from = {
        1: multiple_pokemon[0],
        2: multiple_pokemon[1],
        3: multiple_pokemon[2],
        4: multiple_pokemon[3],
        5: multiple_pokemon[4],
    }
    choice_of_pokemons = pick_from

    option1 = choice_of_pokemons[1]
    option2 = choice_of_pokemons[2]
    option3 = choice_of_pokemons[3]
    option4 = choice_of_pokemons[4]
    option5 = choice_of_pokemons[5]


    #pprint(choice_of_pokemons)

    print("Pokemon Names and Stats")
    print("1: {:12} -> Height: {:2}, Weight: {:2} ".format(option1['name'].upper(),option1['height'],option1['weight'] ))
    print("2: {:12} -> Height: {:2}, Weight: {:2} ".format(option2['name'].upper(), option2['height'], option2['weight']))
    print("3: {:12} -> Height: {:2}, Weight: {:2} ".format(option3['name'].upper(), option3['height'], option3['weight']))
    print("4: {:12} -> Height: {:2}, Weight: {:2} ".format(option4['name'].upper(), option4['height'], option4['weight']))
    print("5: {:12} -> Height: {:2}, Weight: {:2} ".format(option5['name'].upper(), option5['height'], option5['weight']))



    error = True
    while error:
        try:
            pick_one = int(input("\nWhich pokemon do you want? (pick between 1-5 from above options): "))
            if pick_one > 5:
                raise ValueError
            error = False
        except ValueError:
            print("Please enter a number between 1 & 5")
        # except Exception:
        #     print("Something went wrong")

    your_choice = choice_of_pokemons[pick_one]
    print("\nYou chose {}".format(your_choice["name"].upper()))

    return your_choice

def game ():
    # 4. Get a random Pokemon for the player and another for their opponent
    my_chosen_pokemon = pick_from_multiple()
    #print("\nYour pokemon is {} ".format(my_chosen_pokemon["name"]))

    computer_rand_pokemon = random_pokemon()
    print("Fred chose {} \n".format(computer_rand_pokemon["name"].upper()))
# print(my_rand_pokemon["Pokemon Name"])


# 5. Ask the user which stat they want to use (id, height or weight)

    #----------------
    # stat_choice = input("What Stat do you want to use? (id, weight,height) ")
    # my_pokemon = my_chosen_pokemon[stat_choice]
    # computer_pokemon = computer_rand_pokemon[stat_choice]
    #------------------

    error = True
    while error:
        try:
            stat_choice = input("What Stat do you want to use? (weight,height) ")
            if stat_choice in random_pokemon():
                my_pokemon = my_chosen_pokemon[stat_choice]
                computer_pokemon = computer_rand_pokemon[stat_choice]
            else:
                raise KeyError
            error = False
        except KeyError:
            print ("Please pick one of the following stats: weight or height")
        except Exception:
            print("Something went wrong")



    global my_score
    global comp_score
    global your_points
    global comp_points

# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

    if my_pokemon > computer_pokemon:
        print("\nYour stat is {}".format(my_pokemon))
        print("The Fred's stat is {}".format(computer_pokemon))
        print("\n### ### ### ### ### ### ### ### ")
        print("\nCONGRATULATION! \nYou WIN {} points for defeating {}!\n ".format(computer_rand_pokemon['points'], computer_rand_pokemon['name']))
        print("### ### ### ### ### ### ### ### \n")
        my_score += 1
        your_points = computer_rand_pokemon['points']
        your_points += your_points



    elif computer_pokemon > my_pokemon:
        print("\nYour stat is {}".format(my_pokemon))
        print("Fred's stat is {}".format(computer_pokemon))
        print("Sorry, you LOSE! :( Fred wins {} for defeating your {}\n".format(my_chosen_pokemon['points'],my_chosen_pokemon['name']))
        comp_score += 1
        comp_points = my_chosen_pokemon['points']
        comp_points +=comp_points

    else:
        print("It's a draw!")

    # print("TEST TEST {} and comp {}".format(my_score, comp_score))

    return my_score, comp_score, your_points, comp_points



#game()


# Play multiple rounds and record the outcome of each round. The player who wins the most number rounds, wins the game
def rounds_scores ():
    global result
    global how_many_rounds
    no_rounds = 0

    error = True

    while error:
        try:
            how_many_rounds = int(input("How many rounds do you want to play? "))
            error = False
        except ValueError:
            print("Please enter a number")
        except Exception:
            print("Something went wrong")


    while no_rounds < how_many_rounds:
        for i in range (how_many_rounds):
            no_rounds +=1
            rounds_left = how_many_rounds - no_rounds
            print("\n**** ROUND {} **** You have {} rounds left ****".format(no_rounds, rounds_left))
            game()

    print("========================")
    print("G A M E  O V E R")
    print("========================")

    if my_score > comp_score:
        print("\nYour score is {} and the Fred's score is {}".format(my_score, comp_score))
        print("You win this game")
        print("\nYou get a TOTAL of {} points for defeating your opponent".format(your_points))
        result = "WIN"
    else:
        print("\nYour score is {} and the Fred's score is {}".format(my_score, comp_score))
        print("You lose this game")
        print("\nHe gets a TOTAL of {} points for defeating you".format(comp_points))
        result = "LOSE"

#Take the player's username and stores it in .csv file
def store_leaderboard ():
    username = input ("Enter your username? ")
    #points = my_score
    rounds = how_many_rounds
    finals = result
    total_points = your_points

    board = { 'Player': username,
              'Points': total_points,
              'Rounds Played': rounds,
              'Result': finals
    }

    field_names =["Player", "Points", "Rounds Played", "Result"]

    with open ("pokemon_stats.csv", "a") as pokemon_file:
        spreadsheet = csv.DictWriter(pokemon_file, fieldnames=field_names)

        #Allows you to add header if it's a new file or append if it's an existing file
        pf = "pokemon_stats.csv"
        if os.stat(pf).st_size == 0:
            spreadsheet.writeheader()
            spreadsheet.writerow(board)
        else:
            spreadsheet.writerow(board)


def read_run ():
    #Reading the pokemon stat from .csv file
    data = []
    with open("pokemon_stats.csv", "r") as pokemon_file1:
        spreadsheet = csv.DictReader(pokemon_file1)

        for row in spreadsheet:
            data.append(row)
    print("\n^^^^^^^^^^^^^^^^^^")
    print("THE LEADERBOARD:")
    print("^^^^^^^^^^^^^^^^^^")
    pprint(data)


    # Pulling out specific info
    player = []
    rounds = []
    win_lose =[]
    for data in data:
        user = data["Player"]
        round_no = int(data ["Rounds Played"])
        results = data ["Result"]


        player.append(user)

        #removing duplicates
        player = list(dict.fromkeys(player))
        win_lose.append(results)
        rounds.append(round_no)
        sum_of_round = sum(rounds)

    no_wins = 0
    no_losses = 0
    for i in win_lose:
        if i == "WIN":
            no_wins +=1
        else:
            no_losses +=1


    print ("\nLeaderboard Info:")
    print ("The players: {}".format(player))
    print("Total rounds: {}".format(sum_of_round))
    print("No of Total wins is {}, No. of Total losses is {}".format(no_wins, no_losses))

intro()
rounds_scores()
store_leaderboard()
read_run()
