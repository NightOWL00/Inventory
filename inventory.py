# Perfection 100%

import os
import ast
import time

# Global Variable start
if os.path.exists("datafile.txt") == False: # to create the file "datafile.txt"
    f = open("datafile.txt", 'w')
    f.close()

# Global Variable end

# Functions
def ADD_ITEM(item):
    location = input("-> Location of item : ")
    date_of_keeping = input("-> Date of item : ")
    itemlist = [item, location, date_of_keeping]
    return itemlist


def EDIT_ITEM():
    what_to_do = input("-> EDITING Functions :\n1 for REMOVE_ITEM\n2 for UPDATE_ITEM \n")
    choice = 'y'
    while choice == 'y':
        item_to_edit = input("-> Item to be removed/updated : \n").lower()
        list_of_items = get_from_txt_file()
        for i in list_of_items:
            if i[0] == item_to_edit:        # Checking if the itemname given in the file matches the item_to_edit
                choice = 'n'
                
                if what_to_do == '1':           # Case for Removing a item
                    UPDATE_ITEM(item_to_edit, list_of_items)
                    print("{} Removed !\n".format(item_to_edit))
                    break
                
                elif what_to_do == '2':         # Case for Updating a item
                    edited_items = ADD_ITEM(i[0])
                    UPDATE_ITEM(edited_items[0],list_of_items)
                    open("datafile.txt","a").write(str(edited_items)+'\n')      # Adding/Updating the item after removing the old one.
                    print("\n{} Updated !\n".format(item_to_edit))
                    break

        if choice == 'y':
            choice = input("Item not found !\nTry Again? (y/n) : \n").lower()


def UPDATE_ITEM(edited_items, list_of_items):
    inventory_edited = open("datafile.txt","w")
    for i in list_of_items :
        if i[0] != edited_items:        # All items are added except the item which you wanted to remove/update.
            inventory_edited.write(str(i)+'\n')
    inventory_edited.close()


def SHOW_ITEMS(specific):
    f = get_from_txt_file()
    for i in f:
        if i[0] ==specific:
            print("\n-> Item name : {} \n   Location : {} \n   Date of keeping : {} \n".format(i[0],i[1],i[2]))
            break
    else:
        print("Item does not exist\n")


def add_to_txt_file(data):
    with open("datafile.txt",'a+') as f:
        f.write(data)


def get_from_txt_file():
    all_item_list=[]
    with open("datafile.txt",'r') as f:
        for i in f.read().splitlines():
            all_item_list.append(ast.literal_eval(i))
    return all_item_list


# main program 

run = True
print("\n-->> Welcome to the Inventory <<--\n")
while(run == True):
    choice = input(
        "Functions are: \n- > 1 for Adding an item \n- > 2 for Editing the item in inventory \n- > 3 for showing all items in inventory \n- > 4 for exiting the program\nEnter choice: ")
    
    if choice == '1':
        item = input("-> Add item : ")
        add_to_txt_file(str(ADD_ITEM(item))+"\n")
        print("\nItem added !\n")

    elif choice == '2':
        EDIT_ITEM()
                
    elif choice == '3':
        if len(get_from_txt_file()) == 0:
            print("\nInventory Empty !\n")
        else :
            print("\nItems in inventory are: ",end=' ')
            for i in get_from_txt_file():
                    print('< '+i[0],end=' > ')
            specific_item = input("\nEnter item to find: ")
            SHOW_ITEMS(specific_item)
        
    elif choice == '4':
        print("\nExiting program...")
        time.sleep(0.5)  # for sexy flow
        run = False
    else:
        print("Wrong choice. Please try again.\n")

# When testing un-comment the following code for ease
# print("Removing datafile.txt")
# os.remove("datafile.txt")
