#Wilon Ramirez
def show_status(current_room, inventory, rooms):
    #print players status
    #print the current inventory.
    #print an item if one located in room.

def show_instructions():
    #The instructions and letting the player know the initial room they are in.
    print('Welcome to Space, Greate Escape!!! \n'
          'You are a scoundrel of a lieutenant officer, who got thrown into the brig for starting a bar fight. \n '
          'As you were sound asleep, the ship was boarded by a shape shifting alien who killed your entire crew.\n'
          'Your job is to ESCAPE!!! \n'
          'Here are the controls and rules. \n'
          'You can only go North, South, East, West or Exit the game. \n'
          'Type the direction you wish to go, or type Exit to be warped to the exit. \n'
          'If you enter a room where the Alien is located, you will most likely die. \n')


def main():
    #dictionary of rooms, representing the game map.
    rooms = {
        'Brig': {'West': 'Security Room'},
        'Security Room': {'East': 'Brig', 'North': 'Mess Hall', 'item': 'Security Key Card'},
        'Mess Hall': {'South': 'Security Room', 'West': 'Corridor P', 'North': 'Docking Hatch', 'East': 'Bathrooms', 'item': 'Pizza'},
        'Corridor P': {'East': 'Mess Hall', 'South': 'Captains Quarters', 'West': 'Bridge', 'North': 'Shuttle Bay', 'item': 'Lead Pipe'},
        'Captains Quarters': {'North': 'Corridor P', 'Self destruct codes'},
        'Bridge': {'East': 'Corridor P', 'item': 'Shape Shifting Alien'},
        'Shuttle Bay': {'South': 'Corridor P', 'item': 'Warp Drive Anti-Chamber Key Card'},
        'Docking Hatch': {'South': 'Mess Hall', 'East': 'Armory', 'item': 'Shuttle Key Card'},
        'Armory': {'West': 'Docking Hatch', 'East': 'Engineering Room', 'item': 'Laser rifle'},
        'Engineering Room': {'West': 'Armory', 'item': 'Anti-matter Bomb'},
        'Bathrooms': {'West': 'Mess Hall', 'North': 'Showers', 'East': 'Crew Quarters', 'item': 'Armory Key Card'},
        'Showers': {'South': 'Bathrooms', 'item': 'Towel'},
        'Crew Quarters': {'West': 'Bathrooms', 'item': 'Space Suit'}
    }

#initializing the variable, current_room to great hall as the starting point for the player.
    current_room = 'Brig'
    inventory =[]
    show_instructions()

#While loop set to true. It will endlessly loop until it hits a break statement
    while True:
        #Gets players input choice.
        show_status(current_room, inventory, rooms)

        #If statement with break statement in order to exit the game.
        if current_room == 'Exit':#Change to current_room has alien to exit
            print('Too tough for you huh. Its ok. Maybe next time quitter.')
            break

        player_choice = str(input('So tell me escape artist, which direction would you like to go?').strip().capitalize())


        if player_choice not in ['North', 'South', 'East', 'West']:
            print("Invalid input. Please enter a valid direction or type 'Exit' to be warped to the exit.\n")
            continue

        #this if statement checks if the player choice leades an actual room in the dictionary. I had to create new_room and put rooms[current_room][player_choice] as its value and reassign current_room
        if player_choice in rooms[current_room]:
            new_room = rooms[current_room][player_choice]
            current_room = new_room
            print(f'You are in the {current_room}.')
        else: #else statement if the player enters the wrong direction.
            print('Sorry, but that''s a brick wall!!! \n'
                  'Dont worry. you can make another choice.')



#def dialoge():
#def pickup_item
'''items = {
    'Security Room': 'Security Key Card', #Needed to unlock the docking hatch.
    'Mess Hall': 'Pizza', #If picked up, chance of defeating Alien up by %25
    'Corridor P': 'Lead Pipe',
    'Captains Quarters': 'Self Distruct Codes', #needed to self distruct the ship, using the Engineering room
    #'Bridge': 'Shape Shifting Alien',
    'Shuttle Bay': 'Warp Drive Anti-Chamber Key Card', #Needed to get the Anti-matter material , to create a bomb.
    'Docking Hatch': 'Shuttle Key Card', #Needed to escape using a shuttle located at the Shuttle bay
    'Armory': 'Laser rifle ', #Garentees a win if you enter a room where the alien is in.
    'Engineering Room': 'Anti-matter Bomb', #Can be used to kill the  Alien..... and you.
    'Bathrooms': 'Armory Key Card', #Used to enter the Armory and the Engineering room
    'Showers': 'Towel', #Rule number 1, never panic!!!
    'Crew Quarters': 'Space Suit' #Would be useful if you decided to escape via the Docking hatch
}'''