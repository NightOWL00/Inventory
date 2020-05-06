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

import time

inventory = dict()


def ADD_ITEM(item):
    location = input("-> Location of item : ")
    date_of_keeping = input("-> Date of item : ")
    location_changed = input("-> Location changed : ")
    data = [location, date_of_keeping, location_changed]
    inventory[item] = data
    return inventory


def EDIT_ITEM():
    choice = 'y'
    bp = 0
    while choice == 'y':
        item_to_edit = input("-> Item to be edited : ").lower()
        print()
        inventory_file_read = open(
            "D:/Github/Inventory/inventory_text_data.txt", "r+")
        for i in inventory_file_read.readlines():
            # Below if statement is checking if the key of the key-value pair in the txt file is equal to the given item or not.
            # both item_to_edit and the key from the txt file are converted to lower case to reduce the error of inequality.
            file_item = i.split(":")[0].lower()
            if file_item == item_to_edit:
                choice = 'n'
                edited_items = ADD_ITEM(file_item)
                # CHANGES()
                print(edited_items)
                break
        if choice == 'y':
            choice = input("Item not found !\nTry Again? (y/n) : ").lower()
            print()
    inventory_file_read.close()


def REMOVE_ITEM():
    pass


def SHOW_ITEMS():
    pass


def CHANGES():
    pass

def Add_to_txt_file(data):
    inventory=dict()
    with open("inventory_test_data.txt",'a') as f:
        f.write(data)

    

flag = True
while flag != False:
    print("Functions are: \n1 for ADD_ITEM \n2 for EDIT_ITEM \n3 for REMOVE_ITEM \n4 for SHOW_INVENTORY \n5 for EXIT")
    choice = input().lower()
    if choice == "1":
        item = input("-> Add item : ")
        data=str(ADD_ITEM(item))
        data=data[1:-1]
        print(data)
        # {'01': ['laasd', 'uu', 'gdddgd'], '02': ['asf', 'dgng', 'etjt'], '03': ['asfj', 'agssga', 'asgnas'], '04': ['pqp', 'rpr', 'rwr'], '05': ['hhh', 'www', 'rrr']}
        Add_to_txt_file(data)

    elif choice == "2":
        EDIT_ITEM()

    elif choice == "3":
        REMOVE_ITEM()

    elif choice == "4":
        SHOW_ITEMS()
        print(inventory)

    elif choice == "5":
        print("Exiting program...")
        time.sleep(1)
        flag = False
    else:
        print("Wrong choice. Try again")
