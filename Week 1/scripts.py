import pandas as pd

def read_df(filename):
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    elif filename.endswith('.parquet'):
        df = pd.read_parquet(filename)

    df['duration'] = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
    df['duration'] = df['duration'].apply(lambda td: td.total_seconds() / 60)

    df = df[(df['duration'] >= 1) & (df['duration'] <= 60)]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)

    return df
