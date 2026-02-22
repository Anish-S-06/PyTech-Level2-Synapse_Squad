import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('attendance.csv', delimiter=',', dtype=None, encoding=None, names=True)
print(data.dtype)
print(data.shape)
names = data['student_name']
attendance = data['attendance_percentage']

mean_attendance = np.mean(attendance)
std_attendance = np.std(attendance)
print(f"Mean attendance: {mean_attendance:.2f}%")
print(f"Standard deviation: {std_attendance:.2f}%")

below_75_mask = attendance < 75
students_below_75 = names[below_75_mask]
print("Students below 75% attendance:")
for student in students_below_75:
    print(student)

sizes = [np.sum(attendance >= 75), np.sum(below_75_mask)]

plt.pie(sizes, labels=['>= 75%', '< 75%'], autopct='%1.1f%%')
plt.title("Attendance Distribution")
plt.show()