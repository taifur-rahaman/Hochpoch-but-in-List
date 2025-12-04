user_list = [2, 3, 4, 5, 2, 3, 2, 1, 8]

unique_list = []

for item in user_list:
    if item not in unique_list:
        unique_list.append(item)

sorted_list = unique_list.sort()

print(sorted_list)