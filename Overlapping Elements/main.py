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

print("Enter Number for List 1\n")
user_list = input_list()
print("Enter Number for List 2\n")
user_list_2 = input_list()

overlapping_elements = []
unique_elements = []

for element in user_list:
    if element in user_list_2:
        overlapping_elements.append(element)
    elif element not in user_list_2:
        unique_elements.append(element)

for element in user_list_2:
    if element not in user_list:
        if element in unique_elements:
            continue
        else:
            unique_elements.append(element)
            
print(f"Overlapping Elements from both Lists are : {overlapping_elements}\n")
print(f"Unique Elements from both Lists are: {unique_elements}\n")