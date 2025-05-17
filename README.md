# TrendAnalysis

This repository demonstrates how to apply the Mann–Kendall test and Sen's Slope estimator to time series data. The included notebook analyzes AP exam participation trends using a dataset named `tapar.csv` and produces summary files with trend statistics.

## Project Outputs

Running the notebook generates two files containing the calculated statistics:

- `tapar_analysis.csv`
- `tapar_analysis.xlsx`

## Installation

Install the required Python packages with:

```bash
pip install -r requirements.txt
```

## Obtaining `tapar.csv`

The notebook expects a file called `tapar.csv` in the repository root. This dataset is not distributed with the project. You can download a copy from the [APCSGender data repository](https://github.com/Dr-Kaya/APCSGender) or create your own CSV file with similar columns. Place the file next to the notebook so it can be loaded during execution.

## Running the Notebook

1. Ensure all dependencies are installed.
2. Start Jupyter:

   ```bash
   jupyter notebook "Clean_TA_PAR_AP_ALL_Gender_MKendall_and_Sen's_Slope.ipynb"
   ```
3. Execute the cells in order. When complete, the outputs listed above will appear in the same directory.

## License

This project is available under the terms of the MIT License. See [LICENSE](LICENSE).

## Citation

If you use this code or reproduce the analysis, please cite it following the information in [CITATION.cff](CITATION.cff).

