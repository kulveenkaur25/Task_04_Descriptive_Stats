
---

### ✅ `performance_report.md.txt`

```markdown
# Performance Comparison: Pandas vs. Polars vs. Pure Python

## 🧪 Objective

To compute descriptive statistics (count, mean, min, max, std, etc.) on large CSV datasets grouped by a specified column, using:
1. Pure Python
2. Pandas
3. Polars

---

## ⚙️ Ease of Use

| Approach       | Ease of Setup | Code Complexity | Learning Curve |
|----------------|---------------|------------------|----------------|
| Pure Python    | ✅ High        | ❌ High          | 🔺 Steep        |
| Pandas         | ✅ High        | ✅ Moderate       | ✅ Easy         |
| Polars         | ✅ High        | ✅ Moderate       | 🔺 Moderate     |

- **Pandas** was the most intuitive due to widespread use and rich documentation.
- **Polars** was modern and efficient but required some learning to understand lazy vs. eager evaluation.
- **Pure Python** offered the deepest control but was verbose and more error-prone.

---

## ⏱️ Performance (Speed)

| Dataset                  | Pandas Time | Polars Time | Pure Python Time |
|--------------------------|-------------|-------------|------------------|
| MERGED2021_22_PP.csv     | ~2.4 sec    | **~0.6 sec**| ~5.3 sec         |

> ✅ **Polars** was the fastest due to its Rust backend and memory efficiency.
> ❌ **Pure Python** was the slowest, especially on large groupings.

---

## ✅ Accuracy of Results

- All three approaches produced **equivalent numerical results** for count, mean, min, max, and std.
- Pandas and Polars handled missing values more gracefully than pure Python.
- Categorical columns (`most_frequent`) were easier to compute in Pandas/Polars using `.value_counts()`.

---

## 📈 Insights from Visualizations

- States like **CA**, **TX**, and **NY** have the highest number of institutions and wide variance in median earnings.
- States like **PR** and **MS** showed consistently lower income outcomes but higher Pell Grant reliance.
- Some institutions report `PS` (privacy suppressed) for debt values — requiring handling in code.

---

## 💬 Recommendation to a Junior Analyst

If you're looking to get results fast and maintain readability, **use Pandas**.  
If you're working with very large datasets or want lightning-fast computation, **Polars** is worth learning.  
Avoid using **pure Python** unless for learning or environments where libraries are restricted.

---

## 🤖 Reflection on Using AI Tools

ChatGPT was useful in:
- Scaffolding boilerplate code
- Clarifying Polars syntax differences
- Speeding up data cleaning and debugging

It saved time, but manual validation was still essential to avoid logic bugs.

---

## 🔄 Challenges Faced

- Handling missing data (`PS`, `NULL`, or empty cells)
- Computing group-level `most_frequent` values in pure Python
- Avoiding memory overload with the large IPEDS dataset in Python

---

## ✅ Final Verdict

| Category       | Winner     |
|----------------|------------|
| Speed          | **Polars** |
| Simplicity     | **Pandas** |
| Transparency   | Pure Python|
