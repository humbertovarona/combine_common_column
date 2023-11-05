# combine_common_column

Simple function to combine two csv files with a common column

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-Nov%2C%205%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```bash
pip install pandas
```

```python
import pandas as pd
```

## How to run

```python
base_filename = "data.csv"
reference_filename = "station_coordinates.csv"
common_column_name = "STATION_ID"
output_filename = "finaldata.csv"

combine_csv_files(base_filename, reference_filename, common_column_name, output_filename)
```
