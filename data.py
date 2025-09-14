# ===============================
# Assignment: Data Analysis with Pandas and Matplotlib
# Objective: Load, analyze, and visualize a dataset
# ===============================

# Task 0: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Set Seaborn style for nicer visuals
sns.set(style="whitegrid")

# ===============================
# Task 1: Load and Explore the Dataset
# ===============================

try:
    # Example dataset: Iris (from seaborn)
    df = sns.load_dataset("iris")

    print(" Dataset loaded successfully!\n")

    # Display the first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Check structure
    print("Dataset Info:")
    print(df.info(), "\n")

    # Check missing values
    print("Missing Values per Column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (if needed) – here we just drop missing values
    df = df.dropna()

    # ===============================
    # Task 2: Basic Data Analysis
    # ===============================

    # Summary statistics
    print("Statistical Summary:")
    print(df.describe(), "\n")

    # Grouping example: Average petal length per species
    grouped = df.groupby("species")["petal_length"].mean()
    print("Average Petal Length per Species:")
    print(grouped, "\n")

    # ===============================
    # Task 3: Data Visualization
    # ===============================

    # Line Chart (not always suitable for Iris, but using index for example)
    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df["sepal_length"], label="Sepal Length")
    plt.title("Sepal Length Trend Over Index")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length")
    plt.legend()
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x="species", y="petal_length", data=df, estimator="mean")
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Avg Petal Length")
    plt.show()

    # Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["sepal_width"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    plt.legend(title="Species")
    plt.show()

    # ===============================
    # Task 4: Findings & Observations
    # ===============================

    print("\n📊 Findings:")
    print("- The dataset has 3 species: setosa, versicolor, and virginica.")
    print("- Setosa generally has smaller petal lengths compared to the others.")
    print("- Sepal length and petal length are positively correlated.")
    print("- Data is clean with no missing values in this dataset.")

except FileNotFoundError:
    print(" File not found. Please check the file path.")
except Exception as e:
    print(f" An error occurred: {e}")