"""manages the list of tasks and task operations"""

from typing import Optional

from app.core.task import Task
from app.models.utils import TaskInput


class TaskManager:
    """This class defines a datastructure that holds Tasks.
    It will be a list."""

    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, task: TaskInput) -> str:
        added_task = Task.from_input(task)
        self.tasks.append(added_task)
        return f"Task {added_task.taskId} inserted successfully"

    def get_task_by_id(self, passedId: int) -> Task:
        for task in self.tasks:
            if passedId == task.taskId:
                return task
        raise ValueError("Task not found.")

    def delete_task(self, taskId: int) -> str:
        try:
            task_to_delete = self.get_task_by_id(taskId)
            self.tasks.remove(task_to_delete)
            return "Task deleted successfully."
        except ValueError:
            return "Task not found."

    def edit_task(
        self,
        taskId: int,
        difficulty: Optional[str] = None,
        description: Optional[str] = None,
    ) -> str:
        task_to_change = self.get_task_by_id(taskId)
        if description is not None:
            task_to_change.description = description
        if difficulty is not None:
            if difficulty not in Task.ALLOWED_DIFFICULTIES:
                raise ValueError(
                    """
                    Difficulty provided is not allowed. Use ('easy', 'medium', 'hard')
                """
                )
            task_to_change.difficulty = difficulty
        return "Task updated!"

    def toggle_completion(self, taskId: int) -> str:
        task_to_change = self.get_task_by_id(taskId)
        task_to_change.is_completed = not task_to_change.is_completed
        return f"The status of Task {taskId} switched to {task_to_change.is_completed}"

    def list_tasks(self) -> list[str]:
        task_lines = []
        for task in self.tasks:
            status = "Completed" if task.is_completed else "Pending"
            task_lines.append(
                f"Task ID : {task.taskId}\n"
                f"Task Description : {task.description}\n"
                f"Task Difficulty : {task.difficulty}\n"
                f"Task Status : {status}"
            )
        return task_lines
