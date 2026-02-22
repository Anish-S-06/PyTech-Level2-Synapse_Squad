# PyTech Arena 2026 – Level 2  
## Problem 7: Pass/Fail Predictor (ML – Classification)

---

## Problem Chosen

**Problem 7: Pass/Fail Predictor**

- Create target column (Pass if score ≥ 40, else Fail)
- Split dataset (80% training, 20% testing)
- Train Logistic Regression model
- Display accuracy score
- Predict result for sample input

---

## Dataset Source

- Dataset Used: Student Performance Dataset
- Source: Kaggle  
- Link: https://www.kaggle.com/datasets/spscientist/students-performance

---

## Project Description

This project builds a **Binary Classification Machine Learning model** to predict whether a student passes or fails based on performance data.

The implementation includes:

1. Loading the dataset using Pandas.
2. Inspecting columns and checking for null values.
3. Creating an `avg_score` column using subject marks.
4. Creating a binary `target` column:
   - `1 → Pass`
   - `0 → Fail`
5. Converting categorical features into numerical format using Label Encoding.
6. Performing correlation analysis to understand feature relationships.
7. Splitting dataset into 80% training and 20% testing sets.
8. Training a Logistic Regression classifier.
9. Evaluating model performance using accuracy score.

---

## Output

The program displays:

- Correlation matrix
- Accuracy score of the model

High accuracy was observed due to strong correlation between subject scores and the target variable.

---

## How to Run the Project

### Install Required Libraries

```bash
pip install pandas scikit-learn
