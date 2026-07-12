# ---------------------------------- The Terminal Text-RPG Habit Tracker (Beginner) ----------------------------------

# \\\\ Modules ////

import random
import time

# \\\\ Variables, Inputs and loops ////

name = input("What's your first name ? ").strip().capitalize()
print(f"Your name is {name}")
print("-" * 10)

max_hp = 100
print(f"You max HP is {max_hp}")
print("-" * 10)

player1 = {                         # Player Data
    "current_health" : 60,
    "attack" : 5,
    "defense" : 10,
}

boss1 = {                           # Boss Data
    "name" : "Golem",
    "max_hp" : 100,
    "attack" : 25,
}


for key, value in player1.items():      # Display player stats

    print(f"Your {key} is {value}")
    
    if key == "defense":

        print("#" * 50)

    else:

        print("-" * 10)


# \\\\ Functions ////

def buffs1():

    player1["current_health"] += 10
    player1["attack"] += 5
    player1["defense"] += 10
    print(f"Your health is buffed ! It becomes {player1['current_health']}")    
    print(f"Your attack power is buffed ! It becomes {player1['attack']}")    
    print(f"Your defense is buffed ! It becomes {player1['defense']}")
    print("-" * 10)    

def buffs2():

    print("-" * 10)
    player1["current_health"] += 10
    player1["attack"] += 5
    player1["defense"] += 10
    print(f"Your health is buffed ! It becomes {player1['current_health']}")    
    print(f"Your attack power is buffed ! It becomes {player1['attack']}")    
    print(f"Your defense is buffed ! It becomes {player1['defense']}")
    print("#" * 10)

# Checking if healthy habits have been done or not

water_intake = input("Have you drunk water since morning ? 'Yes' or 'No' ? ").strip().capitalize()
print("-" * 10)

if water_intake == "Yes":

    buffs1()

elif water_intake == "No":

    pass

else:

    while water_intake not in ["Yes", "No"]:

        print("Wrong Input")

        water_intake = input("Have you drunk water since morning ? 'Yes' or 'No' ? ").strip().capitalize()

        print("-" * 10)

        if water_intake == "Yes":

            buffs1()    

            break

        elif water_intake == "No":

           break



healthy_food = input("Did you eat healthy food ? 'Yes' or 'No' ? ").strip().capitalize()
print("-" * 10)

if healthy_food == "Yes":

    player1["current_health"] += 10
    player1["attack"] += 5
    player1["defense"] += 10    
    print(f"Your health is buffed ! It becomes {player1['current_health']}")    
    print(f"Your attack power is buffed ! It becomes {player1['attack']}")    
    print(f"Your defense is buffed ! It becomes {player1['defense']}")
    print("-" * 10)

elif healthy_food == "No":

    pass

else:

    while healthy_food not in ["Yes", "No"]:

        print("Wrong Input")

        healthy_food = input("Did you eat healthy food ? 'Yes' or 'No' ? ").strip().capitalize()

        print("-" * 10)

        if healthy_food == "Yes":

            buffs1()    

            break

        elif healthy_food == "No":

           break


exercise = input("Have you done exercises ? 'Yes' or 'No' ? ").strip().capitalize()
print("-" * 10)

if exercise == "Yes":

    buffs1()

elif exercise == "No":

    pass
else:

    while exercise not in ["Yes", "No"]:

        print("Wrong Input")

        exercise = input("Have you done exercises ? 'Yes' or 'No' ? ").strip().capitalize()

        print("-" * 10)

        if exercise == "Yes":

            buffs1()    

            break

        elif exercise == "No":

           break

sleep = input("Have you slept for 7-9 hours ? 'Yes' or 'No' ? ").strip().capitalize()


if sleep == "Yes":
    
    buffs2()

elif sleep == "No":
    print("#" * 10)
    pass

else:

    while sleep not in ["Yes", "No"]:

        print("Wrong Input")

        sleep = input("Have you slept for 7-9 hours ? 'Yes' or 'No' ? ").strip().capitalize()

        print("#" * 10)

        if sleep == "Yes":

            buffs2()    

            break

        elif sleep == "No":

           break

if water_intake == "No" and healthy_food == "No" and exercise == "No" and sleep == "No":
    
    print("#" * 50)
    print("Your health didn't improve. Try harder !")
    print("#" * 50)

else:
   
    for key, value in player1.items():

        print(f"Your {key} is {value}")
   
        if key == "defense":

            print("#" * 50)

        else:

            print("-" * 10)


if player1["current_health"] <= 70:         # Check the compatibility of the battle

    print("You can't fight. You are weak !")

else:

    print("----------------------------\nThe battle has started !\n----------------------------")

    time.sleep(3)

    while player1["current_health"] > 0 and boss1["max_hp"] > 0:

        while player1["defense"] > 0:

            damage_to_boss = random.randint(5, player1["attack"])

            boss1["max_hp"] -= damage_to_boss

            if boss1["max_hp"] <= 0:

                break

            else:
        
                print(f"{name} dealt {damage_to_boss} to the {boss1['name']}. The {boss1['name']}'s health becomes {boss1['max_hp']}")


            time.sleep(4)

            damage_to_player = random.randint(10, boss1["attack"])

            player1["defense"] -= damage_to_player

            if player1["defense"] <= 0:
            
                print(f"The {boss1['name']} breaked {name}'s defense !")

            else:

                print(f"The {boss1['name']} attacked ! {name}'s defense downgrades to {player1['defense']}")


            time.sleep(4)

        damage_to_boss = random.randint(5, player1["attack"])

        boss1["max_hp"] -= damage_to_boss

        if boss1["max_hp"] <0:

            print(f"{name} killed the {boss1['name']} !")
            

        if boss1["max_hp"] <= 0:

            break

        else:
            
            print(f"{name} dealt {damage_to_boss} to the {boss1['name']}. The {boss1['name']}'s health becomes {boss1['max_hp']}")


        time.sleep(4)

        damage_to_player = random.randint(10, boss1["attack"])

        player1["current_health"] -= damage_to_player

        if player1["current_health"] < 0:
            
            print(f"The {boss1['name']} killed {name}")

        else:

            print(f"The {boss1['name']} attacked ! {name}'s health downgrades to {player1['current_health']}")


        time.sleep(4)

    if player1["current_health"] > 0:

        print(f"Victory ! {name} has made it ! Keep healthy")

    else:

        print(f"Game Over ! The healthier {name} is, the stronger {name} will be")


time.sleep(10)