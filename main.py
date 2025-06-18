import sys
import findDuplicateModule
import schedule
import DeleteDuplicateModule
import time

def main():
    if len(sys.argv) == 2 and (sys.argv[1] == '--u' or sys.argv[1] == '--U'):
        print("This automation script deletes duplicate files from the given directory.")
        print("Usage: python script.py <directory_path> <sender_email> <receiver_email> <interval_minutes>")
    
    elif len(sys.argv) == 2 and (sys.argv[1] == '--h' or sys.argv[1] == '--H'):
        print("Enter command line arguments: directory path, sender email, receiver email, interval in minutes.")
    
    elif len(sys.argv) == 5:
        directory = sys.argv[1]
        sender = sys.argv[2]
        receiver = sys.argv[3]

        try:
            interval = int(sys.argv[4])
        except ValueError:
            print("Invalid time interval. Please provide an integer value in minutes.")
            return

        print(f"Scheduler started: checking every {interval} minute(s)...")

        schedule.every(interval).minutes.do(
            lambda: DeleteDuplicateModule.DeleteDuplicate(directory, sender, receiver)
        )

        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Invalid arguments.")
        print("Usage:")
        print("  --u or --U for usage")
        print("  --h or --H for help")
        print("  python script.py <directory_path> <sender_email> <receiver_email> <interval_minutes>")

if __name__ == "__main__":
    main()
