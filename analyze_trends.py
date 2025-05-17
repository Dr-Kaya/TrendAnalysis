import argparse
import pandas as pd
import numpy as np
import pymannkendall as mk


def load_and_prepare(csv_path: str) -> pd.DataFrame:
    """Load tapar.csv and prepare the dataframe for analysis."""
    df = pd.read_csv(csv_path)
    df2 = df.T
    header = df2.iloc[0]
    df2 = df2[1:]
    df2.columns = header
    df2.reset_index(inplace=True)
    df2.rename(columns={'index': 'Year'}, inplace=True)
    df3 = df2.apply(pd.to_numeric)
    return df3


def analyze_exam(series: pd.Series, years: pd.Series) -> dict:
    """Run Mann-Kendall test on a series and compute Sen's slope."""
    result = mk.original_test(series)
    intercept_final = series.iloc[-1] - result.slope * years.iloc[-1]
    return {
        'trend': result.trend,
        'p': result.p,
        'slope': result.slope,
        'z': result.z,
        'Tau': result.Tau,
        's': result.s,
        'var_s': result.var_s,
        'intercept': intercept_final,
    }


def main():
    parser = argparse.ArgumentParser(description='Run trend analysis on AP exam data.')
    parser.add_argument('csv_path', help='Path to tapar.csv')
    args = parser.parse_args()

    df = load_and_prepare(args.csv_path)
    years = df['Year']

    for col in df.columns[1:46]:
        print(f'Exam Name: {col}')
        stats = analyze_exam(df[col], years)
        for key, value in stats.items():
            print(f'{key}: {value}')
        print('-' * 29)
        print()


if __name__ == '__main__':
    main()
