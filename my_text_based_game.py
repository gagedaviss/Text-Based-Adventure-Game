


def show_instructions():
    """Display the game objective and available commands."""
    #Print main menu commands
    print("=================================\n")
    print("Welcome to the Wizard Text Adventure Game!\n")
    print("=================================\n")
    print("You must collect all 6 items to defeat the dark wizard")
    print("Move commands: go south, go north, go east, go west")
    print("To add item to inventory: get 'item name' \n")
    
def get_item(item, current_room, inventory):
    pass

def show_status(current_room, inventory, rooms):

    print(f"Current Room: {current_room}")

    print(f"Items in inventory {inventory}")

    print(f"-------------------\n")
    
    return 

    
    
command_list = ["north", "south", "east", "west"]

def main():
    
    
    rooms = {
    "Dungeon": {"west": "Hall of Chains", "north": "Guard Tower"},
    "Hall of Chains": {"north": "Abandoned Armory", "east": "Dungeon", "item": 'Iron Key'},
    "Abandoned Armory": {"north": "Alchemist Lab", "south": "Hall of Chains", "item": "Knights Sword"},
    "Alchemist Lab" : {"east": "Forbidden Library", "south": "Abandoned Armory", "item": "Healing Potion"},
    "Forbidden Library": {"east": "Ruined Chapel", "west": "Alchemist Lab", "item": "Spellbook"},
    "Ruined Chapel": {"south": "Dark Wizard Sanctum", "west": "Forbidden Library", "item": "Holy Relic"},
    "Dark Wizard Sanctum": {"west": "Guard Tower", "north": "Ruined Chapel", "item": "Dark Wizard"}
    }

    # TODO: Set the player's starting room.
    current_room = "Dungeon"

    # TODO: Create the player's inventory.
    inventory = []

    # TODO: Call the instruction function at the appropriate time.
    show_instructions()

    
    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    while True:

        show_status(current_room=current_room, inventory=inventory, rooms=rooms)

        user_command = input("Enter Move, or exit (Ex. go south): ")
        #if user enters exit break out of the game loop
        if user_command.lower().strip() == "exit":
            print("Thanks for playing!")
            break
    #extract the user_command and turn it into a list
        direction = user_command.lower().split()

    #check to make sure the list contains more than 1 argument and no more than 2
        if (len(direction) == 0 or len(direction) > 2):
            print("Please enter a possible command: go north, go south, go east, go west")

    #check if command entered matches one of the available commands
        elif direction[-1] not in command_list:
            print("Please enter a possible command: go north, go south, go east, go west")

    #check if the user entered the available command options
        elif direction[0] != "go" and direction[0] not in command_list:
            print("Please enter a possible command: go north, go south, go east, go west")

    #check if the user entered 2 directional commands
        elif len(direction) == 2 and direction[0] in command_list and direction[-1] in command_list:
            print("Please only enter one move command (Ex. go south or south)")

    #IF all checks pass update the current room 
        else:
            if direction[-1] in rooms[current_room]:
                current_room = rooms[current_room][direction[-1]]

            
            
