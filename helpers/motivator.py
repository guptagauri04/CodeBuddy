import random

messages = [
    "You don’t need motivation. Just start.",
    "Just 5 minutes. You can stop after that.",
    "Starting is the hardest part.",
    "You showed up. That already counts.",
    "Code a little today. Thank yourself later."
]

def get_message():
    return random.choice(messages)
