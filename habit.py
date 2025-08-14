# habit.py
import datetime

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # "daily" o "weekly"
        self.creation_date = datetime.datetime.now()
        self.completion_dates = []

    def mark_completed(self):
        self.completion_dates.append(datetime.datetime.now())

    def get_streak(self):
        # Placeholder semplificato: numero di completamenti
        return len(self.completion_dates)
