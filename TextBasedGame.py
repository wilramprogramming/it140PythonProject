#Wilon Ramirez

#show_status function. To be displayed every time they enter a room.
def show_status(current_room, inventory, rooms):
    print(f'You have entered the {current_room}.\n'
          f'The item(s) you currently have in your inventory  are: {", ".join(inventory)}.\n')#this adds a seperator and displays the items in the players inventory


#instructions function. To be displayed at the start of the game
def show_instructions():
    print('Welcome to Space, Great Escape!!! \n'
          'You are a scoundrel of a lieutenant officer, who got thrown into the brig for starting a bar fight. \n '
          'As you were sound asleep, the ship was boarded by a shape shifting alien who killed your entire crew.\n'
          'Your job is to collect all the items and fight the alien invader!!! \n'
          'Here are the controls and rules. \n'
          'You can only go North, South, East, West or Exit. \n'
          'Type the direction you wish to go, or type Exit to exit the game. \n'
          'If you find an item, you will be promted to type yes or no to pick it up\n'
          'If you enter a room where the Alien is located before collecting all the items, \n'
          'you will most likely die. \n')

#List of directions. It made it easier to illiterate through the rooms loop
directions = ['North', 'South', 'East', 'West']

#Had to create this to create the win condition of finding all the items before finding the Alien
required_items = {'Security Key Card', 'Pizza', 'Lead Pipe', 'Self destruct codes',
                   'Warp Drive Anti-Chamber Key Card', 'Shuttle Key Card', 'Laser rifle',
                   'Anti-matter Bomb', 'Armory Key Card', 'Towel', 'Space Suit'}

#main  function where the code will run.
def main():
    #dictionary of rooms, representing the game map.
    rooms = {
        'Brig': {'West': 'Security Room'},
        'Security Room': {'East': 'Brig', 'North': 'Mess Hall', 'item': 'Security Key Card'},
        'Mess Hall': {'South': 'Security Room', 'West': 'Corridor P', 'North': 'Docking Hatch', 'East': 'Bathrooms', 'item': 'Pizza'},
        'Corridor P': {'East': 'Mess Hall', 'South': 'Captains Quarters', 'West': 'Bridge', 'North': 'Shuttle Bay', 'item': 'Lead Pipe'},
        'Captains Quarters': {'North': 'Corridor P', 'item' : 'Self destruct codes'},
        'Bridge': {'East': 'Corridor P', 'item': 'Shape Shifting Alien'},
        'Shuttle Bay': {'South': 'Corridor P', 'item': 'Warp Drive Anti-Chamber Key Card'},
        'Docking Hatch': {'South': 'Mess Hall', 'East': 'Armory', 'item': 'Shuttle Key Card'},
        'Armory': {'West': 'Docking Hatch', 'East': 'Engineering Room', 'item': 'Laser rifle'},
        'Engineering Room': {'West': 'Armory', 'item': 'Anti-matter Bomb'},
        'Bathrooms': {'West': 'Mess Hall', 'North': 'Showers', 'East': 'Crew Quarters', 'item': 'Armory Key Card'},
        'Showers': {'South': 'Bathrooms', 'item': 'Towel'},
        'Crew Quarters': {'West': 'Bathrooms', 'item': 'Space Suit'}
    }


#initializing the variable, current_room to brig as the starting point for the player. Also initialising inventory to an empty list
    current_room = 'Brig'
    inventory = []
    #Calling the show_instructions method so it can be displayed to the player before entering the loop.
    show_instructions()

    while True:
        #Calling the show_status function to display current room and inventory.
        show_status(current_room, inventory, rooms)

        player_choice = input('So tell me escape artist, which direction would you like to go? ').strip().capitalize()

        #If statement to give a way to quit the game if couldnt find alien and want to stop playing
        if player_choice == 'Exit':
            print('Thanks for playing! Goodbye!')
            break

        if player_choice in directions:#First if to confirm that the player typed a valid input.
            if player_choice in rooms[current_room]:#Second if to confirm if there is a room in the direction typed.
                current_room = rooms[current_room][player_choice]#Updates the current_room variable.... to the current room.


                if rooms[current_room].get('item') == 'Shape Shifting Alien':# Check if the current room contains the alien item
                    if required_items.issubset(set(inventory)):#this checks if the player has all the items
                        print(
                            "Congratulations! You have collected all the items and defeated the shape shifting alien. You win!")
                        break  # End the game with a win
                    else:
                        print(
                            "Oh no, you have encountered the shape shifting alien and you do not have all the items yet! Game over.")
                        break  # End the game with a loss

                # Check if the current room contains an item
                if 'item' in rooms[current_room] and rooms[current_room]['item'] is not None:
                    item = rooms[current_room]['item']
                    while True:
                        pick_up_item_response = input(f'There is a {item} here! Do you want to pick it up? (yes/no)').strip().lower()#prompts the player if they want to pick up the item
                        if pick_up_item_response == 'yes':
                            inventory.append(item)#adds item to inventory
                            rooms[current_room]['item'] = None
                            break
                        elif pick_up_item_response == 'no':
                            break
                        else:
                            print("Invalid entry. Please type 'yes' or 'no' only.")#If player inputs anything else but yes or no, to picking item up prompt
            else:
                print("You can't go that way.") #If player chooses a direction not connected to a room
        else:
            print("Invalid input. Please enter a valid direction or type 'Exit' to be warped to the exit.\n")# If player inputs anything else but 'North', 'South', 'East', 'West', when prompted to enter a direction to go.


if __name__ == "__main__":
    main()


#For reference when I expand the code.
'''items = {
    'Security Room': 'Security Key Card', #Needed to unlock the docking hatch.
    'Mess Hall': 'Pizza', #If picked up, chance of defeating Alien up by %25
    'Corridor P': 'Lead Pipe',
    'Captains Quarters': 'Self Destruct Codes', #needed to self destruct the ship, using the Engineering room
    #'Bridge': 'Shape Shifting Alien',
    'Shuttle Bay': 'Warp Drive Anti-Chamber Key Card', #Needed to get the Anti-matter material , to create a bomb.
    'Docking Hatch': 'Shuttle Key Card', #Needed to escape using a shuttle located at the Shuttle bay
    'Armory': 'Laser rifle ', #Guarantees a win if you enter a room where the alien is in.
    'Engineering Room': 'Anti-matter Bomb', #Can be used to kill the  Alien..... and you.
    'Bathrooms': 'Armory Key Card', #Used to enter the Armory and the Engineering room
    'Showers': 'Towel', #Rule number 1, never panic!!!
    'Crew Quarters': 'Space Suit' #Would be useful if you decided to escape via the Docking hatch
}'''