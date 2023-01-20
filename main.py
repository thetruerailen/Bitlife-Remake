import configparser

# Life Simulation Game

config = configparser.ConfigParser()

# check if config file exists, if not create it with default values
if not config.read('game.ini'):
    config['DEFAULT'] = {'health': 100, 'money': 0, 'age': 0, 'happiness': 100}
    with open('game.ini', 'w') as configfile:
        config.write(configfile)

# load player's health, money and age from config file
player_health = config.getint('DEFAULT', 'health')
player_money = config.getint('DEFAULT', 'money')
player_age = config.getint('DEFAULT', 'age')
player_happiness = config.getint('DEFAULT', 'happiness')

# Happiness Level Define
def happiness(mode, amount):
    global player_happiness
    if mode == "subtract":
      player_happiness -= amount
      config['DEFAULT'] = {'health': player_health, 'money': player_money, 'age': player_happiness, 'happiness': player_happiness}
    with open('game.ini', 'w') as configfile:
        config.write(configfile)
    print("Player happiness: ", player_happiness)

    if mode == "add":
      player_happiness =+ amount
      config['DEFAULT'] = {'health': player_health, 'money': player_money, 'age': player_happiness, 'happiness': player_happiness}
    with open('game.ini', 'w') as configfile:
        config.write(configfile)
    print("Player happiness: ", player_happiness)
# main game loop
while player_health > 0:
    # display player's current health, money and age
    print("Health:", player_health)
    print("Money: $" + str(player_money))
    print("Happiness: ", player_happiness)
    print("Age: ", player_age)
    input("Press Enter to age one year")
    # get player's next action
    action = input("What would you like to do? (work, exercise, eat, shop) ")

    # handle player's action
    if action == "work" and player_age == 0 < 21:
        player_money += 100
        print("You worked and earned $10.")
        player_age += 1
        happiness("subtract", 10)
    elif action == "exercise" and player_age == 0 < 5:
        player_health += 5
        print("You exercised and gained 5 health.")
        player_age += 1
        happiness("subtract", 5)
    elif action == "eat":
        player_health += 10
        player_money -= 5
        print("You ate and gained 10 health. (-$5)")
        happiness("add", 5)
        player_age += 1
    elif action == "shop" and player_age == 0 < 16:
        player_money -= 10
        print("You shopped and spent $10.")
        player_age += 1
        happiness("add", 10)
    elif action == "reset":
        player_health = 100
        player_money = 0
        player_age = 0
        player_happiness = 100
    else:
      print("???")
      
    #save the new state of the game to the config file
    config['DEFAULT'] = {'health': player_health, 'money': player_money, 'age': player_happiness, 'happiness': player_happiness}
    with open('game.ini', 'w') as configfile:
        config.write(configfile)

# player's health has reached 0, game over
print("Your health has reached 0. Game over.")
