# PyTech Arena 2026 – Level 2  
## Problem 4: Attendance Statistics (NumPy + Matplotlib)

---

## Problem Chosen

**Problem 4: Attendance Statistics**

- Load `attendance.csv`
- Calculate mean and standard deviation
- Identify students below 75%
- Generate pie chart

---

## Dataset Source

- File Used: `attendance.csv`
- Dataset Type: Student attendance dataset
- Source: Open dataset (as permitted in competition guidelines)

---

## Project Description

This project performs statistical analysis on student attendance data using **NumPy** and visualizes the results using **Matplotlib**.

### Steps Performed:

1. Loaded the dataset using `numpy.genfromtxt()`.
2. Verified dataset structure (data types and shape).
3. Extracted student names and attendance percentages.
4. Calculated:
   - Mean attendance
   - Standard deviation
5. Identified students with attendance below 75%.
6. Generated a pie chart showing the distribution of:
   - Students with attendance ≥ 75%
   - Students with attendance < 75%

---

## Output

The program displays:

- Mean attendance percentage
- Standard deviation
- List of students below 75%
- Pie chart visualization of attendance distribution

---

## How to Run the Project

### Install Required Libraries

```bash
pip install numpy matplotlib
