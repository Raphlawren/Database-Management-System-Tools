# Database-Management-System Technologies

 ✨ Overview
This project implements and compares five research-backed database and ML tools on the Brazilian Higher Education Census dataset (658,877 rows, 189 features):
- **Feature Selection (Chi2, LASSO, PSO)**
- **MLflow** for experiment tracking
- **Feast** for feature storage and retrieval
- **Pinecone** for vector database retrieval
- **SQL-based Big Data Techniques**

## 🚀 Key Results
| Method | Accuracy | Features | Reduction | Runtime |
|--------|----------|----------|-----------|---------|
| Chi2 (Filter) | 97.31% | 30 | 84.13% | 5.72s |
| LASSO (Embedded) | 99.95% | 42 | 77.78% | 74.37s |
| PSO (Wrapper) | 99.96% | 112 | 40.74% | 1444s |

✅ **Feast** retrieval: 0.0183s  
✅ **Pinecone** ANN query: 0.251s (Top‑k retrieval)  
✅ **MLflow**: tracked all experiments and metrics with DagsHub integration.

## 📂 Repository Structure
- `notebooks/` – Jupyter notebooks for feature selection & pipeline steps
- `sql_scripts/` – SQL implementations for structured storage
- `mlflow_runs/` – MLflow logs and experiment artifacts

## 📖 Research Basis
Built on 5 papers including:
- Feature selection survey (Dhal & Azad, 2021)
- MLflow lifecycle (Chen, 2020)
- Vector DB retrieval (Han, 2023)
- Feature stores (Orr, 2021)
- Big data in RDBMS (2022)

## ▶️ How to Run
1. Clone repo: `git clone https://github.com/Raphlawren/Database-Management-System-Tools.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Explore notebooks in `notebooks/` to replicate experiments.

## 📊 Scoring Outcomes
| Tool/Model | Accuracy | Runtime | Infrastructure | Reproducibility | Total Score |
|------------|----------|---------|----------------|-----------------|-------------|
| LASSO | 84/100 | Best balance | | | |
| MLflow | 58/60 | Excellent tracking | | | |
| Feast | 70/80 | Fast retrieval | | | |
| Pinecone | 71/80 | ANN search | | | |

---

📎 **Linked Paper:** [Quantitative Analysis PDF](https://docs.google.com/document/d/1HNPK9bbwFek4TB4mbtCXFit6HCxBlQoKzFH8kwhvqjo/edit?usp=drivesdk)