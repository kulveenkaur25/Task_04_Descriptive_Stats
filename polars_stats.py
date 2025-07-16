import polars as pl
import argparse
import os

def compute_group_stats(df, group_by, output_dir):
    grouped = df.groupby(group_by)
    summary = grouped.agg([
        pl.col(pl.Utf8).n_unique().alias("unique"),
        pl.col(pl.Utf8).mode().alias("most_frequent"),
        pl.col(pl.Float64).count().alias("count"),
        pl.col(pl.Float64).mean().alias("mean"),
        pl.col(pl.Float64).min().alias("min"),
        pl.col(pl.Float64).max().alias("max"),
        pl.col(pl.Float64).std().alias("std")
    ])

    print(summary)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"groupby_{'_'.join(group_by)}.csv")
        summary.write_csv(output_file)
        print(f"\n✅ Summary saved to {output_file}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='CSV file path')
    parser.add_argument('--group_by', nargs='+', help='Group by column(s)')
    parser.add_argument('--visuals', help='Optional output directory for saving results')
    args = parser.parse_args()

    df = pl.read_csv(args.input, infer_schema_length=10000)

    # Convert non-numeric fields to string
    df = df.with_columns([
        pl.when(pl.col(col).is_numeric())
        .then(pl.col(col).cast(pl.Float64))
        .otherwise(pl.col(col).cast(pl.Utf8))
        .alias(col) for col in df.columns
    ])

    compute_group_stats(df, args.group_by, args.visuals)

if __name__ == '__main__':
    main()
