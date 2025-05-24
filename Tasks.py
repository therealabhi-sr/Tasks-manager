class task:
    def __init__(self,name,due_date,priority):
        self.name=name
        self.due_date=due_date
        self.priority=priority
        self.done=False 
    
    def mark_done(self):
        self.done=True
    
        
               

class personal_task(task):
    def __init__(self,name,due_date,priority="medium"):
        super().__init__(name,due_date,priority)

        
class work_task(task):
    def __init__(self,name,due_date,priority="High"):
        super().__init__(name,due_date,priority)        