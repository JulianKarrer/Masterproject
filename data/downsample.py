import pandas as pd
import sys

if __name__ == "__main__":
    print("argument 1: filename, argument 2: downsample to every n-th line")
    df = pd.read_csv(sys.argv[1])
    df_downsampled = df.iloc[::int(sys.argv[2])] 
    df_downsampled.to_csv(sys.argv[1]+"-downsampled.csv", index=False)