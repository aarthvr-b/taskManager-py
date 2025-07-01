"""Contains all types of the project"""

from dataclasses import dataclass


@dataclass
class TaskInput:
    taskId: int
    description: str
    is_completed: bool
    difficulty: str
