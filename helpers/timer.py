import time

def start_timer(minutes):
    seconds = minutes * 60

    print(f"\n⏳ Timer started for {minutes} minutes.")
    print("Focus on coding...")

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60

        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)

        seconds -= 1

    print("\n✅ Time’s up! Good job for showing up.")
