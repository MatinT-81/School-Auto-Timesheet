import random

def generate_random_times():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    times = []
    total_minutes = 300  # 5 ساعت = 300 دقیقه
    start_hour = 8  # شروع ساعت کاری
    while total_minutes > 0:
        duration = random.choice([60, 90])  # انتخاب تصادفی بین 60 یا 90 دقیقه
        if total_minutes - duration < 0:
            duration = total_minutes  # اطمینان از اینکه مجموع زمان‌ها از 5 ساعت تجاوز نکند
        hour = random.randint(start_hour, 16)  # ساعت تصادفی بین 8 تا 16
        minute = random.choice([0, 30])  # دقیقه تصادفی (00 یا 30)
        end_hour = hour + (duration // 60)
        end_minute = minute + (duration % 60)
        if end_minute >= 60:
            end_hour += 1
            end_minute -= 60
        if end_hour > 17:  # اطمینان از اینکه زمان پایان از ساعت 17 تجاوز نکند
            break
        day = random.choice(days)  # انتخاب تصادفی یک روز
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
}