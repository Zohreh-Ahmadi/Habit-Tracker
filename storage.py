# storage.py
import json
import os
import datetime
from habit import Habit

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "habits.json")

def save_habits(habits):
    data = [
        {
            "name": h.name,
            "periodicity": h.periodicity,
            "creation_date": h.creation_date.isoformat(),
            "completion_dates": [d.isoformat() for d in h.completion_dates]
        }
        for h in habits
    ]
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_habits():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    habits = []
    for item in data:
        h = Habit(item['name'], item['periodicity'])
        h.creation_date = datetime.datetime.fromisoformat(item['creation_date'])
        h.completion_dates = [datetime.datetime.fromisoformat(d) for d in item['completion_dates']]
        habits.append(h)
    return habits
