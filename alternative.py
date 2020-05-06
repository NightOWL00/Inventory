# Perfection 100%

import os
import ast
import time

# Global Variable start
if os.path.exists("datafile.txt") == False:
    f = open("datafile.txt", 'w')
    f.close()

# Global Variable end

# Definitions


def ADD_ITEM(item):
    location = input("-> Location of item : ")
    date_of_keeping = input("-> Date of item : ")
    location_changed = input("-> Location changed : ")
    itemlist = [item, location, date_of_keeping, location_changed]
    print("\nItem added !\n")
    return itemlist


def EDIT_ITEM():
    what_to_do = input("-> EDITING Functions :\n1 for REMOVE_ITEM\n2 for UPDATE_ITEM \n")
    choice = 'y'
    bp = 0
    while choice == 'y':
        item_to_edit = input("-> Item to be removed/updated : ").lower()
        print()
        list_of_items = get_from_txt_file()
        inventory_file_read = open("datafile.txt", "r+")
        for i in list_of_items:
            if i[0] == item_to_edit:
                choice = 'n'
                
                if what_to_do == '1':           # Case for Removing a item
                    UPDATE_ITEM(item_to_edit, list_of_items)
                    print("\nItem Edited !\n")
                    choice = 'n'
                    break
                
                elif what_to_do == '2':         # Case for Updating a item
                    edited_items = ADD_ITEM(i[0])
                    UPDATE_ITEM(edited_items[0],list_of_items)
                    open("D:/Github/datafile.txt","a").write(str(edited_items)+'\n')
                    print("\nItem Edited !\n")
                    inventory_file_read.close()
                    break
        
        if choice == 'y':
            choice = input("Item not found !\nTry Again? (y/n) : ").lower()
            print()


def UPDATE_ITEM(edited_items, list_of_items):
    
    inventory_edited = open("D:/Github/datafile.txt","w")
    for i in list_of_items :
        if i[0] != edited_items:
            inventory_edited.write(str(i)+'\n')
    inventory_edited.close()


def SHOW_ITEMS():
    f = get_from_txt_file()
    for i in f:
        print("\n->Item name : {} \n  Location : {} \n  Date of keeping : {} \n  Location Changed : {}".format(i[0],i[1],i[2],i[3]))
    print()


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
while(run == True):
    choice = input(
        "Functions are: \n1 for ADD_ITEM \n2 for EDIT_ITEM \n3 for SHOW_INVENTORY \n4 for EXIT\n")
    
    if choice == '1':
        item = input("-> Add item : ")
        data = str(ADD_ITEM(item))
        add_to_txt_file(data+"\n")

    if choice == '2':
        EDIT_ITEM()
        pass
                
    if choice == '3':
        print("Items in inventory are: ",end=' ')
        for i in get_from_txt_file():
            print(i[0],end=', ')
        print()
        SHOW_ITEMS()
        
    if choice == '4':
        print("Exiting program")
        time.sleep(0.5)  # for sexy flow
        run = False

print("removing datafile for ease")
os.remove("datafile.txt")