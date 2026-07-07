# CodeBuddy 🧑‍💻

CodeBuddy is a simple CLI-based Python application that helps me overcome procrastination and build a daily coding habit.

I built this project for myself while learning Python, with the goal of:
- reducing the mental friction of starting to code
- practicing core Python concepts in a real project
- building something small, useful, and complete

---

## 🚀 What CodeBuddy Does

When you run CodeBuddy, it:

1. Greets you with a short motivational message  
2. Tracks and displays your daily coding streak  
3. Lets you choose a task difficulty (easy / medium)  
4. Suggests one coding task for the day  
5. Offers a 5-minute coding timer to help you start  

The focus is consistency over intensity.

---

## 🧠 Why I Built This

I noticed that I often want to code, but delay starting. Once I start, I enjoy it.

So instead of relying on motivation, I built a small system that:
- removes decision fatigue
- encourages starting small
- rewards showing up regularly

CodeBuddy is not meant to be a productivity tool for everyone- it’s a personal learning project and habit-building tool.

---

## 🛠️ Technologies Used

- Python 3
- JSON (for storing data)
- Standard Python libraries only (`datetime`, `random`, `time`)

No external dependencies.

---

## 📂 Project Structure

CodeBuddy/
│
├── codebuddy.py
│
├── helpers/ 
│ ├── init.py
│ ├── streak.py 
│ ├── tasks.py 
│ ├── motivator.py 
│ └── timer.py 
│
├── data/ 
│ ├── streaks.json
│ └── settings.json
│
├── tasks.json 
│
└── README.md

---

## ▶️ How to Run

1. Make sure Python 3 is installed  
2. Clone the repository  
3. Navigate to the project folder  
4. Run:

```bash
python codebuddy.py

