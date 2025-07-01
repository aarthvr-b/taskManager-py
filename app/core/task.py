# Define Task class

from app.models.utils import TaskInput


class InvalidTaskDataError(Exception):
    """Raised when task data is invalid or incomplete."""


class Task:

    ALLOWED_DIFFICULTIES = {"easy", "medium", "hard"}

    def __init__(
        self, taskId: int, description: str, difficulty: str, is_completed: bool
    ):
        print("Initialized a new instance of Task.")
        if difficulty not in self.ALLOWED_DIFFICULTIES:
            raise ValueError(
                f"Invalid Difficulty provided: '{difficulty}'. Allowed values: {self.ALLOWED_DIFFICULTIES}"
            )
        self.taskId = taskId
        self.description = description
        self.is_completed = is_completed
        self.difficulty = difficulty

    def to_dict(self) -> dict:
        """Create a dictionary that will be my return value"""
        return {
            "taskId": self.taskId,
            "description": self.description,
            "difficulty": self.difficulty,
            "is_completed": self.is_completed,
        }

    @classmethod
    def from_input(cls, data: TaskInput) -> "Task":
        """Instanciates a new task from a dictionary passed as parameter."""
        return cls(data.taskId, data.description, data.difficulty, data.is_completed)
