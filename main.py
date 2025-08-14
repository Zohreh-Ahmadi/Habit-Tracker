# main.py
# main.py
from manager import HabitManager
from storage import save_habits, load_habits
from analytics import all_habits, filter_by_periodicity, longest_streak, longest_streak_for_habit

def show_menu():
    print("\n=== Habit Tracker CLI ===")
    print("1. Add new habit")
    print("2. Show all habits")
    print("3. Complete a habit")
    print("4. Analyze habits")
    print("5. Save and Exit")

def main():
    habits = load_habits()
    manager = HabitManager()
    manager.habits = habits

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Habit name: ")
            periodicity = input("Periodicity (daily/weekly): ")
            manager.add_habit(name, periodicity)
            print("✅ Habit added!")

        elif choice == '2':
            for idx, h in enumerate(manager.habits, start=1):
                print(f"{idx}. {h.name} ({h.periodicity}) - completions: {len(h.completion_dates)}")

        elif choice == '3':
            for idx, h in enumerate(manager.habits, start=1):
                print(f"{idx}. {h.name}")
            idx = int(input("Select habit number to mark as completed: ")) - 1
            if 0 <= idx < len(manager.habits):
                manager.habits[idx].mark_completed()
                print("✅ Completed!")
            else:
                print("❌ Invalid number.")

        elif choice == '4':
            print("\n--- ANALYSIS ---")
            print("All habits:", [h.name for h in all_habits(manager.habits)])
            print("Daily habits:", [h.name for h in filter_by_periodicity(manager.habits, "daily")])
            
            longest, name = longest_streak(manager.habits)
            if name:
                print(f"Longest overall streak: {longest} ({name})")
            else:
                print("No habits found.")
            if manager.habits:
                h = manager.habits[0]
                print(f"Longest streak for '{h.name}':", longest_streak_for_habit(h))

        elif choice == '5':
            save_habits(manager.habits)
            print("💾 Data saved. Exiting...")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == '__main__':
    main()
