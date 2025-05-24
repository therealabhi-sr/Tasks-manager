from Tasks import task,personal_task,work_task

class task_manager:
    def __init__(self):
        self.tasks=[]
        
    def add_task(self,task):
        self.tasks.append(task)
        
    def search_task(self, input_search):
        for i in self.tasks:
            if i.name.lower()==input_search:
              return {"Task name" :i.name,
                      "Due Date":i.due_date,
                      "task priority":i.priority}
              
    def view_tasks_by_date(self,input_date):
        personal=[]
        work=[]
        for i in self.tasks:
            if(i.due_date==input_date and i.priority=="medium"):
                personal.append(i.name)
            elif(i.due_date==input_date and i.priority=="High" ):
                work.append(i.name)  
        return{
            "PERSONAL":personal,
            "WORK":work
        }  
                   
                
                
        
            
            

        