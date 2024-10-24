#Hard code a dictionary
myFoodDictionary = {
    "Banana" : "Yellow, long, and seedless. Just don't let this one split us apart.",
    "Apple" : "Mostly red, can be green, keeps the doctors away... mostly.",
    "Asparagus" : "This green vegetable also doubles as the primary weapon for a Roman Legionary.",
    "Orange" : "What came first, the fruit or the color?",
    "Pasta" : "No one knows for sure where it came from, but many believe that the italians did it best."
}

#Define main 
def main():
    #Print out the menu
    menu()

    #Continue until the user exits the program
    while(True):
        #Get the users input
        user_input = input("Your input: ")
        print()
        #If users wants to continue, continue
        if(user_input.lower() != "done"):
            if(user_input == "1"):
                print_list()
            elif(user_input == "2"):
                add_item_to_dict()
            elif(user_input == "3"):
                find_item()
            elif(user_input == "4"):
                print_keys()
            else:
                print("Option not found, please try again!\n")
        #Break if the user wants to exit the program 
        else:
            count = 0
            for item in myFoodDictionary:
                count += 1
            #Print out the count of add entires, there are 5 hard coded items in the list
            print(f"You added a total of: {count - 5} entries for a grand total of {count} entries!")
            print("Good bye!")
            break

#Create a menu for the program output
def menu():
    print("\tWelcome to my program!")
    print("\nPlease pick an option listed below:")
    print("\nPrint list: 1")
    print("Add item to list: 2")
    print("Find item from list: 3")
    print("Print the list of answers to the list questions: 4")
    print("Exit program: Done\n")

def print_list():
    print("Can you guess the food for each of these desciptions? \n")
    for item in myFoodDictionary:
        print(myFoodDictionary[item])
    print()

def add_item_to_dict():
    temp_food = input("What class of food would you like to add? (Fruit, starch, etc...) ")
    temp_food_des = input("What is a short description of this food ")
    if(temp_food.lower != "done"):
        myFoodDictionary[temp_food] = temp_food_des
    else:
        print("Can't add \"done\" to the list\n")

def find_item():
    item_to_be_found = input("What would you like to find? ")
    for item in myFoodDictionary:
        if(item.lower() == item_to_be_found.lower()):
            print(f"{item_to_be_found} was found!")
            return
    print(f"{item_to_be_found} was not found in the list.\n")

def print_keys():
    for item in myFoodDictionary:
        print(item)
    print()

#Run main program
main()