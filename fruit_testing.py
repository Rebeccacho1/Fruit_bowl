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

def menu():
    print("Main function")
    my_menu = [
        ("R", "Review"),
        ("A", "Add New Fruit"),
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
        elif option == "Q":
            print("Thank You!")
            run = False
        else:
            print("Invalid Entry")

if __name__ == "__main__":
    menu()











