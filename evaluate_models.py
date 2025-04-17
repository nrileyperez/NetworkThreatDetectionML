import joblib
from data_loader import load_data
from sklearn.metrics import classification_report, confusion_matrix

def evaluate():
    X_train, X_test, y_train, y_test = load_data()
    for path in ['models/logistic_regression.pkl',
                 'models/random_forest.pkl',
                 #
                 ]:
        model = joblib.load(path)
        preds = model.predict(X_test)
        print(f"\n=== {path.split('/')[-1]} ===")
        print(classification_report(y_test, preds))
        print("Confusion matrix:")
        print(confusion_matrix(y_test, preds))

if __name__ == '__main__':
    evaluate()
