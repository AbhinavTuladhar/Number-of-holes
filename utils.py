import numpy as np
import pandas as pd
from keras.models import load_model
import warnings
warnings.filterwarnings('ignore')


model = load_model('Holes_predictor.h5')

with open('Column names.txt', 'r') as file:
    value = file.readlines()
    column_names = [name.rstrip() for name in value]

# Create a function which counts the number of each digit
def count_digits(number: int) -> np.array:
    """
    Function to count the number of occurence of each digit in a number.
    """
    # Make a dictionary containing a count of occurence of each digit
    digit_dict = {x: 0 for x in range(0, 10)}
    for digit in str(number):
        # Increment the corresponding digit on each occurence.
        digit_dict[int(digit)] += 1
        
    to_return = list(digit_dict.values())
    return np.array(to_return)

def extract_features(number: int) -> pd.DataFrame:
    """
    Extract the required features for the keras model
    """
    digit_counts = count_digits(number)
    digit_counts = np.array([digit_counts])
    df = pd.DataFrame(digit_counts, columns=column_names)
    return df

def predict(number: int) -> int:
    dataframe = extract_features(number)
    predicted_value = model.predict(dataframe, verbose=0)
    return round(predicted_value[0][0])