# -*- coding: utf-8 -*-
"""dash.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BeyhxxHs0zGXpC7mwTR1qC6t-4pwNtPj
"""

!pip install dash
import dash
from dash import dcc, html
!pip install dash-bootstrap-components
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import joblib
import pandas as pd

# Cargar el modelo previamente entrenado
# model = joblib.load('C:/Users/Andres/Downloads/pickle_model.pkl')
model = joblib.load('ModeloClasificacion.joblib')

# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Diseño de la aplicación
app.layout = html.Div([
    html.H1("Predicción de Cluster con Machine Learning"),
    dcc.Input(id='input-recency', type='number', placeholder='Recency'),
    dcc.Input(id='input-frequency', type='number', placeholder='Frequency'),
    dcc.Input(id='input-monetary', type='number', placeholder='Monetary'),
    dcc.Input(id='input-segmentonombre', type='number', placeholder='SegmentoNombre'),
    html.Button('Predict', id='submit-val', n_clicks=0),
    html.Div(id='output')
])

# Callback para actualizar la salida basada en los inputs
@app.callback(
    Output('output', 'children'),
    [Input('submit-val', 'n_clicks')],
    [State('input-recency', 'value'),
     State('input-frequency', 'value'),
     State('input-monetary', 'value'),
     State('input-segmentonombre', 'value')]
)
def update_output(n_clicks, recency, frequency, monetary, segmentonombre):
    if n_clicks is not None and n_clicks > 0:
        # Crear un DataFrame con los datos de entrada
        data = {
            'Recency': [recency],
            'Frequency': [frequency],
            'Monetary': [monetary],
            'SegmentoNombre': [segmentonombre]
        }
        df = pd.DataFrame(data)

        # Realizar la predicción del cluster
        prediction = model.predict(df)[0]

        return f"El Cluster predicho es: {prediction}"
    else:
        return "Ingrese los datos y haga clic en 'Predict'"