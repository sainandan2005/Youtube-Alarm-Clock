#!/usr/bin/env python3

import sys
import time
import random
import argparse
import datetime
import webbrowser
from pathlib import Path


class AlarmClock:
    def __init__(self):
        self.youtube_links = []
        self.alarm_time = None
        self.youtube_links_file = None

    def load_youtube_links(self, file_path):
        try:
            file_path = Path(file_path).resolve()
            if not file_path.exists():
                print(f"Error: File {file_path} does not exist.")
                return False

            self.youtube_links_file = file_path
            with open(file_path, 'r') as file:
                self.youtube_links = [line.strip() for line in file if line.strip() and 
                                     ('youtube.com' in line or 'youtu.be' in line)]

            if not self.youtube_links:
                print("Error: No valid YouTube links found in the file.")
                return False

            print(f"Successfully loaded {len(self.youtube_links)} YouTube links.")
            return True
        except Exception as e:
            print(f"Error loading YouTube links: {e}")
            return False

    def set_alarm(self, alarm_time_str):
        try:
            time_parts = alarm_time_str.split(':')
            if len(time_parts) < 2 or len(time_parts) > 3:
                print("Error: Time should be in format HH:MM or HH:MM:SS")
                return False

            hour, minute = int(time_parts[0]), int(time_parts[1])
            second = int(time_parts[2]) if len(time_parts) == 3 else 0

            if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
                print("Error: Invalid time values. Hours (0-23), Minutes (0-59), Seconds (0-59).")
                return False

            now = datetime.datetime.now()
            alarm_time = now.replace(hour=hour, minute=minute, second=second, microsecond=0)
            
            if alarm_time < now:
                alarm_time += datetime.timedelta(days=1)

            self.alarm_time = alarm_time
            return True
        except ValueError:
            print("Error: Please enter valid numeric values for time.")
            return False
        except Exception as e:
            print(f"Error setting alarm: {e}")
            return False

    def run_alarm(self):
        if not self.youtube_links or not self.alarm_time:
            print("Error: YouTube links or alarm time not set properly.")
            return

        print(f"\nAlarm set for: {self.alarm_time.strftime('%H:%M:%S')}")
        print(f"Current time:  {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("\nPress Ctrl+C to cancel the alarm.")
        
        try:
            while datetime.datetime.now() < self.alarm_time:
                time.sleep(1)
                if datetime.datetime.now().second % 10 == 0:
                    time_left = self.alarm_time - datetime.datetime.now()
                    hours, remainder = divmod(time_left.seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print(f"\rTime remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
                    sys.stdout.flush()
            
            print("\n\nALARM! ALARM! ALARM!")
            print("Playing a random YouTube video...\n")
            
            youtube_link = random.choice(self.youtube_links)
            webbrowser.open(youtube_link)
            print(f"Playing: {youtube_link}")
            
        except KeyboardInterrupt:
            print("\nAlarm canceled by user.")
        except Exception as e:
            print(f"Error in alarm: {e}")


def create_sample_youtube_links_file():
    sample_file = Path("youtube_links.txt")
    
    if not sample_file.exists():
        sample_links = [
            "https://youtu.be/2nP3ElUtFDU?si=VlNRqGGKddgC_EZU",
            "https://youtu.be/-Djq3QihTyA?si=cqIFCf3kb7b3lIq0",
            "https://youtu.be/IpFX2vq8HKw?si=rnGvvjeEUDFZ50dC",
        ]
        
        with open(sample_file, 'w') as f:
            f.write("\n".join(sample_links))
        
        print(f"Sample YouTube links file created: {sample_file}")
        print("Feel free to edit this file to add your own YouTube links.")
    
    return sample_file


def main():
    parser = argparse.ArgumentParser(description='Command-line Alarm Clock that plays random YouTube videos')
    parser.add_argument('-t', '--time', help='Set alarm time in format HH:MM or HH:MM:SS')
    parser.add_argument('-f', '--file', help='Path to file containing YouTube links (one per line)')
    
    args = parser.parse_args()
    alarm = AlarmClock()
    youtube_links_file = args.file or create_sample_youtube_links_file()
    
    if not args.time:
        print("\n=== YouTube Alarm Clock ===\n")
        
        while True:
            if not args.file:
                print(f"Using sample file: {youtube_links_file}")
                if alarm.load_youtube_links(youtube_links_file):
                    break
            else:
                file_path = input(f"Enter path to YouTube links file [{args.file}]: ").strip() or args.file
                if alarm.load_youtube_links(file_path):
                    break
            
            if input("Do you want to try with a different file? (y/n): ").lower() != 'y':
                print("Exiting program.")
                sys.exit(0)
        
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if alarm.set_alarm(input(f"Enter alarm time (HH:MM or HH:MM:SS) [current: {current_time}]: ").strip()):
                break
    else:
        if not alarm.load_youtube_links(youtube_links_file) or not alarm.set_alarm(args.time):
            sys.exit(1)
    
    alarm.run_alarm()


if __name__ == "__main__":
    main()
