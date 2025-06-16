import json
import os

def save_json(data, filepath):
    try:
        # Create directory if it doesn't exist
        dir_path = os.path.dirname(filepath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"📁 Created directory: {dir_path}")

        # Save JSON data to file
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Saved JSON to {filepath}")
    except Exception as e:
        print(f"❌ Error saving JSON to {filepath}: {e}")

def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        print(f"✅ Loaded JSON from {filepath}")
        return data
    except FileNotFoundError:
        print(f"⚠️ File not found: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"⚠️ Error decoding JSON from file: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Error loading JSON from {filepath}: {e}")
        return None
