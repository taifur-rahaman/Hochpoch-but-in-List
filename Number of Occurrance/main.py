def input_list():
    user_list = []
    while True:
        print("Want to Input a Number: ")
        choice = input("Enter your choice (y/n): ")
        
        match choice:
            case "y":
                try:
                    user_list.append(int(input(f"Enter a Number: ")))
                except ValueError:
                    print("Please give appropiate Data Type")
            case "n":
                return user_list


user_list = [1, 2, 4, 2, 1, 4, 2, 5]

unique_element = []

for element in user_list:
    if element not in unique_element:
        unique_element.append(element)

for element in unique_element:
    print(f"{element}: {user_list.count(element)}")

