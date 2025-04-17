import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# df = pd.read_csv('data/cicids2017_cleaned.csv')
# print(df.columns.tolist())
def load_data():
    df = pd.read_csv('data/cicids2017_cleaned.csv')
    # Drop any non‑feature columns (e.g. timestamps, IPs if desired)
    df = df.drop(columns=['Flow ID', 'Source IP', 'Destination IP', 'Timestamp'], errors='ignore')
    # Label encode the target
    y = df.pop('Attack Type')
    le = LabelEncoder()
    y = le.fit_transform(y)  # normal=0, attack=1 (depending on your data)
    X = df.fillna(0)
    # Split
    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_data()
    print("Training set:", X_train.shape, y_train.shape)
    print("Test set:", X_test.shape, y_test.shape)
