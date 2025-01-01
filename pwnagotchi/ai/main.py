import time
from ai.context_detection import detect_context
from ai.behavior_adjustment import adjust_behavior

while True:
    current_context = detect_context()
    adjust_behavior(current_context)
    time.sleep(60)  # Check context every 60 seconds
