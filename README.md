# Student Performance Analysis

A Python data analysis project exploring student exam performance, attendance, study hours, and department-level summaries.

## Project status

The Python analysis script is included. The original dataset was not available to be bundled with this archive, so add your `student_performance.csv` file to the `data/` folder before running the script.

The dataset should contain these columns:

- `student_id`
- `department`
- `exam_score`
- `attendance_pct`
- `study_hours_per_day`

These are the column names referenced by the analysis script. Confirm that your CSV uses these exact names.

## Project structure

```text
student-performance-analysis/
├── data/
│   └── student_performance.csv   # Add your dataset here
├── outputs/
│   ├── department_scores.png     # Generated when script runs
│   └── student_dashboard_data.csv
├── powerbi/
│   └── README.md                # Notes for the future Power BI report
├── analyze_students.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Tools and libraries

- Python
- Pandas
- Matplotlib

## Analysis performed

1. Loads student records from a CSV file.
2. Categorizes exam scores into performance bands.
3. Calculates the number of students and average exam score.
4. Calculates average attendance.
5. Summarizes average score, average attendance, and student count by department.
6. Calculates descriptive correlations among attendance, exam score, and study hours.
7. Exports processed data to `outputs/student_dashboard_data.csv`.
8. Creates a department-wise average exam score chart.

## Setup and run

Use Python 3.9 or later.

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place `student_performance.csv` in the `data/` folder, then run:

```bash
python analyze_students.py
```

Generated files will be saved in `outputs/`.

## Important interpretation note

Correlation is descriptive and does not prove that attendance or study hours cause higher exam scores. Any findings should be interpreted in the context of the dataset and its limitations.

## Dataset and limitations

The dataset is intended for practice/portfolio analysis. If it is synthetic or fictional, state that clearly in your final portfolio and do not present the results as evidence about real students.

## Future extensions

- Add data-quality checks and additional exploratory visualizations.
- Build SQL queries for department and performance analysis.
- Create an interactive Power BI dashboard and place the `.pbix` file in `powerbi/`.
- Add screenshots and verified findings after completing those extensions.
