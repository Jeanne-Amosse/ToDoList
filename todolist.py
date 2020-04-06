from tabulate import tabulate
import os

items = []

def draw_table(items):
    content = [[i, elem] for i,elem in enumerate(items)]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(tabulate(content, headers=["id", "todo list"]))
    

draw_table(items)


while (True):
    print("1) Add an item    2) Delete item   3) Modify")
    choice = int(input())
    
    if (choice == 1):
        print("What task should I add?")
        text = input()
        items.append(text)
        
    if (choice == 2):
        print("Which item do you want me to delete?")
        id = int(input())
        del items[id]
        

    if (choice == 3):
        print("Which task should I modify?")
        id = int(input())
        print("Please enter new task")
        new = input()
        items[id]= new

    draw_table(items)



    
