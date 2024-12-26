
### Sample Python Scripts

#### data_cleaning.py

```python
import pandas as pd

def clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Handle missing values
    df.dropna(inplace=True)

    # Convert relevant columns to appropriate data types
    df['GPA'] = df['GPA'].astype(float)
    df['Attendance'] = df['Attendance'].astype(float)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df
