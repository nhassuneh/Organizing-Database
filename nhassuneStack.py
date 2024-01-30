class Idea():#Node
    def __init__(self, title = "No title", task = "No task", next = None):
        self.title = title
        self.task = task
        self.next = next
    
class Organizer():#Stack
    def __init__(self, top = None):
        self.top = top
    
    def empty(self):
        if self.top == None:
            return True
        elif self.top != None:
            return False
    
    def peek(self):
        return(self.top)

    def push(self, title, task):
        item = Idea(title, task)
        if self.top == None:
            self.top = item
        else:
            item.next = self.top
            self.top = item

    def pop(self):
        if self.top == None:
            print()
        else:
            popped = self.top
            self.top = self.top.next
            return popped

def main():
    switch = True
    print("Welcome to your organizing Database!")
    database = Organizer()
    while switch == True:
        selection = int(input("Please choose whether to place an item, remove an item, view the top item, or close the database (1,2,3,4) \n 1) Place an Item\n 2) Remove an Item \n 3) View the top item \n 4) Close Database " ))
        if selection == 1:
            titleselect = input("Please input a title for your item ")
            taskselect = input("Please input a task for your item ") 
            database.push(titleselect, taskselect)
        elif selection == 2:
            popped = database.pop()
            if popped == None:
                print("No Items Inserted")
            else:
                x = popped.title
                y = popped.task
                print(f"You have completed this title: {x} and this task: {y}")
        elif selection == 3:
            if database.peek() == None:
                print("No Items Inserted")
            else:    
                print(f"Your top thing to do is this title: {database.peek().title} and this task: {database.peek().task}")
        elif selection == 4:
            print("Your database has now been closed")
            switch = False
            

main()