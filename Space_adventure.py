import time

def Introduction():
    print("Welcome to 'The Space Explorer'!")
    time.sleep(1)
    print("You are Captain Mueez, an astronaut on a solo mission in deep space.")
    time.sleep(1)
    print("Your ship, the Starlight Voyager, is malfunctioning, and you must make decisions to survive.\n")
    time.sleep(1)

def Make_Choice(choices):
    print("\nChoose your action:\n ") 
    for i,choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
        time.sleep(1)

    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))

            if 1 <= choice <= len(choices):
                return choice
            
            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Enter a number.")

def Repair_ship():
    print("Your ship's engine is malfunctioning.")
    print("You can attempt to repair it.")
    choices = ["Attempt to repair the engine.", "Ignore the engine issue and explore nearby asteroids."]
    choice = Make_Choice(choices)

    if choice == 1:
        print("\nYou start repairing the engine.")
        time.sleep(2)

        print("Success! The engine is back online, and you continue your mission.")
        time.sleep(1)
        return True
    
    else:
        print("\nYou decide to explore nearby asteroids, hoping to find resources.")
        time.sleep(2)
        print("Unfortunately, you encounter a space anomaly that damages your ship. Game over.")
        time.sleep(1)
        return False
    
def Alien_Encounter():
    print("\nAs you explore deeper into space, you come across an unknown alien civilization.")
    time.sleep(2)

    print("They seem peaceful and offer to share advanced technology with you.")
    choices = ["Accept the alien's offer.", "Decline and continue your mission."]
    choice = Make_Choice(choices)

    if choice == 1:
        print("\nYou accept the alien's offer and receive advanced technology.")
        time.sleep(2)
        print("This technology helps you navigate through space more efficiently.")
        time.sleep(2)
        print("The aliens also share knowledge about the mysterious anomalies.")
        time.sleep(2)
        print("Armed with this information, you avoid potential dangers in your journey.")
        time.sleep(2)
        return True
    
def Space_Anomalies():
    print("\nWhile traveling through the vastness of space, you encounter strange anomalies.")
    time.sleep(2)
    print("One of them is a cosmic storm that could disrupt your ship's systems.")
    choices = ["Navigate through the storm.", "Take a detour and avoid the storm."]
    choice = Make_Choice(choices)

    if choice == 1:
        print("\nYou decide to navigate through the cosmic storm.")
        time.sleep(2)
        print("It's a risky maneuver, but your ship weathers the storm successfully.")
        time.sleep(1)
        print("Your courage earns you respect among space explorers.")
        time.sleep(1)
        return True
    
    else:
        print("\nYou take a detour to avoid the cosmic storm.")
        time.sleep(2)
        print("While you avoid immediate danger, the detour increases your travel time.")
        time.sleep(1)
        print("You arrive at your final destination later than planned.")
        time.sleep(1)
        return False
    
def Final_Destination():
    print("\nYou reach the final destination of your space exploration.")
    time.sleep(2)
    print("There are two planets in sight: one lush and habitable, the other barren and desolate.")
    choices = ["Land on the lush planet.", "Land on the barren planet."]
    choice = Make_Choice(choices)

    if choice == 1:
        print("\nYou land on the lush planet and discover a new home for humanity.")
        time.sleep(2)
        print("Congratulations! You successfully complete your space exploration.")
        time.sleep(1)
        return True
    else:
        print("\nYou land on the barren planet and struggle to survive.")
        time.sleep(2)
        print("Unfortunately, the lack of resources leads to your mission failure. Game over.")
        time.sleep(1)
        return False
    
def Play_Game():
    Introduction()

    if Repair_ship():

        if Alien_Encounter():

            if Space_Anomalies():

                if Final_Destination():
                    print("\nYou are hailed as a hero of space exploration. Congratulations!")
                else:
                    print("\nYour mission ends in challenges, but you persevere. Better luck next time.")

            else:
                print("\nYour encounter with space anomalies adds complexities to your mission.")
                time.sleep(2)
                print("Despite the challenges, you continue your exploration with determination.")
                time.sleep(1)
                print("In the end, you achieve a moderate success in your mission.")
        
        else:
            print("\nYou continue your mission without the help of alien technology.")
            time.sleep(2)
            print("Your journey through space is challenging, but you persevere.")
            time.sleep(1)
            print("In the end, you achieve a moderate success in your mission.")

    else:
        print("\nYour attempt to repair the ship fails, and you drift aimlessly in space. Game over.")

if __name__ == "__main__":
    Play_Game()