def get_validated_integer(m, min, max):
    while True:
        try:
            my_int = int(input(m))
        except ValueError:
            print("Sorry your entry is not correct.")
            continue
        if my_int < min:
            print("Your entry is too small")
            continue
        elif my_int > max:
            print("Your entry is too large")
            continue
        else:
            return my_int







if __name__ == "__main__":
    test = get_validated_integer("Please enter your number: -> ", 0, 5)