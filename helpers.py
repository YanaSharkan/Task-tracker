import json
import os


TASKS_FILE = "tasks.json"


# Checking that the JSON file exists
def initialize_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump({'tasks': [], 'task_id_counter': 1}, file)


# Load tasks from the JSON file
def load_tasks():
    with open(TASKS_FILE, "r") as file:
        data = json.load(file)
        return data.get('tasks', []), data.get('task_id_counter', 1)


# Save tasks to the JSON file
def save_tasks(tasks, task_id_counter):
    with open(TASKS_FILE, "w") as file:
        json.dump({'tasks': tasks, 'task_id_counter': task_id_counter}, file, indent=4)
