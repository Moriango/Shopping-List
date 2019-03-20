import os
import time

shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def addList(item):
    if(shopping_list):
        position = input("Where should I add {}?\n"
                        "Press Enter to add to the end of the list\n"
                        "> ".format(item))
    else: 
        position = 0
    try: 
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
        print("Item Added to the Cart!")
        time.sleep(1)
        clear_screen()
    else: 
        shopping_list.append(item)
        print("Item Added to the Cart!")
        time.sleep(1)
        clear_screen()

def showList():
    clear_screen()
    print("====================================================\nYou have a total of {} item(s) in your shopping cart\n====================================================".format(len(shopping_list)))
    print("Shopping List\n=============")
    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
        index += 1
    print("="*10)

def removeItem():
    showList()
    index = input("Which item number would you like to remove\n> ")
    try: 
        if(index.isdigit()):
            del shopping_list[(int(index)-1)]
        else:
            shopping_list.remove(index)
    except ValueError:
        pass
    showList()

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE, STOP, FINISHED or CLEAR' to stop adding items.
\n---------------------------------\n
Enter 'Help' for the help menu.
\n---------------------------------\n
Enter 'SHOW' to display the current shopping list.
\n---------------------------------\n
Enter 'REMOVE' to remove an item by name or number from the shopping cart.
    """)

show_help()

while True:
    new_item = input("> ")

    if new_item.lower() in {'done', 'finished', 'stop', 'clear'}:
        break
    elif new_item.lower() == 'help':
        show_help()
        continue
    elif new_item.lower() == 'show':
        showList()
        continue
    elif new_item.lower() == 'remove':
        removeItem()
        continue
    else:
        addList(new_item)
        continue