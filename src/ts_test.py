from autogluon.timeseries import TimeSeriesPredictor
import pandas as pd
from ts_util import ts
import numpy as np

predictor = TimeSeriesPredictor.load("AutogluonModels/ag-20251106_012406")

df = pd.read_csv("data/test.csv")
df["Rented Bike Count"] = np.nan

predictions = predictor.predict(ts(df))
print(predictions)

pd.DataFrame(predictions).to_csv(
    "dist/ag_ts_300s.csv",
    encoding="utf-8",
    index_label="ID",
)
