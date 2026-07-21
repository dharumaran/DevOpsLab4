attendance = {}

def mark_attendance(roll_no, status):
    attendance[roll_no] = status

def display_attendance():
    print("\nAttendance")
    for roll, status in attendance.items():
        print(f"Roll No: {roll} -> {status}")

if __name__ == "__main__":
    mark_attendance(101, "Present")
    mark_attendance(102, "Absent")
    display_attendance()
    