# Data Folder Overview

The `data` folder contains the following files, each serving a specific purpose in the **School Auto Timesheet** project:

## Files

### 1. `grades.py`
- **Purpose**: Defines the subjects and the number of hours required for each grade.
- **Structure**: A dictionary where each grade is a key, and its value is another dictionary mapping subjects to the required hours.

### 2. `teachers.py`
- **Purpose**: Specifies the teachers, their available times, and the subjects they can teach.
- **Key Functionality**:
  - **`generate_random_times`**:
    - **Description**: This function generates random time slots for teachers' availability.
    - **How It Works**:
      1. Randomly selects a day from the week (`Saturday` to `Wednesday`).
      2. Allocates random durations of 60 or 90 minutes, ensuring the total does not exceed 5 hours (300 minutes).
      3. Ensures the generated time slots do not exceed the working hours (8:00 to 17:00).
      4. Formats the time slots as strings in the format `Day HH:MM-HH:MM`.
    - **Output**: A list of formatted time slots for a teacher's availability.

### 3. `output.py`
- **Purpose**: Stores the generated schedule after running the scheduling algorithm in `main.py`.
- **Structure**: A dictionary where each day maps to time slots, and each time slot contains the grade, subject, and assigned teacher.
