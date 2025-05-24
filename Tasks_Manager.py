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
            
            

        