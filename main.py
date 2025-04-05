import json
from collections import defaultdict

from data.grades import grades
from data.teachers import teachers

# Final schedule
schedule = defaultdict(dict)

# Reserved times for teachers
reserved_times = {teacher: set() for teacher in teachers}

# Allocation algorithm
for grade, subjects in grades.items():
    for subject, hours_needed in subjects.items():
        assigned_hours = 0
        for teacher, data in teachers.items():
            if subject in data["subjects"]:
                for time_slot in data["available_times"]:
                    # Check if this time slot is not already reserved
                    if time_slot not in reserved_times[teacher]:
                        # Extract day and hour
                        day = "Monday"  # یا هر روز پیش‌فرض یا داده‌ای که باید اضافه شود
                        hour = time_slot  # فرض می‌کنیم time_slot فقط شامل بازه زمانی است
                        # Check if that hour for that day is not already occupied
                        if hour not in schedule[day]:
                            schedule[day][hour] = {
                                "grade": grade,
                                "subject": subject,
                                "teacher": teacher
                            }
                            reserved_times[teacher].add(time_slot)
                            assigned_hours += 1
                            break  # Move to the next time slot for this subject
                if assigned_hours >= hours_needed:
                    break  # The subject has been allocated the required hours

with open("data/output.py", "w", encoding="utf-8") as f:
    f.write("schedule = ")
    json.dump(dict(schedule), f, ensure_ascii=False, indent=4)