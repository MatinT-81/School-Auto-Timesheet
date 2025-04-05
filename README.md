# School Auto Timesheet

The **School Auto Timesheet** project is a Python-based application designed to automate the scheduling of classes for a school. It allocates teachers, subjects, and grades to specific time slots based on availability and requirements.

## Features

- **Dynamic Scheduling**: Automatically assigns teachers to classes based on their availability and expertise.
- **Grade-Specific Allocation**: Ensures that each grade's required subjects are scheduled with the appropriate teachers.
- **Conflict-Free Scheduling**: Prevents overlapping time slots for teachers and ensures no double-booking.
- **Customizable Inputs**: Easily modify teacher availability, grade requirements, and subject preferences.

## Project Structure

## How It Works

1. **Input Data**:
   - `data/grades.py`: Defines the subjects and hours required for each grade.
   - `data/teachers.py`: Specifies teacher availability and the subjects they can teach.

2. **Scheduling Algorithm**:
   - The algorithm in `main.py` iterates through grades, subjects, and teacher availability to allocate time slots.
   - Ensures no conflicts in teacher schedules or overlapping time slots.

3. **Output**:
   - The generated schedule is saved in `data/output.py` in a structured format.

## Example Schedule Output

An example of the generated schedule is as follows:

```python
schedule = {
    "Sunday": {
        "13:30-14:30": {
            "grade": "8",
            "subject": "Math",
            "teacher": "Mr. A"
        },
        ...
    },
    ...
}