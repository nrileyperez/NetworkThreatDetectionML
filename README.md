# Network Threat Detection ML 🛡️📊

> **Goal:** Train and compare several machine‑learning models that can automatically label each network flow in the **CICIDS‑2017** dataset as **benign** or different types of **attacks**.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Build](https://img.shields.io/badge/Project-Portfolio-success)

---

## ✨ Project Highlights
| What | Why it matters |
|------|----------------|
| **End‑to‑end pipeline** | Goes from raw CSV → cleaned DataFrame → trained & saved models → evaluation metrics. |
| **Model comparison** | Lines up *Logistic Regression* (baseline) against *Random Forest* and *XGBoost* to show strengths & weaknesses. |
| **Reproducible workflow** | Uses a `requirements.txt`, modular scripts, and joblib checkpoints so anyone can rerun in minutes. |
| **Security‑domain data** | Works with real IDS traffic from CICIDS‑2017 (or a smaller Kaggle‑hosted CSV) and tackles heavy class imbalance. |

---

## 🗂️ Repository Layout
~~~text
NetworkThreatDetectionML/
├─ data/                  # (ignored) place the CSV here
├─ models/                # trained .pkl files (ignored)
├─ data_loader.py         # read & preprocess dataset
├─ train_models.py        # fit LR, RF, XGB, save to /models
├─ evaluate_models.py     # classification report + confusion matrix
├─ requirements.txt
└─ README.md
~~~

---

## 🔧 Setup
~~~bash
# 1) Clone the repo
git clone https://github.com/nrileyperez/NetworkThreatDetectionML.git
cd NetworkThreatDetectionML

# 2) Create / activate a virtual‑env (Windows PowerShell example)
python -m venv .venv
.venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt
~~~

---

## 📥 Download the dataset
~~~python
import kagglehub, os
os.makedirs("data", exist_ok=True)

# Pull cleaned + pre‑processed CSV (~100 MB)
kagglehub.dataset_download(
    "ericanacletoribeiro/cicids2017-cleaned-and-preprocessed",
    download_path="data",
    unzip=True
)
~~~
*(Or download the ZIP from Kaggle and unzip into `data/` manually.)*

---

## 🚀 Usage

### Train all models
~~~bash
python train_models.py
~~~

### Evaluate on the held‑out test split
~~~bash
python evaluate_models.py
~~~

Example output (abridged):
~~~text
=== random_forest.pkl ===
accuracy  : 0.999
macro F1  : 0.97
           precision recall f1‑score support
Attack‑0       0.89   0.77     0.83      384
...
~~~

---

## 📈 Results

| Model | Accuracy | Macro F1 | Notes |
|-------|----------|----------|-------|
| Logistic Regression | 0.89 | 0.34 | Misses rare attacks—high imbalance sensitivity |
| Random Forest (50 trees) | **≈ 1.00** | **0.97** | Excellent on all classes; warrants leakage check |
| XGBoost | _(to‑do)_ | _(to‑do)_ | Strong baseline plus feature importances |

---

## 🔮 Roadmap / Improvements
- ✅ **Class‑weighting / SMOTE** for the linear model  
- 🔄 Time‑based or IP‑based train/test split to remove potential leakage  
- 📊 SHAP explanations & interactive dashboard (Streamlit)  
- ⏱️ Hyper‑parameter search (`GridSearchCV` / `Optuna`)  
- ☸️ Containerised inference endpoint (FastAPI + Docker)

---

## 🤝 Contributing
Issues and PRs are welcome! Feel free to open a discussion if you’d like to experiment with additional algorithms, feature engineering, or deployment tooling.

---

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.

---

*Built with ❤️ on a Razer Blade Stealth 13.*
