import pandas as pd
from .models import Diabetes
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score


# Data Collecting
df = pd.DataFrame(Diabetes.objects.all().values())

# Preprocessing
X = df.drop(columns=['outcome','id']) 
y = df['outcome']

# PreProcessing
scaler = preprocessing.StandardScaler().fit(X)
X_scaled = scaler.transform(X)

# Model Inisialization
model = LogisticRegression(max_iter=1000)

# Training
model.fit(X_scaled, y)

