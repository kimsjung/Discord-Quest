import os
import json

settings_path = 'settings.json'
discord_filename = 'settings.json'

def run():
    # Load existing settings
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                settings = {}
    else:
        settings = {}

    logic_type = settings.get("type")
    if logic_type.lower() == "default":
        discord_settings_path = settings.get("defaultPath") + f"\\{discord_filename}"
    else:
        discord_settings_path = settings.get("customPath") + f"\\{discord_filename}"

    # Load existing settings
    if os.path.exists(discord_settings_path):
        with open(discord_settings_path, 'r') as f:
            try:
                discord_settings_file = json.load(f)
            except json.JSONDecodeError:
                discord_settings_file = {}
    else:
        discord_settings_file = {}

    if discord_settings_file.get("DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING") and discord_settings_file.get("DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING") == True:
        print("you're discord already enable IQ")
    else:
        discord_settings_file['DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING'] =  True
        with open(discord_settings_path, 'w') as f:
            json.dump(discord_settings_file, f, indent=4)
        print(f"Updated data in settings.json.")