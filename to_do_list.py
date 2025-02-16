class Task:
    def __init__(self, task_title, task_text="", deadline="", priority="", status=False):
        self.task_title = task_title
        self.task_text = task_text
        self.deadline = deadline
        self.priority = priority
        self.status = status

class ToDoList:
    def __init__(self):
        self.task_list = []

    def task_exists(self, task_title):
        return any(task.task_title == task_title for task in self.task_list)

    def add_task(self, task_title, task_text="", deadline="", priority=""):
        if self.task_exists(task_title):
            raise ValueError(f"The task '{task_title}' already exist!")
        new_task = Task(task_title, task_text, deadline, priority)
        self.task_list.append(new_task)

    def delete_task(self, task_title):
        for task in self.task_list:
            if task.task_title == task_title:
                self.task_list.remove(task)
                return
        raise NameError("We don't have this task")

    def change_status(self, task_title, status):
        for task in self.task_list:
            if task.task_title == task_title:
                task.status = status
                return

        raise NameError("We don't have this task")

    def show_completed_tasks(self):
        completed_tasks = [task for task in self.task_list if task.status]
        if completed_tasks:
            for task in completed_tasks:
                print(task)
        else:
            raise ValueError("You don't have completed tasks")


    def show_active_tasks(self):
        for task in self.task_list:
            if not task.status:
                print(task)
        print("Congratulations, you have completed all your tasks!")
