Duplicate File Automation Script

This Python script automatically detects and deletes duplicate files from a specified directory using MD5 checksums. It generates a log file and emails it to the specified recipient at regular intervals using a scheduler.



Features

- Scans folders recursively for duplicate files.
- Compares file content using "MD5 checksums".
- Automatically deletes all duplicates, keeping one copy.
- Creates a "log file" of deleted files.
- Sends the log file via "email" using "SMTP".
- Runs on a "custom time interval" (in minutes) using a scheduler.
- Supports "command-line arguments" for full automation.



Requirements

- Python 3.x
- Internet connection (for email sending)
- A Gmail account with an **App Password** enabled

Install required packages:
```bash
pip install schedule

CommandLine input

python main.py <directory_path> <sender_email> <receiver_email> <interval_minutes>

Example

python main.py C: \Test myemail@gmail.com targetemail@gmail.com 10

