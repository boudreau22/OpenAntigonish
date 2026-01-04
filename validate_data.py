import json
import sys
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y/%m/%d')
        return True
    except ValueError:
        return False

def validate_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {filepath}: {e}")
        return False
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return False

    required_sections = ['pfizerFacts', 'pfizerTimeline', 'otherVaccines']
    success = True

    for section in required_sections:
        if section not in data:
            print(f"Error: Missing section '{section}'")
            success = False
            continue

        items = data[section]
        if not isinstance(items, list):
             print(f"Error: Section '{section}' should be a list")
             success = False
             continue

        for i, item in enumerate(items):
            if 'title' not in item or 'description' not in item:
                print(f"Error: Item {i} in '{section}' missing title or description")
                success = False

            # Check dates
            if section == 'pfizerTimeline':
                if 'start' not in item or 'end' not in item:
                    print(f"Error: Item {i} in '{section}' missing start or end date")
                    success = False
                else:
                    if not validate_date(item['start']) or not validate_date(item['end']):
                        print(f"Error: Invalid date format in item {i} of '{section}' (expected YYYY/MM/DD)")
                        success = False
            else:
                if 'date' not in item:
                    print(f"Error: Item {i} in '{section}' missing date")
                    success = False
                else:
                    if not validate_date(item['date']):
                        print(f"Error: Invalid date format in item {i} of '{section}' (expected YYYY/MM/DD)")
                        success = False

    return success

if __name__ == "__main__":
    if validate_data('vaccine_timeline.json'):
        print("Data validation passed.")
        sys.exit(0)
    else:
        print("Data validation failed.")
        sys.exit(1)
