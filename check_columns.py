import pandas as pd

# Load dataset
df = pd.read_csv("emails.csv")  # Ensure correct filename

# Print the column names
print("Columns in dataset:", df.columns)
