import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["life satisfaction"]].values

# Visualize the data
lifesat.plot(
    kind="scatter", grid=True, x="GDP per capita (USD)",
    y="Life satisfaction"
)