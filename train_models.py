import joblib
from data_loader import load_data
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def train_and_save():
    X_train, X_test, y_train, y_test = load_data()

    models = {
        # 'logistic_regression': LogisticRegression(max_iter=100),
         'random_forest': RandomForestClassifier(n_estimators=50),
        # 'xgboost': XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
    }

    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        joblib.dump(model, f'models/{name}.pkl')
        print(f"→ Saved to models/{name}.pkl")

if __name__ == '__main__':
    import os
    os.makedirs('models', exist_ok=True)
    train_and_save()
