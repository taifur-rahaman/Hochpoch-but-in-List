import functionalities as func

# Goal:
# Given two friends' ranked lists of favorite foods, find the food
# that both like, with the lowest combined preference score.
# Lower index = more preferred.

menu_qty = 5  # Number of items each friend must rank

# Collect food preferences from both friends
friend_1_list = func.food_inOrder(menu_qty)
friend_2_list = func.food_inOrder(menu_qty)

min_index = menu_qty             # Stores best food index from friend_1_list
index_sum = menu_qty * 2         # Stores lowest combined index found

# Loop through friend 1's list and compare with friend 2's list
for item in friend_1_list:
    if item in friend_2_list:
        # Calculate combined index for the common food
        combined_index = friend_1_list.index(item) + friend_2_list.index(item)

        # Check if this combined index is the best so far
        if combined_index < index_sum:
            index_sum = combined_index
            min_index = friend_1_list.index(item)

# Print the final selected food
print(friend_1_list[min_index])
