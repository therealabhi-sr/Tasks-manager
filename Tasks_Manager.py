from Tasks import task,personal_task,work_task

class task_manager:
    def __init__(self):
        self.tasks=[]
        
    def add_task(self,task):
        self.tasks.append(task)