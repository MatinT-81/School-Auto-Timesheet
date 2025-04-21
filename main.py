import json
from collections import defaultdict
from data.grades import grades
from data.teachers import teachers


# ? [{
# ?     teacher : {}
# ?     availability : {
# ?         'saturday':{
# ?             start: 8
# ?             end: 10
# ?             total_min: 100
# ?         }
# ? 7-9 11-15 
# ?     }
# ?     {title , sub , grade 8, major }
# ? }]


# Final schedule
schedule = defaultdict(lambda: defaultdict(dict))

# Reserved times for teachers
reserved_times = {teacher: set() for teacher in teachers}

def is_valid_assignment(day, time_slot, teacher, subject, grade):
    """
    Check if the current assignment is valid.
    """
    # Check if the teacher is already reserved at this time
    if time_slot in reserved_times[teacher]:
        return False

    # Check if the time slot is already occupied in the schedule
    if time_slot in schedule[day][grade]:
        return False

    return True

def backtrack(grade_list, grade_index=0):
    """
    Backtracking function to allocate subjects to teachers.
    """
    # Base case: All grades are processed
    if grade_index == len(grade_list):
        return True

    grade = grade_list[grade_index]
    subjects = grades[grade]

    for subject, hours_needed in subjects.items():
        assigned_hours = 0

        for teacher, data in teachers.items():
            if subject in data["subjects"]:
                for time_slot in data["available_times"]:
                    day, time_range = time_slot.split()

                    if is_valid_assignment(day, time_slot, teacher, subject, grade):
                        # Ensure 'lessons' key exists
                        if "lessons" not in schedule[day][grade]:
                            schedule[day][grade]["lessons"] = {}

                        # Assign the time slot
                        schedule[day][grade]["lessons"][subject] = {
                            "time": time_range,
                            "teacher": teacher,
                        }
                        reserved_times[teacher].add(time_slot)
                        assigned_hours += 1

                        # If all hours are assigned, move to the next subject
                        if assigned_hours >= hours_needed:
                            break

                # If the subject is fully assigned, move to the next subject
                if assigned_hours >= hours_needed:
                    break
        
    # Move to the next grade
    return backtrack(grade_list, grade_index + 1)

# Start the backtracking process
grade_list = list(grades.keys())
if backtrack(grade_list):
    print("Schedule successfully generated!")
else:
    print("Failed to generate a valid schedule.")

# Save the schedule to the output file
with open("data/output.py", "w", encoding="utf-8") as f:
    f.write("schedule = ")
    json.dump(dict(schedule), f, ensure_ascii=False, indent=4)