import json
import random

TASK_FILE = "tasks.json"

def get_task(difficulty):
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)

    filtered_tasks = []

    for task in tasks:
        if task["difficulty"] == difficulty:
            filtered_tasks.append(task)

    chosen_task = random.choice(filtered_tasks)
    return chosen_task["task"]
