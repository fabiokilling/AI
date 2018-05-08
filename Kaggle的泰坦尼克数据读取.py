import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
titanic_df = pd.read_csv('C:\\Users\\ArcherX\\Desktop\\train.csv', dtype={"Age": np.float64},)
test_df = pd.read_csv('C:\\Users\\ArcherX\\Desktop\\test.csv', dtype={"Age": np.float64},)
titanic_df.head()
titanic_df.info()
print("----------------------------")
test_df.info()
titanic_df = titanic_df.drop(['PassengerId','Name','Ticket'], axis=1)
test_df = test_df.drop(['Name','Ticket'], axis=1)
