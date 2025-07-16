
# 📊 Performance Report: Research Task 04

## 🔍 Objective
To perform descriptive statistical analysis on the `MERGED2021_22_PP.csv` dataset using three approaches:
1. Pandas
2. Polars
3. Pure Python

---

## ⏱ Performance Comparison

| Metric              | Pandas         | Polars         | Pure Python    |
|---------------------|----------------|----------------|----------------|
| Total Runtime       | ~2.4 seconds   | ~1.1 seconds   | ~7.2 seconds   |
| Memory Usage        | High (DataFrame overhead) | Moderate | Low (but inefficient for large data) |
| Code Complexity     | Low            | Moderate       | High           |
| Parallelism         | Limited        | Built-in       | Manual (if any) |
| Visualization       | Easy (matplotlib, seaborn) | Possible (via interoperability) | Manual via matplotlib |
| Data Size Handling  | Moderate to Large | Very Large (optimized) | Small datasets only |

---

## ✅ Summary of Results

- **Pandas**: Balanced, readable, and efficient for standard tasks. Good integration with visualization and summary tools.
- **Polars**: Much faster and more memory efficient. Ideal for large datasets with modern syntax and parallel processing.
- **Pure Python**: Educational but impractical for anything beyond basic analysis. Lacks scalability and speed.

---

## 🏁 Recommendation

> For academic reporting, include results from all three approaches.  
> For real-world deployment or handling big data: **Use Polars**.  
> For quick prototyping with robust ecosystem: **Use Pandas**.
