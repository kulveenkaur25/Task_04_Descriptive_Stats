
# Research Task 04: Descriptive Statistics on U.S. College Scorecard Data

## 📌 Objective
The goal of this task was to compute and compare descriptive statistics across various tools—**Pandas**, **Polars**, and **Pure Python**—on the 2021–22 U.S. College Scorecard dataset. The analysis focused on key metrics such as median earnings, student debt, and Pell Grant recipient percentages, grouped by U.S. states.

---

## 🧰 Tools Used
- **Pandas** (for comprehensive and quick analysis)
- **Polars** (for high-performance, memory-efficient processing)
- **Pure Python** (for manual, foundational understanding of operations)

---

## 📂 Project Structure
```
├── MERGED2021_22_PP.csv       # Raw data file
├── pandas_stats.py            # Analysis using pandas
├── polars_stats.py            # Analysis using polars
├── pure_python_stats.py       # Analysis using pure Python
├── performance.md             # Benchmark results
├── visuals/                   # Output plots grouped by state
└── README.md                  # This file
```

---

## 📈 Key Columns Analyzed
- `MD_EARN_WNE_P8`: Median earnings 8 years after entry
- `MN_EARN_WNE_P9`: Mean earnings 9 years after entry
- `PCTPELL_DCS`: Percent of students receiving Pell Grants
- `GRAD_DEBT_MDN_SUPP`: Median student loan debt at graduation
- `COUNT_WNE_P8`: Number of students working and not enrolled after 8 years
- `GT_25K_P8`: Fraction earning more than $25,000 after 8 years

---

## 📊 Output
- Descriptive statistics grouped by `STABBR` (state abbreviation)
- Mean, standard deviation, min, max, and mode for each column
- Visualizations saved to the `visuals/` folder
- Tool-wise performance benchmark (see `performance.md`)

---

## ✅ How to Run

```bash
# Pandas version
python pandas_stats.py --input MERGED2021_22_PP.csv --group_by STABBR --visuals visuals/

# Polars version
python polars_stats.py --input MERGED2021_22_PP.csv --group_by STABBR

# Pure Python version
python pure_python_stats.py --input MERGED2021_22_PP.csv --group_by STABBR
```

---

## 📌 Notes
- "PS" values in the dataset denote suppressed or privacy-protected fields.
- Visualizations are only generated in the `pandas_stats.py` script.

---

## 📬 Author
Kulveen Kaur  
MS in Applied Data Science  
Syracuse University
