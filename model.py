# kerala_rainfall_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1️⃣ Load dataset
df = pd.read_csv("kerala_climate_data.csv")

# 2️⃣ Features & Target
X = df[['Altitude(m)', 'Temperature(°C)', 'Humidity(%)', 'WindSpeed(km/h)']]
y = df['Rainfall']

# 3️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Evaluate Model
y_pred = model.predict(X_test)
print(f"\n📊 Model Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

# 6️⃣ Get place input
place = input("\n🏙️ Enter a place in Kerala: ").strip().title()

# 7️⃣ Check if place exists in dataset
if place in df['City'].values:
    row = df[df['City'] == place].iloc[0]
    features = [[row['Altitude(m)'], row['Temperature(°C)'], row['Humidity(%)'], row['WindSpeed(km/h)']]]
    
    # Predict rainfall
    prediction = model.predict(features)[0]
    
    print(f"\n📍 Location: {place}")
    print(f"🗻 Altitude: {row['Altitude(m)']} m")
    print(f"🌡 Temperature: {row['Temperature(°C)']} °C")
    print(f"💧 Humidity: {row['Humidity(%)']} %")
    print(f"🌬 Wind Speed: {row['WindSpeed(km/h)']} km/h")
    
    if prediction == 1:
        print("\n🌧️ Rainfall is likely to occur here.")
    else:
        print("\n☀️ No rainfall expected.")
else:
    print("\n⚠️ Place not found in dataset! Please check spelling or add it to kerala_climate_data.csv.")
