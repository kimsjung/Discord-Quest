import os
import json
from setFile import run as step2
# Paths
users_path = 'C:\\Users'
settings_path = 'settings.json'

# Folders to ignore
excluded_names = ['Default', 'Default User', 'Public', 'All Users']

def run():
    # Get valid user folders
    user_folders = [
    f for f in os.listdir(users_path)
        if os.path.isdir(os.path.join(users_path, f)) and f not in excluded_names
    ]

    # Load existing settings
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                settings = {}
    else:
        settings = {}

    # Get current username in settings (if any)
    current_username = settings.get("username")
    logic_type = settings.get("type")

    # Logic to check and update only if needed
    if logic_type.lower() == "default":
        if len(user_folders) == 1:
            detected_username = user_folders[0]
            if current_username == detected_username:
                print(f"Username '{current_username}' already set. No update needed.")
            else:
                settings["username"] = detected_username
                settings["defaultPath"] = f"C:\\Users\\{detected_username}\\AppData\\Roaming\\discord"
                with open(settings_path, 'w') as f:
                    json.dump(settings, f, indent=4)
                print(f"Updated username to '{detected_username}' in settings.json.")
                step2()
        else:
            if current_username != "not set":
                settings["username"] = "not set"
                with open(settings_path, 'w') as f:
                    json.dump(settings, f, indent=4)
                print("Multiple or no user folders found. Updated username to 'not set'.")
            else:
                print("Username already 'not set'. No update needed.")
    else:
        step2()