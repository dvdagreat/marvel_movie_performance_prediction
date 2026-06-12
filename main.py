import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('./dataset/marvel_movie_data.csv')
df2 = pd.get_dummies(df, columns=['genres', 'cast', 'director'])

def calculate_smash_hit(row):
  if row['worldwide_collection'] > 800000000:
    return 1
  else:
    return 0

df2['smash_hit'] = df2.apply(calculate_smash_hit, axis = 1)

X = df2.drop(['title', 'worldwide_collection', 'smash_hit'], axis = 1)
y = df2['smash_hit']

model = linear_model.LogisticRegression(max_iter=1000)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)

model.fit(X_train, y_train)

pred = model.predict(X_test)


arr = y_test.to_numpy()
print(f"y_test: {arr}")
print(f"pred: {pred}")

result = accuracy_score(y_test, pred)
print(f"Accuracy Score: {result}")
print(f"Model accuracy: {round(result * 100, 2)}%")

result = classification_report(y_test, pred)
print("Classification Report:")
print(result)
