import joblib
import pandas as pd
import gradio as gr

model = joblib.load('kmeans_customer_model.pkl')
cluster_mapping = joblib.load('cluster_mapping.pkl')

def predict_customer_cluster(age, buying_score):
    new_data = pd.DataFrame([[age, buying_score]], columns=['Age', 'BuyingScore'])
    predicted_label = model.predict(new_data)[0]
    return cluster_mapping.get(predicted_label, 'Unknown')

iface = gr.Interface(
    fn=predict_customer_cluster,
    inputs=[gr.Number(label="Age"), gr.Number(label="Buying Score")],
    outputs="text",
    title="Customer Cluster Predictor"
)

iface.launch()
