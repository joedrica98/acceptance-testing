class Task:
    def __init__(self, description):
        self.description = description
        self.status = 'Pending'

    def complete(self):
        self.status = 'Completed'

    def __repr__(self):
        return self.description


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        task = Task(task_description)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_as_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.complete()

    def remove_task(self, task_description):
        self.tasks = [task for task in self.tasks if task.description != task_description]

    def clear(self):
        self.tasks = []

    def find_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                return task
        return None
