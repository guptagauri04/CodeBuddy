import json

FILE_PATH = "data/stats.json"


def load_stats():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_stats(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def update_stats(minutes, xp):
    data = load_stats()

    data["tasks_completed"] += 1
    data["study_minutes"] += minutes
    data["xp"] += xp

    # Every 100 XP = Next Level
    data["level"] = (data["xp"] // 100) + 1

    save_stats(data)


def get_stats():
    return load_stats()