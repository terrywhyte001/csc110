def adventure_game():
    print("Welcome to the Adventure Game!")
    input("Press Enter to start...")
    print("You are in a dark forest, and you have to make a choice to survive the night.")
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
    choice1 = input("Which one do you want to pick up? (MATCH/FLASHLIGHT) ").strip().upper()

    if choice1 == "MATCH":
        print("\nYou pick up the match and strike it. For an instant, the forest around you is illuminated.")
        print("You see a large grizzly bear, and then the match burns out.")
        choice2 = input("Do you want to RUN or HIDE behind a tree? ").strip().upper()
        
        if choice2 == "RUN":
            print("\nYou sprint as fast as you can, but the bear starts chasing you.")
            choice3 = input("Do you CLIMB a tree or KEEP RUNNING? ").strip().upper()
            
            if choice3 == "CLIMB":
                print("\nYou scramble up a tree just in time. The bear growls but eventually leaves.")
                print("You survive the night safely. Congratulations!")
            elif choice3 == "keep running":
                print("\nYou keep running, but you trip over a root! The bear catches up, and... well, it was a good run.")
            else:
                print("\nInvalid choice. The bear catches up while you're confused.")

        elif choice2 == "HIDE":
            print("\nYou quickly hide behind a tree, holding your breath.")
            choice3 = input("Do you STAY still or THROW a rock to distract the bear? ").strip().upper()
            
            if choice3 == "STAY":
                print("\nThe bear sniffs around but doesn't notice you. After a while, it leaves. You survive!")
            elif choice3 == "THROW":
                print("\nYou throw a rock, but it accidentally hits the bear! It turns and charges at you.")
                print("Game over.")
            else:
                print("\nInvalid choice. The bear hears you and finds you.")

        else:
            print("\nInvalid choice. The bear sees you hesitating and attacks.")

    elif choice1 == "FLASHLIGHT":
        print("\nYou pick up the flashlight and turn it on.")
        print("You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
        choice2 = input("Do you want to FOLLOW the path or LOOK in the trees for the noise? ").strip().upper()
        
        if choice2 == "FOLLOW":
            print("\nYou follow the path and find a cabin with lights on. You are safe for the night!")
        elif choice2 == "LOOK":
            print("\nYou investigate the trees and discover a hidden cave.")
            choice3 = input("Do you ENTER the cave or GO BACK to the path? ").strip().upper()
            
            if choice3 == "ENTER":
                print("\nInside the cave, you find an old treasure chest. You are rich!")
            elif choice3 == "GO BACK":
                print("\nYou return to the path and safely reach a cabin. You survive the night.")
            else:
                print("\nInvalid choice. You get lost in the woods.")

        else:
            print("\nInvalid choice. You wander aimlessly until morning.")

    else:
        print("\nInvalid choice. You stand there too long, and something approaches from the darkness...")

# Start the game
adventure_game()
   