from autogluon.tabular import TabularPredictor
import pandas as pd

predictor = TabularPredictor.load("AutogluonModels/ag-20251105_064208")

predictions = predictor.predict("data/test.csv")
print(predictions)

pd.DataFrame(predictions).to_csv(
    "dist/ag_300s.csv",
    encoding="utf-8",
    index_label="ID",
)
