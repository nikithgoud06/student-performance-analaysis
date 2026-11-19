from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project root: the folder containing this Python file
ROOT = Path(__file__).resolve().parent

# Load the dataset from the data folder
DATA_FILE = ROOT / "data" / "student_performance.csv"
df = pd.read_csv(DATA_FILE)

# Create output folder if it does not exist
out = ROOT / "outputs"
out.mkdir(exist_ok=True)

# Categorize exam scores
df["performance_band"] = pd.cut(
    df["exam_score"],
    bins=[0, 59, 74, 89, 100],
    labels=["Needs Support", "Developing", "Good", "Excellent"],
    include_lowest=True
)

# Overall summary
print("Students:", len(df))
print("Average exam score:", round(df["exam_score"].mean(), 1))
print("Average attendance:", round(df["attendance_pct"].mean(), 1), "%")

# Department summary
department_summary = (
    df.groupby("department")
      .agg(
          avg_score=("exam_score", "mean"),
          avg_attendance=("attendance_pct", "mean"),
          students=("student_id", "count")
      )
      .round(2)
)
print("\nDepartment summary:\n", department_summary)

# Descriptive correlations (correlation does not establish causation)
print(
    "\nCorrelation (descriptive only):\n",
    df[["attendance_pct", "exam_score", "study_hours_per_day"]]
      .corr()
      .round(2)
)

# Export processed data
df.to_csv(out / "student_dashboard_data.csv", index=False)

# Department average exam score chart
(
    df.groupby("department")["exam_score"]
      .mean()
      .plot(
          kind="bar",
          title="Average Exam Score by Department",
          ylabel="Average score"
      )
)
plt.tight_layout()
plt.savefig(out / "department_scores.png", dpi=150)
plt.show()
