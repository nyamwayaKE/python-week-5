import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile

# Task 1: Load and Explore the Dataset
try:
    # Open the ZIP file
    with zipfile.ZipFile('wine.zip') as z: 
        # List all files in the ZIP
        print("Files in ZIP:", z.namelist())

        # Specify the target file to load
        target_file = 'wine.data'  # Replace with the desired file name in the ZIP
        with z.open(target_file) as file:
            # Load the dataset
            column_names = [
                "Class", "Alcohol", "Malic_Acid", "Ash", "Alcalinity_of_Ash",
                "Magnesium", "Total_Phenols", "Flavanoids", "Nonflavanoid_Phenols",
                "Proanthocyanins", "Color_Intensity", "Hue", "OD280/OD315_of_Diluted_Wines", "Proline"
            ]
            df = pd.read_csv(file, header=None, names=column_names)

    # Display dataset information
    print(df.head())
    print(df.info())

    # Check for missing values
    print("Missing values:\n", df.isnull().sum())

    # Clean the data by filling missing values (if any)
    df.fillna(method='ffill', inplace=True)

except zipfile.BadZipFile:
    print("The file is not a valid ZIP file.")
    exit()
except FileNotFoundError:
    print("The ZIP file was not found. Please ensure the file is in the correct directory.")
    exit()
except KeyError:
    print(f"The file '{target_file}' was not found in the ZIP archive.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Task 2: Basic Data Analysis
try:
    # Summary statistics
    print(df.describe())

    # Group by the class and compute mean values for each group
    grouped = df.groupby('Class').mean()
    print("Mean values by class:\n", grouped)
except KeyError as e:
    print(f"Column not found: {e}")
except Exception as e:
    print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization
try:
    # Line Chart
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df.index, y='Alcohol', data=df)
    plt.title("Line Chart: Alcohol Content by Index")
    plt.xlabel("Index")
    plt.ylabel("Alcohol")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Class', y='Alcohol', data=df)
    plt.title("Bar Chart: Average Alcohol Content by Class")
    plt.xlabel("Class")
    plt.ylabel("Alcohol")
    plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Alcohol'], kde=True, bins=30)
    plt.title("Histogram: Distribution of Alcohol Content")
    plt.xlabel("Alcohol")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Alcohol', y='Color_Intensity', data=df)
    plt.title("Scatter Plot: Alcohol vs Color Intensity")
    plt.xlabel("Alcohol")
    plt.ylabel("Color Intensity")
    plt.show()
except KeyError as e:
    print(f"Column not found: {e}")
except Exception as e:
    print(f"An error occurred during visualization: {e}")
