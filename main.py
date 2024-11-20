# Step 1: Install and Import pandas
import pandas as pd

# Step 2: Import pandas and Load the Spreadsheet
df = pd.read_csv("bestsellers.csv")

# Step 3: Explore the Data
# Get the first 5 rows of the spreadsheet
print(df.head())
# Get the shape of the spreadsheet
print(df.shape)
# Get the colum names of the spreadsheet
print(df.columns)
# Get the summary for each column
print(df.describe())

# Step 4: Clean the Data

# Drop duplicates
df.drop_duplicates(inplace=True)
# inplace is used to make changes which are made directly to the original DataFrame.

# check the datatypes of the columns
df.info() # All columns datatypes is described

# Renaming Columns - For easy access and determination
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

## Converting Data Types
df['Price'] = df['Price'].astype(float)
# astype - This code converts the "Price" column to a float data type. Note that we select the "Price" column of the DataFrame
# using the square bracket notation, and then apply the astype() function to it. The resulting values are 
# then stored back in the "Price" column of the DataFrame.

# Step 5: Run an Analysis
  # 1. Analyzing Author Popularity
aurthor_counts = df['Author'].value_counts()
print(aurthor_counts)


  # 2. Average Rating by Genre
avg= df.groupby('Genre')['Rating'].mean()
print(avg)

#Step 6: Export the Results
# Export top selling authors to a CSV file
aurthor_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg.to_csv("avg.csv")


 # Utilise Mathplot libraries to plot these graphs as well. 
 # In case if this not running in local system, try to Use Google Collab notebook or Kaggle notebooks.