from datetime import date, timedelta
import json

FILE_PATH = "data/streak.json"

def load_streak_data():
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_streak_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def update_streak():
    data = load_streak_data()

    today = date.today()
    last_date_str = data["last_date"]

    if last_date_str == "":
        data["current_streak"] = 1

    else:
        last_date = date.fromisoformat(last_date_str)

        if last_date == today:
            pass

        elif last_date == today - timedelta(days=1):
            data["current_streak"] += 1

        else:
            data["current_streak"] = 1

    if data["current_streak"] > data["longest_streak"]:
        data["longest_streak"] = data["current_streak"]

    data["last_date"] = today.isoformat()
    save_streak_data(data)

    return data
