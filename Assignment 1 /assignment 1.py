"""
CSET343 - Lab Experiment 1
AI in Healthcare - Reading Tabular, Textual, Image, Signal, Medical Data
SECTION 1: ENVIRONMENT SETUP
"""

import pandas as pd             
import numpy as np                
import matplotlib.pyplot as plt   
import wfdb                       
import warnings

warnings.filterwarnings("ignore")  

print("Environment ready! Sab packages import ho gaye.")


# SECTION 2: TABULAR DATA - UCI Cleveland Heart Disease Dataset

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix

print("\n" + "=" * 60)
print("SECTION 2: TABULAR DATA (Heart Disease)")
print("=" * 60)


column_names = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
heart_df = pd.read_csv(url, names=column_names, na_values="?")
# na_values="?" -> file me jahan bhi "?" likha hai, use missing (NaN) treat karega

print("\nDataset shape (rows, columns):", heart_df.shape)
print("\nFirst 5 rows:\n", heart_df.head())

# --- Schema / missingness inspection ---
print("\nData types:\n", heart_df.dtypes)
print("\nMissing values per column:\n", heart_df.isnull().sum())

# --- Handle missing values ---
heart_df = heart_df.dropna()   # thodi si rows hain missing wali, unhe drop kar rahe hain
print("\nShape after dropping missing rows:", heart_df.shape)

# --- Convert target to binary (0 = no disease, 1+ = disease present) ---
heart_df["target"] = heart_df["target"].apply(lambda x: 1 if x > 0 else 0)
print("\nTarget distribution:\n", heart_df["target"].value_counts())

# --- Basic EDA ---
print("\nSummary statistics:\n", heart_df.describe())

plt.figure(figsize=(8, 6))
plt.imshow(heart_df.corr(), cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(heart_df.columns)), heart_df.columns, rotation=90)
plt.yticks(range(len(heart_df.columns)), heart_df.columns)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("heart_correlation.png")
print("\nCorrelation heatmap saved as heart_correlation.png")

# --- Train a baseline classifier ---
X = heart_df.drop(columns=["target"])
y = heart_df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))