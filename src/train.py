from autogluon.tabular import TabularPredictor

predictor = TabularPredictor(label="Rented Bike Count")\
    .fit(
        "data/train.csv",
        presets="best",
        time_limit=300,
    )
