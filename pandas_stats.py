import pandas as pd
import argparse
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Manually selected useful columns based on College Scorecard data
selected_cols = [
    "CONTROL",               # Public/Private
    "STABBR",                # State
    "MD_EARN_WNE_P8",        # Median earnings after 8 years
    "MN_EARN_WNE_P9",        # Mean earnings after 9 years
    "PCTPELL_DCS",           # % Pell Grant recipients
    "GRAD_DEBT_MDN_SUPP",    # Median grad debt (suppressed/estimated)
    "COUNT_WNE_P8",          # Number of students with earnings data
    "GT_25K_P8"              # Proportion earning > $25K after 8 years
]

def is_useless(col):
    return col.nunique() <= 1 or col.astype(str).str.fullmatch(r"(NA|NULL|PrivacySuppressed|PS)").all()

def summarize_column(col):
    summary = {"count": col.count()}

    if pd.api.types.is_numeric_dtype(col):
        summary.update({
            "mean": col.mean(),
            "min": col.min(),
            "max": col.max(),
            "std": col.std()
        })
    else:
        counts = col.value_counts()
        if not counts.empty:
            summary.update({
                "unique": col.nunique(),
                "most_frequent": counts.idxmax()
            })
        else:
            summary.update({
                "unique": 0,
                "most_frequent": None
            })
    return summary

def analyze(df, group_cols=None):
    filtered_cols = [col for col in selected_cols if col in df.columns and not is_useless(df[col])]

    if group_cols:
        grouped = df.groupby(group_cols)
        for name, group in grouped:
            print(f"\n--- Group: {name} ---")
            for col in filtered_cols:
                print(f"\nColumn: {col}")
                print(summarize_column(group[col]))
    else:
        for col in filtered_cols:
            print(f"\nColumn: {col}")
            print(summarize_column(df[col]))

def generate_visuals(df, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    numeric_cols = df[ [col for col in selected_cols if col in df.columns] ].select_dtypes(include='number').columns

    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, f"{col}_hist.png"))
        plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to input CSV file')
    parser.add_argument('--group_by', help='Comma-separated column names to group by')
    parser.add_argument('--visuals', default='visuals/', help='Output folder for plots')
    args = parser.parse_args()

    df = pd.read_csv(args.input, low_memory=False)

    # Grouping logic
    group_by_cols = args.group_by.split(',') if args.group_by else None
    analyze(df, group_by_cols)

    # Visualizations
    generate_visuals(df, args.visuals)
    print(f"\n✅ Visualizations saved in '{args.visuals}'")

if __name__ == "__main__":
    main()
