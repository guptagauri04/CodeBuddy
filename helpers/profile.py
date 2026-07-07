import json
from datetime import date

FILE_PATH = "data/profile.json"


def load_profile():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_profile(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def get_profile():

    data = load_profile()

    if data["name"] == "":

        print("\n👋 Welcome to CodeBuddy!")
        print("Let's set up your profile.\n")

        data["name"] = input("Enter your name: ")
        data["favorite_language"] = input("Favorite programming language: ")
        data["joined_date"] = str(date.today())

        save_profile(data)

    return data