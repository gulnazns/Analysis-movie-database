import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
# con = sqlite3.connect("C:/Users/gulnaz/Desktop/MathsHub courses/DS/SQL/Project/new_db_test", timeout=10)
# cur = con.cursor()

# Read the data from a CSV file
df = pd.read_csv('C:/Users/gulnaz/Desktop/MathsHub courses/DS/SQL/Project/IMDB-Movie-Data.csv', encoding='utf-8')
# df.to_sql(con=con, name='IMDB-Movie-Data.csv', index=False)

# Checked compliance with the project requirements, the minimum number of rows should be at least 500
rank_counts = df['Rank'].value_counts()
total_unique_ranks = len(rank_counts)
print(f"Total number of unique values in the 'Rank' column: {total_unique_ranks}")

# View the first few rows of the table
print(df.head())

# Change column names to lowercase
df.columns = df.columns.str.lower()

# Replace column names with lowercase
df.columns = df.columns.str.lower()

# Display the first 5 rows of the DataFrame with the new column names
print(df.head())

# Show the number of rows before removing duplicates
print(f"Number of rows before removing duplicates: {len(df)}")

# Remove duplicate rows
df = df.drop_duplicates()

# Find missing values
missing_values = df.isna().sum()
print(missing_values)

# Remove rows with missing values
df = df.dropna()

# Check all types
print(df.dtypes)

# rename columns
df.rename(columns={"runtime (minutes)": "runtime_min"}, inplace=True)
df.rename(columns={"revenue (millions)": "revenue_mln"}, inplace=True)
print(df.head())

# Replace the comma with an empty string and convert the 'year' column to a numeric format
df['year'] = df['year'].astype(str).str.replace(',', '').astype(int)
print(df['year'].head())


print(df['year'].dtypes)
# Connect to the SQLite database
#con = sqlite3.connect("C:/Users/gulnaz/Desktop/MathsHub courses/DS/SQL/Project/project_db", timeout=10)
#cur = con.cursor()
#df.to_sql(con=con, name='IMDB-Movie-Data.csv', index=False)


conn = sqlite3.connect("C:/Users/gulnaz/Desktop/MathsHub courses/DS/SQL/Project/project_db")
cursor = conn.cursor()
cursor.execute("SELECT title, rating FROM imdb ORDER BY rating DESC LIMIT 10")
data = cursor.fetchall()

titles = [row[0] for row in data]
ratings = [row[1] for row in data]

plt.figure(figsize=(10, 6))
plt.barh(titles, ratings, color='skyblue')
plt.xlabel('rating')
plt.ylabel('movies')
plt.title('Top 10 movies')
plt.gca().invert_yaxis()
plt.show()

# Top genre

# Splitting the results by genres and average ratings
genres, ratings = zip(*data)

# creating a vertical-axis column chart
plt.figure(figsize=(8, 6))
plt.bar(genres, ratings, color='skyblue')
plt.ylabel('average_rating')
plt.title('Top popular genres by rating')
plt.xticks(rotation=45)  # Rotating
plt.tight_layout()  # for labeling
plt.show()

# closing the database connection
conn.close()
