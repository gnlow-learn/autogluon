from autogluon.timeseries import TimeSeriesPredictor, TimeSeriesDataFrame
import pandas as pd
from ts_util import ts

df = pd.read_csv("data/train.csv")

predictor = TimeSeriesPredictor(
    target="Rented Bike Count", 
    freq="H",
)\
    .fit(
        ts(df),
        presets="best",
        time_limit=300,
    )
