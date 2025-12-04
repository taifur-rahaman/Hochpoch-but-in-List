def food_inOrder(menu_qty):
    """
    Collects a list of food preferences from most favorite to least.
    
    menu_qty: number of items the user must enter.
    Returns a list of food names in ranked order.
    """
    friend_preference = []
    print("Enter the food from most favorite to least:\n")

    for x in range(menu_qty):
        friend_preference.append(input(f"{x + 1} : "))

    return friend_preference