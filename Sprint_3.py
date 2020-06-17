def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def review_fruit(m):
    for i in range (0, len(m)):
        output = "{:^13}, {}".format(m[i][0], m[i][1])
        print(output)

def add_to_fruit_bowl(m):
    add_fruit = get_string("What fruit did you want to add? ")
    new_number = get_integer("How many fruits did you want to add? ")
    my_L = [add_fruit, new_number]
    m.append(my_L)
    output = "You have {} {} added to the list.".format(new_number, add_fruit)
    print(output)

def update_quantity(m):
    for i in range(0, len(m)):
        output = "{:3} : {:^13} {}".format(i, m[i][0], m[i][1])
        print(output)
    choice_number = get_integer("Please enter the choice number to update the quantity? ")
    new_quantity = get_integer("Please enter the new quantity: -> ")
    old_quantity = m[choice_number][1]
    m[choice_number][1] = new_quantity
    output_message = "The quantity of {} has now changed from {} to {}.".format(m[choice_number][0], old_quantity, new_quantity)
    print(output_message)

def menu():
    print("Main function")
    my_menu = [
        ("R", "Review"),
        ("A", "Add New Fruit"),
        ("U", "Quantity Update"),
        ("Q", "Quit")
    ]

    my_L = [
        ["Blueberries", 0],
        ["Strawberries", 0],
        ["Apples", 0],
    ]
    run = True
    while run == True:
        for i in range(0, len(my_menu)):
            print("{} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_string("Choose option -> ")
        if option == "R":
            review_fruit(my_L)
        elif option == "A":
            add_to_fruit_bowl(my_L)
        elif option == "U":
            update_quantity(my_L)
        elif option == "Q":
            print("Thank You!")
            run = False
        else:
            print("Invalid Entry")

if __name__ == "__main__":
    menu()