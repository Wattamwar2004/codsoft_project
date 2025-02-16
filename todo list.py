def display_menue():
    print("menue")
    print("1. view tasks")
    print("2. add task")
    print("3. remove task")
    print("4. exit")    
def view_tasks(tasks):
    if not tasks:
        print("your list is empty")
    else:
        print("your list")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
                
def add_task(tasks):
    task = input("enter the new task: ").strip()
    if task:
        tasks.append(task)
        print(f"task '{task}' has been added")
    else:
        print("task cannot be empty")                     
def remove_task(tasks):
    if not tasks:
        print("your list is empty")
        return
                        
    try:
        view_tasks(tasks)
        task_number = int(input("enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"task '{removed_task}' has been removed")
        else:
            print("invalid task number")
    except ValueError:
        print("invalid input enter new number")
                                    
def to_do_list_app():
    tasks = []
    while True:
        display_menue()
        choice = input("your choice (1/2/3/4): ").strip()
                                            
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("exciting the to do list.")
            break
        else:
            print("invalid choice.")
            