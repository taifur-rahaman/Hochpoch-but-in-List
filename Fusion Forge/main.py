
user_list = []

list_amount = int(input("Enter how many Integer you want to add: "))


for x in range(list_amount):
    user_list.append(input(f"{x + 1} : "))

concat_number = ""

for item in user_list:
    concat_number += item

print(int(concat_number))