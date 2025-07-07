import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import classification_report
import joblib

# Load data
df = pd.read_csv('dataset/creditcard.csv')

# Split into features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Balance the data
rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate (optional printout)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, 'fraud_model.pkl')
