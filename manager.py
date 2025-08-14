# manager.py
from habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        return habit

    def list_habits(self):
        return self.habits

    def list_by_periodicity(self, periodicity):
        return [h for h in self.habits if h.periodicity == periodicity]
