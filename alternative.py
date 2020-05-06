#   IDEA aka a 2d list
#  [
#       ['01', 'laasd', 'uu', 'gdddgd'],
#       ['02', 'asf', 'dgng', 'etjt'],
#       ['03', 'asfj', 'agssga', 'asgnas'],
#       ['04', 'pqp', 'rpr', 'rwr'],
#       ['05', 'hhh', 'www', 'rrr']
#   ]
import os
import ast
import time

# Global Variable start
if os.path.exists("datafile.txt") == False:
    f = open("datafile.txt", 'w')
    f.close()

invetory = []
# Global Variable end

# Definations


def ADD_ITEM(item):
    location = input("-> Location of item : ")
    date_of_keeping = input("-> Date of item : ")
    location_changed = input("-> Location changed : ")
    itemlist = [item, location, date_of_keeping, location_changed]
    print("item added")
    return itemlist


def REMOVE_ITEM():
    pass


def SHOW_ITEMS():
    f = get_from_txt_file()
    for i in f:
        print("\nItem name : {} \nLocation : {} \nDate of keeping : {} \nLocation Changed : {}".format(i[0],i[1],i[2],i[3]))


def add_to_txt_file(data):
    with open("datafile.txt",'a+') as f:
        f.write(data)

def get_from_txt_file():
    all_item_list=[]
    with open("datafile.txt",'r') as f:
        for i in f.read().splitlines():
            all_item_list.append(ast.literal_eval(i))
    # print(all_item_list)                            <------------ 2D list here
    return all_item_list

run = True
while(run == True):
    choice = input(
        "Functions are: \n1 for ADD_ITEM \n2 for EDIT_ITEM \n3 for REMOVE_ITEM \n4 for SHOW_INVENTORY \n5 for EXIT\n").lower()
    if choice == '1':
        item = input("-> Add item : ")
        data = str(ADD_ITEM(item))
        add_to_txt_file(data+"\n")

    if choice == '2':
        # do editing and
        pass

    if choice == '3':
        # do editing and
        REMOVE_ITEM()
                
    if choice == '4':
        print("Items in inventory are: ",end=' ')
        for i in get_from_txt_file():
            print(i[0],end=' ')
        SHOW_ITEMS()
        
    if choice == '5':
        print("Exixting program")
        time.sleep(0.5)  # for sexy flow
        run = False
print("removing datafile for ease")
os.remove("datafile.txt")