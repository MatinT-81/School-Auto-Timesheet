import random

def generate_random_times():
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    times = []
    total_minutes = 480  # 8 hours = 480 minutes
    start_hour = 8  # Start of working hours
    while total_minutes > 0:
        duration = random.choice([60, 90])  # Randomly choose between 60 or 90 minutes
        if total_minutes - duration < 0:
            duration = total_minutes  # Ensure the total time does not exceed 8 hours
        hour = random.randint(start_hour, 16)  # Random hour between 8 and 16
        minute = random.choice([0, 30])  # Random minute (00 or 30)
        end_hour = hour + (duration // 60)
        end_minute = minute + (duration % 60)
        if end_minute >= 60:
            end_hour += 1
            end_minute -= 60
        if end_hour > 17:  # Ensure the end time does not exceed 17:00
            break
        day = random.choice(days)  # Randomly choose a day
        times.append(f"{day} {hour:02}:{minute:02}-{end_hour:02}:{end_minute:02}")
        total_minutes -= duration
    return times

teachers = {
    "Mr. A": {
        "available_times": generate_random_times(),
        "subjects": ["Math", "Physics"]
    },
    "Ms. B": {
        "available_times": generate_random_times(),
        "subjects": ["Science", "Chemistry"]
    },
    "Mr. C": {
        "available_times": generate_random_times(),
        "subjects": ["Biology", "Math"]
    },
    "Ms. D": {
        "available_times": generate_random_times(),
        "subjects": ["English", "History"]
    },
    "Mr. E": {
        "available_times": generate_random_times(),
        "subjects": ["Physics", "Computer Science"]
    },
    "Ms. F": {
        "available_times": generate_random_times(),
        "subjects": ["Art", "Geography"]
    },
    "Mr. G": {
        "available_times": generate_random_times(),
        "subjects": ["Math", "English"]
    },
    "Ms. H": {
        "available_times": generate_random_times(),
        "subjects": ["History", "Physical Education"]
    },
    "Mr. I": {
        "available_times": generate_random_times(),
        "subjects": ["Economics", "Computer Science"]
    },
    "Ms. J": {
        "available_times": generate_random_times(),
        "subjects": ["Biology", "Chemistry"]
    },
    "Mr. K": {
        "available_times": generate_random_times(),
        "subjects": ["Physics", "Math"]
    },
    "Ms. L": {
        "available_times": generate_random_times(),
        "subjects": ["English", "Literature"]
    },
    "Mr. M": {
        "available_times": generate_random_times(),
        "subjects": ["Geography", "History"]
    },
    "Ms. N": {
        "available_times": generate_random_times(),
        "subjects": ["Art", "Physical Education"]
    },
}