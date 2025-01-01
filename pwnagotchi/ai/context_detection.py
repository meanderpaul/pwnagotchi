def get_network_activity_level():
    # Placeholder function to determine network activity level
    # Replace with actual logic to measure network activity
    return "high"

def get_battery_level():
    # Placeholder function to get the device's battery level
    # Replace with actual logic to measure battery level
    return 50  # Example value

def get_current_time_of_day():
    # Placeholder function to get the current time of day
    # Replace with actual logic to get the current time
    import datetime
    return datetime.datetime.now().hour

def detect_context():
    network_activity = get_network_activity_level()
    battery_level = get_battery_level()
    current_time = get_current_time_of_day()
    
    if network_activity == "high":
        return "high_activity"
    elif battery_level < 20:
        return "low_battery"
    elif current_time >= 22 or current_time < 6:
        return "night_time"
    else:
        return "normal"
