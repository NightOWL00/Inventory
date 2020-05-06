"""
[summary of tool]

An item in inventory is defined as {item_name: [string Location, date Date_of_keeping, boolean Location_changed(Y/N)]}

Functions:

-> ADD_ITEM 
    --> item_name
    --> location
    --> date_of_keeping
    --> location_changed(Default=No)
    --> Exit_add_menu

-> EDIT_ITEM
    --> item_to_edit
    --> Choose_what_to_edit
        ---> Enter_new_info
    --> Exit_edit_menu

-> REMOVE_ITEM
    --> item_to_remove
    --> Exit_remove_menu

-> SHOW_ITEMS

-> EXIT
-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-

EXAMPLE OF INVENTORY ITEMS:
dict inventory={}
inventory[item]=['my college bag','4-May-2020',NO]
print(inventory)

o/p: {item_1:['my college bag','4-May-2020',NO]}

"""


inventory = dict()
def ADD_ITEM():
    item = input("-> Add item: ")
    location = input("-> Location of item: ")
    date_of_keeping = input("-> Date of item: ")
    location_changed = input("-> Location changed: ")
    data=[location,date_of_keeping,location_changed]
    inventory[item]=data


def EDIT_ITEM():
    pass


def REMOVE_ITEM():
    pass


def SHOW_ITEMS():
    pass


flag = True
while flag != False:
    print(
        "Functions are: \n1 for ADD_ITEM \n2 for EDIT_ITEM \n3 for REMOVE_ITEM \n4 for SHOW_INVENTORY \n5 for EXIT"
    )
    choice = input().lower()
    if choice == "1":
        ADD_ITEM()

    elif choice == "2":
        EDIT_ITEM()

    elif choice == "3":
        REMOVE_ITEM()

    elif choice == "4":
        SHOW_ITEMS()
        print(inventory)

    elif choice == "5":
        print("Exiting program")
        flag = False
    else:
        print("Wrong choice. Try again")
