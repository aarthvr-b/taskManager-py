# CLI Entry point

from manager import TaskManager
from task import Task
from utils import TaskInput

manager = TaskManager()

task0 = TaskInput(1, "Finish the Task Manager Project", False, "medium")
task1 = TaskInput(2, "Go to sleep", False, "easy")
task2 = TaskInput(3, "Eat sushi", True, "easy")

tasks = [task0, task1, task2]

for task in tasks:
    print(manager.add_task(task))

for line in manager.list_tasks():
    print(line)
