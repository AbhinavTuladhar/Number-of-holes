from utils import predict
from random import seed, randint
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


if __name__ == "__main__":
    seed(22)
    columns = ['Number', 'Prediction']
    data = []
    for _ in range(100):
        number = randint(100, 10_000)
        prediction = predict(number)
        data.append([number, prediction])
    df = pd.DataFrame(data, columns=columns)
    print(df)
    
    df.to_csv('Sample output.csv', index=False)