# Customer Clustering Project

Segmenting customers into groups based on **Age** and **Buying Score** using K-Means clustering, with an interactive Gradio app to predict a new customer's segment.

## What's inside

- `clustering_data.ipynb` — full analysis: EDA, choosing the number of clusters (Elbow method + Silhouette score), training K-Means, labeling and visualizing the clusters, and comparing scaled vs. unscaled features.
- `customer_clustering_data.xlsx` — source dataset (120 synthetic customers: `CustomerID`, `Age`, `BuyingScore`).
- `app.py` — standalone Gradio app that loads the saved model and predicts a customer's segment from `Age` and `BuyingScore`.
- `kmeans_customer_model.pkl` / `cluster_mapping.pkl` — trained model and cluster-name mapping, produced by the notebook.

## Clusters

| Cluster | Age | Buying Score | Label |
|---|---|---|---|
| 0 | ~21.5 | ~24.8 | Low-Value Customers |
| 1 | ~35.4 | ~79.8 | VIP Customers |
| 2 | ~55.5 | ~46.0 | Moderate Customers |

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Usage

Run the notebook end-to-end to reproduce the analysis and regenerate the `.pkl` files, or run the app directly:

```bash
python app.py
```

This launches a local Gradio interface where you can enter a customer's `Age` and `Buying Score` and get their predicted segment.
