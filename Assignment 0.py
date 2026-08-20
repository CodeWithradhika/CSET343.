
#--File Hndling--
print("=" * 60)
print("1. FILE HANDLING")
print("=" * 60)

# --- Writing to a file ---
data_to_write = """Name,Age,Marks
Radhika,21,89
Aman,22,76
Priya,21,92
Kabir,23,65
"""

with open("students.csv", "w") as f:
    f.write(data_to_write)
print("students.csv likh diya (write mode).")

# --- Reading a file line by line ---
with open("students.csv", "r") as f:
    lines = f.readlines()

print("\nFile contents:")
for line in lines:
    print(line.strip())

# --- Appending to a file ---
with open("students.csv", "a") as f:
    f.write("Sana,22,81\n")
print("\nEk aur row append kar di.")

# --- Reading with context manager + splitting into a list of dicts ---
with open("students.csv", "r") as f:
    header = f.readline().strip().split(",")
    records = []
    for line in f:
        values = line.strip().split(",")
        records.append(dict(zip(header, values)))

print("\nParsed records (list of dicts):")
for r in records:
    print(r)



# 2. NUMPY - NUMERICAL OPERATIONS
import numpy as np

print("\n" + "=" * 60)
print("2. NUMPY")
print("=" * 60)

# --- Creating arrays ---
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(1, 11)          # 1 to 10
arr3 = np.linspace(0, 1, 5)      # 5 equally spaced values between 0 and 1
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("arr1:", arr1)
print("arr2 (arange):", arr2)
print("arr3 (linspace):", arr3)
print("matrix shape:", matrix.shape)

# --- Basic operations (vectorized, no loops needed) ---
print("\narr1 + 5 =", arr1 + 5)
print("arr1 * 2 =", arr1 * 2)
print("arr1.mean() =", arr1.mean())
print("arr1.std()  =", arr1.std())
print("arr1.sum()  =", arr1.sum())
print("arr1.max(), arr1.min() =", arr1.max(), arr1.min())

# --- Indexing & slicing ---
print("\narr2[2:5] =", arr2[2:5])
print("matrix[0, :] (row 0) =", matrix[0, :])
print("matrix[:, 1] (col 1) =", matrix[:, 1])

# --- Boolean masking (very commonly asked) ---
mask = arr1 > 20
print("\nMask (arr1 > 20):", mask)
print("Filtered values:", arr1[mask])

# --- Reshaping ---
reshaped = arr2.reshape(2, 5)
print("\narr2 reshaped to 2x5:\n", reshaped)

# --- Matrix operations ---
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("\nMatrix multiplication (a @ b):\n", a @ b)
print("Transpose of a:\n", a.T)


# 3. PANDAS - DATAFRAMES

import pandas as pd

print("\n" + "=" * 60)
print("3. PANDAS")
print("=" * 60)

# --- Reading CSV into a DataFrame ---
df = pd.read_csv("students.csv")
print("\nDataFrame:\n", df)

# --- Convert dtypes (CSV read karte time numbers text ban sakte hain) ---
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)

# --- Basic exploration ---
print("\ndf.head():\n", df.head())
print("\ndf.info():")
print(df.info())
print("\ndf.describe():\n", df.describe())

# --- Selecting columns / rows ---
print("\nOnly Name column:\n", df["Name"])
print("\nRows where Marks > 80:\n", df[df["Marks"] > 80])

# --- Adding a new column ---
df["Grade"] = df["Marks"].apply(lambda m: "A" if m >= 85 else ("B" if m >= 75 else "C"))
print("\nWith Grade column:\n", df)

# --- Sorting ---
print("\nSorted by Marks (desc):\n", df.sort_values(by="Marks", ascending=False))

# --- Group by ---
print("\nAverage marks by Grade:\n", df.groupby("Grade")["Marks"].mean())

# --- Handling missing values (common exam topic) ---
df_with_nan = df.copy()
df_with_nan.loc[1, "Marks"] = None
print("\nDataFrame with a missing value:\n", df_with_nan)
print("Missing value check:\n", df_with_nan.isnull())
df_filled = df_with_nan.fillna(df_with_nan["Marks"].mean())
print("\nFilled with mean:\n", df_filled)

# --- Writing DataFrame back to CSV ---
df.to_csv("students_processed.csv", index=False)
print("\nProcessed data saved to students_processed.csv")


# 4. MATPLOTLIB - DATA VISUALIZATION

import matplotlib.pyplot as plt

print("\n" + "=" * 60)
print("4. MATPLOTLIB")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# --- Bar chart ---
axes[0, 0].bar(df["Name"], df["Marks"], color="skyblue")
axes[0, 0].set_title("Marks per Student")
axes[0, 0].set_xlabel("Name")
axes[0, 0].set_ylabel("Marks")

# --- Line plot ---
axes[0, 1].plot(arr2, arr2 ** 2, marker="o", color="orange")
axes[0, 1].set_title("y = x^2")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("y")

# --- Scatter plot ---
axes[1, 0].scatter(df["Age"], df["Marks"], color="green")
axes[1, 0].set_title("Age vs Marks")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Marks")

# --- Pie chart ---
grade_counts = df["Grade"].value_counts()
axes[1, 1].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
axes[1, 1].set_title("Grade Distribution")

plt.tight_layout()
plt.savefig("revision_plots.png")
print("\nPlots saved as revision_plots.png")