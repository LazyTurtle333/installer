import os
import shutil
import sys
import time
import threading

# Installer settings
app_name = "example-app"  # Replace with your application name
default_path = "path/to/source/directory"  # Change this to your source directory
default_target_path = "path/to/target/directory"  # Change this to your target directory

# Function to create a rotating progress indicator
def spinner(text):
    while not stop_spinner_event.is_set():
        for cursor in '|/-\\':
            sys.stdout.write(f'\r{text} {cursor}')
            sys.stdout.flush()
            time.sleep(0.1)

# Function to create directories and copy files
def create_installer(source, target):
    # Start the spinner for creating directories
    stop_spinner_event.clear()
    spinner_thread = threading.Thread(target=spinner, args=(f"Creating directories...",))
    spinner_thread.start()

    # Create the target directory if it doesn't exist
    if not os.path.exists(target):
        os.makedirs(target)

    stop_spinner_event.set()
    spinner_thread.join()
    print("\rCreating directories... done.")

    # Start the spinner for copying files
    stop_spinner_event.clear()
    spinner_thread = threading.Thread(target=spinner, args=(f"Copying files...",))
    spinner_thread.start()

    # Copy files from source to target
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        target_item = os.path.join(target, item)

        if os.path.isdir(source_item):
            shutil.copytree(source_item, target_item)
        else:
            shutil.copy2(source_item, target_item)

    stop_spinner_event.set()
    spinner_thread.join()
    print("\rCopying files... done.")

def main():
    global stop_spinner_event
    stop_spinner_event = threading.Event()

    print(f"\nWelcome to {app_name} installer.")

    if os.path.exists(default_path):
        create_installer(default_path, default_target_path)
        print(f"\nFinished installing {app_name}.")
    else:
        print(f"Error: Source path '{default_path}' does not exist.")
    print("© Copyright 2024 LazyTurtle333 on GitHub.")
    input("Press enter to close.")

if __name__ == "__main__":
    main()