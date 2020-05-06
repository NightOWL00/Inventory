#   IDEA aka a 2d list
#  [
#       ['01', 'laasd', 'uu', 'gdddgd'],
#       ['02', 'asf', 'dgng', 'etjt'],
#       ['03', 'asfj', 'agssga', 'asgnas'],
#       ['04', 'pqp', 'rpr', 'rwr'],
#       ['05', 'hhh', 'www', 'rrr']
#   ]
import os
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
    print(i for i in f)


def add_to_txt_file(data):
    with open("datafile.txt",'a+') as f:
        f.write(data)

def get_from_txt_file():
    with open("datafile.txt",'r') as f:
        all_item_list=f.readlines()
    print(all_item_list)
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
        SHOW_ITEMS()
        
    if choice == '5':
        print("Exixting program")
        time.sleep(0.5)  # for sexy flow
        run = False
print("removing datafile for ease")
os.remove("datafile.txt")