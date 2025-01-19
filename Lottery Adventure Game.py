
def start_game():
    print("Welcome To Lottery Adventure Game")
    print("Start Your Adventure by choosing a path ")
    print("A: Enter the forest")
    print("B: Explore the cave")
    print("Climb the mountain")
    choice=input("Choose A,B,C").upper()
    if choice=='A':
        forest()
    elif choice=='B':
        cave()
    elif choice=='C':
        mountain()
    else:
        print("Invalid Please Choose Again")
        start_game()
def forest():
    print("\n You are in the forest. Do u want to go left or right?")
    direction=input("Enter L for left or R for right").upper()
    if direction=='L':
        print("\n You choose to go to left. Do u want to climb a tree or follow the stream? ")
        action=input("Enter T to climb a tree or S to follow a stream").upper()
        if action=='T':
            print("\n You climb a tree, but lose")
        elif action=='S':
                    print("You followed the stream and find the treasure,you win")
        else:
                    print("Invalid action Try Again")
                    forest()
    elif direction=='R':
        print("\n You choose to go right. You got lost. Game Over! ")
    else:
                print("Invalid choice.Please Choose again")
                forest()
def cave():
    print("\nYou are in the cave. Do you want to light a torch or move in the dark?")
    action = input("Enter T to light a torch or D to move in the dark: ").upper()
    if action=='T':
        print("\n You lit the torch Do u want to inspect the shiny object or avoid it?  ")
        shiny_object = input("Enter O ti inspect or avoid to A").upper()
        if shiny_object =='O':
            print("You inspected the shinny object and found a hidden treasure, You win!")
        elif shiny_object=='A':
            print("\n You avoided the shinny object but got trapped in the game, Game Over!")
        else:
            print("Invalid choice. Please try again")
            cave()
    elif action=='D':
        print("\n Its too dark You tripped and fell. Game over")
    else:
        print("invalid choice. Please try Again")
        cave()
def mountain():
     print("\n You are on the mountain do u want to take narrow path of steep climb?")
     path=input("Enter N for narrow path or S for steep climb").upper()
     if path=='N':
        print("\n You choose narrow path Do u want to rest or continue climbing?")
        action= input("Enter B to rest or C to continue climbing").upper()
        if action=='B':
           print("\n You rested and found a hidden treasure, You Win")
        elif action=='C':
          print("\n You continue climbing and fell, Game Over!")
        else:
          print("Invalid choice, Try again")
        mountain()
     elif path=='S':
        print("\n You choose the steep climb,Game Over ")
     else:
        print("Invalid choice. Please try again")
        mountain()
def replay_game():
     print("\n Do you want to play again ( Yes or No)")
     play_again= input().lower()
     if play_again=='Yes':
        start_game()
     else:
         print("Thanks For playing! Goodbye!")
         start_game()










