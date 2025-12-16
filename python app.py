# basic_title = "The Book of Mormon"
# final_rating = "4.5"
# is_completed = True
# notes_taken = "256"
# print(f"Title:{basic_title}\n Rating:{final_rating}\n Completion:{is_completed}\n Notes:{notes_taken}") 


#--------------------------------   Printing out the variable above
# notes_on_next_chapter = int(notes_taken) + 5
# print()
# print("-----BOOKS-----")
# print()
# print(f"Title:{basic_title}")
# print(f"Rating:{final_rating}")
# print(f"Completion:{is_completed}")
# print(f"Notes:{notes_taken}")
# print(f"Expected notes for next chapter:{notes_on_next_chapter}")
# print()

#--------------------------------   Dictionary being print out with key and value
# bookshelf = {
#     "Book":"Pride and Prejudice\n",
#     "Rate":"8.5/10\n",
#     "Genre":"Regioncy Romance\n",
# }

# for key, value in bookshelf.items():
#     print(f"{key}: {value}")

#--------------------------------   Allowing input and displaying
# first_name =input("What is your name: ")
# last_name = input("What is your last name: ")
# age = input("What is your age: ")
# bank_account_checking = float(input("How much is in your checking account? "))
# print(f"Your full name is: {last_name}, {first_name}")
# print(f"You are {age} years old")
# print(f"Checking account balance: ${bank_account_checking:,.2f}")

#--------------------------------   If and then with the same problem
# pin = int(input("What is your pin: "))
# checking_balance = 20000000000000


# if pin != 2002:
#     print("Incorrect pin, Try again")

# else:
#     print("Welcome Fernando")
#     print(f"Checking Balance: ${checking_balance:,.2f}")

#--------------------------------   While loop until the answer is correct
checking_balance = 20000000000000
pin = 2002

while True:
    
    pin_input = int(input("What is your pin: "))

    if pin_input == pin:
        print("Welcome Fernando")
        print(f"Checking Balance: ${checking_balance:,.2f}")
        break
    else:
        print("Incorrect pin, Try again")
        print()
print("Thank you for visiting Wells Fargo, Have a nice day!")





 

