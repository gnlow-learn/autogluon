from autogluon.timeseries import TimeSeriesDataFrame
import pandas as pd

def ts(df: pd.DataFrame):
    df["Date"] = pd.to_datetime(df["Date"] + " " + df["Hour"].astype(str), format="%d/%m/%Y %H")
    df["item_id"] = 1

    tsdf = TimeSeriesDataFrame.from_data_frame(
        df,
        timestamp_column="Date",
    )
    return tsdf
