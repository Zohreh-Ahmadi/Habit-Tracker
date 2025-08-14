# tests/test_habits.py
import unittest
from habit import Habit
from analytics import all_habits, filter_by_periodicity, longest_streak, longest_streak_for_habit

class TestHabit(unittest.TestCase):
    def setUp(self):
        self.h1 = Habit("Drink water", "daily")
        self.h2 = Habit("Clean house", "weekly")
        self.h3 = Habit("Meditate", "daily")
        self.h1.completion_dates = ["2025-08-01", "2025-08-02"]
        self.h2.completion_dates = ["2025-07-20", "2025-07-27"]
        self.h3.completion_dates = []

    def test_creation(self):
        self.assertEqual(self.h1.name, "Drink water")
        self.assertEqual(self.h1.periodicity, "daily")
    
    def test_mark_completed(self):
        initial_len = len(self.h3.completion_dates)
        self.h3.mark_completed()
        self.assertEqual(len(self.h3.completion_dates), initial_len + 1)
    
    def test_get_streak(self):
        self.assertEqual(self.h1.get_streak(), 2)
        self.assertEqual(self.h3.get_streak(), 0)
    
    def test_all_habits(self):
        habits = [self.h1, self.h2, self.h3]
        result = all_habits(habits)
        self.assertEqual(len(result), 3)
    
    def test_filter_by_periodicity(self):
        habits = [self.h1, self.h2, self.h3]
        daily_habits = filter_by_periodicity(habits, "daily")
        self.assertEqual(len(daily_habits), 2)
    
    def test_longest_streak(self):
        habits = [self.h1, self.h2, self.h3]
        longest, name = longest_streak(habits)
        self.assertEqual(longest, 2)
        self.assertEqual(name, "Drink water")
    
    def test_longest_streak_for_habit(self):
        self.assertEqual(longest_streak_for_habit(self.h1), 2)
        self.assertEqual(longest_streak_for_habit(self.h3), 0)

if __name__ == '__main__':
    unittest.main()

