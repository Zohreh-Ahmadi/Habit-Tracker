# analytics.py
def all_habits(habits):
    return list(habits)

def all_habits(habits):
    return list(habits)

def filter_by_periodicity(habits, periodicity):
    return [h for h in habits if h.periodicity == periodicity]

def longest_streak(habits):
    if not habits:
        return 0, None
    longest = 0
    best_habit = None
    for h in habits:
        s = h.get_streak()
        if s > longest:
            longest = s
            best_habit = h.name
    return longest, best_habit

def longest_streak_for_habit(habit):
    return habit.get_streak()

