from Tasks_Manager import task_manager
from Tasks import personal_task,work_task

def main():
    manager=task_manager()
    
    while True: 
        print("1.Add Personal tasks\n2.Add Work task\n3.Search for a task by name\n4.Show Tasks By Date ")
    
        choice=input("Select Option : ")
        print(choice)
        if choice=='1':
            name=input("Enter name of Task : ")
            due_date=input("Enter input date :")
            task=personal_task(name,due_date)
            manager.add_task(task)
        
        elif choice=='2':
            name=input("Enter name of Task :")
            due_date=input("Enter input date :")
            task=work_task(name,due_date)
            manager.add_task(task)
    
        elif choice=='3':
            search_input=input("Enter Task name to search : ")
            input_search=search_input.lower()
            result = manager.search_task(input_search)
            print(result)
        
        elif choice=="4":
            input_date=input("Enter Date as dd-mm-yyyy : ")
            result=manager.view_tasks_by_date(input_date)
            print(f"Personal task for {input_date}\n")
            print(result['PERSONAL'])
            print(f"Professional task for {input_date}\n")
            print(result['WORK'])
            
        else :
            print("Invalid choice!")
    
        
if __name__=="__main__":
    main()