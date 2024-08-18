#Wilon Ramirez

def show_status(current_room, inventory, rooms):
    print(f'You have entered the {current_room}.\n'
          f'The item(s) you currently have are: {", ".join(inventory)}.\n')



def show_instructions():
    #The instructions and letting the player know the initial room they are in.
    print('Welcome to Space, Great Escape!!! \n'
          'You are a scoundrel of a lieutenant officer, who got thrown into the brig for starting a bar fight. \n '
          'As you were sound asleep, the ship was boarded by a shape shifting alien who killed your entire crew.\n'
          'Your job is to collect all the items and fight the alien invader!!! \n'
          'Here are the controls and rules. \n'
          'You can only go North, South, East, West or Exit the game. \n'
          'Type the direction you wish to go, or type Exit to exit the game. \n'
          'If you enter a room where the Alien is located before collecting all the items, \n'
          'you will most likely die. \n')


directions = ['North', 'South', 'East', 'West']
required_items = {'Security Key Card', 'Pizza', 'Lead Pipe', 'Self destruct codes',
                   'Warp Drive Anti-Chamber Key Card', 'Shuttle Key Card', 'Laser rifle',
                   'Anti-matter Bomb', 'Armory Key Card', 'Towel', 'Space Suit'}

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


#initializing the variable, current_room to brig as the starting point for the player.
    current_room = 'Brig'
    inventory = []
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)

        player_choice = input('So tell me escape artist, which direction would you like to go? ').strip().capitalize()

        if player_choice == 'Exit':
            print('Thanks for playing! Goodbye!')
            break

        if player_choice in directions:
            if player_choice in rooms[current_room]:
                current_room = rooms[current_room][player_choice]

                # Check if the current room contains the alien item
                if rooms[current_room].get('item') == 'Shape Shifting Alien':
                    if required_items.issubset(set(inventory)):
                        print(
                            "Congratulations! You have collected all the items and defeated the shape shifting alien. You win!")
                        break  # End the game with a win
                    else:
                        print(
                            "Oh no, you have encountered the shape shifting alien and you do not have all the items yet! Game over.")
                        break  # End the game with a loss

                # Check if the current room contains an available item
                if 'item' in rooms[current_room] and rooms[current_room]['item'] is not None:
                    item = rooms[current_room]['item']
                    pick_up_item_response = input(f'There is a {item} here! Do you want to pick it up? (yes/no)').strip().lower()
                    if pick_up_item_response == 'yes':
                        inventory.append(item)
                        # Remove the item from the room after picking it up
                        rooms[current_room]['item'] = None
                        break
                    elif pick_up_item_response == 'no':
                        break
                    else:
                        print("Invalid entry. Please type 'yes' or 'no' only.")

            else:
                print("You can't go that way.")
        else:
            print("Invalid input. Please enter a valid direction or type 'Exit' to be warped to the exit.\n")


if __name__ == "__main__":
    main()

"""    while True:
        show_status(current_room, inventory, rooms)

        player_choice = input(
            'So tell me escape artist, which direction would you like to go?').strip().capitalize()

        if player_choice not in directions:
            print("Invalid input. Please enter a valid direction or type 'Exit' to be warped to the exit.\n")
            continue

        for direction in directions:
            new_room = rooms[current_room][direction]
            current_room = new_room

            # Check if the current room contains an available item
            if 'item' in rooms[new_room]:
                print(f'There is a {rooms[new_room].get("item")[0]["name"]} here! Do you want to pick it up? (yes/no)')
                # Prompt user for input and handle their choice
                if input().lower() == 'yes':
                    inventory.append(rooms[new_room]['item'])

            else:
                if 'item' in rooms[new_room]:
                    inventory.append(rooms[new_room]['item'])

            print(f'You are in the {current_room}.')

        # Check if the current room contains the alien item
        if 'Shape Shifting Alien' in [i['name'] for i in rooms[current_room].get('item', [])]:
            print("Oh no, you have encountered the shape shifting alien! Game over.")
            break  # End the game when encountering the alien"""



'''items = {
    'Security Room': 'Security Key Card', #Needed to unlock the docking hatch.
    'Mess Hall': 'Pizza', #If picked up, chance of defeating Alien up by %25
    'Corridor P': 'Lead Pipe',
    'Captains Quarters': 'Self Destruct Codes', #needed to self destruct the ship, using the Engineering room
    #'Bridge': 'Shape Shifting Alien',
    'Shuttle Bay': 'Warp Drive Anti-Chamber Key Card', #Needed to get the Anti-matter material , to create a bomb.
    'Docking Hatch': 'Shuttle Key Card', #Needed to escape using a shuttle located at the Shuttle bay
    'Armory': 'Laser rifle ', #Garentees a win if you enter a room where the alien is in.
    'Engineering Room': 'Anti-matter Bomb', #Can be used to kill the  Alien..... and you.
    'Bathrooms': 'Armory Key Card', #Used to enter the Armory and the Engineering room
    'Showers': 'Towel', #Rule number 1, never panic!!!
    'Crew Quarters': 'Space Suit' #Would be useful if you decided to escape via the Docking hatch
}'''