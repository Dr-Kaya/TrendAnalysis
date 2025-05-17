# TrendAnalysis
Mann Kendall and Sen's Slope - Non-parametric Trend Analysis

## Running the notebook

The Jupyter notebook `Clean_TA_PAR_AP_ALL_Gender_MKendall_and_Sen's_Slope.ipynb` contains the exploratory analysis used to generate the trend statistics. Open the notebook in Jupyter and run the cells sequentially.

## Running the command line script

Key analysis steps have been exported to `analyze_trends.py`. The script expects a path to `tapar.csv` and prints the trend statistics for each exam column.

```bash
python analyze_trends.py path/to/tapar.csv
```

The CSV file should be the same one used in the notebook. The script performs the same data preparation and Mann–Kendall tests as in the notebook and outputs the slope, p-value and other metrics for each exam.
