from helpers.streak import update_streak
from helpers.tasks import get_task
from helpers.motivator import get_message
from helpers.timer import start_timer
from helpers.statistics import update_stats, get_stats
from helpers.profile import get_profile

from helpers.ui import (
    show_title,
    show_motivation,
    show_streak,
    show_task,
    show_goodbye,
    show_main_menu,
    show_statistics,
)


def main():

    # ==========================
    # Welcome Screen
    # ==========================
    show_title()

    # ==========================
    # Load User Profile
    # ==========================
    profile = get_profile()

    print(f"\n👋 Welcome back, {profile['name']}!")
    print(f"🎯 Daily Goal : {profile['daily_goal']} tasks")
    print(f"💻 Favorite Language : {profile['favorite_language']}")
    print(f"📅 Member Since : {profile['joined_date']}")

    # ==========================
    # Motivation
    # ==========================
    message = get_message()
    show_motivation(message)

    # ==========================
    # Update Streak
    # ==========================
    streak_data = update_streak()

    show_streak(
        streak_data["current_streak"],
        streak_data["longest_streak"],
    )

    # ==========================
    # Main Menu
    # ==========================
    while True:

        show_main_menu()

        choice = input("\n👉 Choose an option: ")

        # =====================================
        # START CODING
        # =====================================
        if choice == "1":

            print("\n🎯 Choose Task Difficulty")
            print("1️⃣ Easy")
            print("2️⃣ Medium")

            difficulty_choice = input("\nEnter choice: ")

            if difficulty_choice == "2":
                difficulty = "medium"
                xp_reward = 20
            else:
                difficulty = "easy"
                xp_reward = 10

            task = get_task(difficulty)

            show_task(task)

            print(f"\n⭐ Complete this session to earn {xp_reward} XP!")

            timer_choice = input(
                "\n⏱ Start a 5-minute coding session? (y/n): "
            )

            if timer_choice.lower() in ["y", "yes"]:

                start_timer(5)

                update_stats(
                    minutes=5,
                    xp=xp_reward
                )

                print("\n🎉 Progress Saved!")
                print(f"🏆 You earned {xp_reward} XP!")

            else:
                print("\n⚠ Session cancelled.")

        # =====================================
        # STATISTICS
        # =====================================
        elif choice == "2":

            stats = get_stats()

            show_statistics(stats)

        # =====================================
        # DAILY CHALLENGE
        # =====================================
        elif choice == "3":

            print("\n🎯 Daily Challenge")
            print("🚧 Coming Soon!")

        # =====================================
        # ACHIEVEMENTS
        # =====================================
        elif choice == "4":

            print("\n🏆 Achievements")
            print("🚧 Coming Soon!")

        # =====================================
        # SETTINGS
        # =====================================
        elif choice == "5":

            print("\n⚙ Settings")
            print("🚧 Coming Soon!")

        # =====================================
        # EXIT
        # =====================================
        elif choice == "6":

            show_goodbye()
            break

        # =====================================
        # INVALID INPUT
        # =====================================
        else:

            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()