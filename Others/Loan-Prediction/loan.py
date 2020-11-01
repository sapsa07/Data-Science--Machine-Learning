import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv") 
#Reading the dataset in a dataframe using Pandas

print(df.describe())

