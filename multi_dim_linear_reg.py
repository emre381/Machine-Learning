import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Veri hazırlama
data = {
    'Ev_Buyuklugu': [120, 250, 175, 300, 220],
    'Oda_Sayisi':[3,5,4,6,4],
    'Fiyat': [2400000, 5000000, 3500000, 6000000, 4400000]
}

# Veriyi DataFrame'e çevirme
df = pd.DataFrame(data)

# Özellikler ve hedef değişken ayırma
X = df[['Ev_Buyuklugu','Oda_Sayisi']]  # Özellik (bağımsız değişken)
y = df['Fiyat']  # Hedef (bağımlı değişken)
# modeli eğitme
# Veriyi eğitim ve test olarak bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur
model = LinearRegression()
model.fit(X_train, y_train)  # Modeli eğitim verisiyle eğitme

# # Test verisi ile tahmin yapma
# y_pred = model.predict(X_test)

# # Hata hesaplama (MSE - Ortalama Kare Hatası)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# print(f"Ortalama kare hatası (MSE): {rmse}")
# ev_buyuklugu=float(input("Lütfen evin büyüklüğünü (m²)girin:"))
# tahmini_fiyat=model.predict([[ev_buyuklugu]])
# print(f"Buevin tahmini fiyatı:{tahmini_fiyat[0]:.2f} TL")

ev_buyuklugu=float(input("Lütfen evin büyüklüğünü (m²)girin:"))
oda_sayisi=int(input("Lütfen evin oda sayısını girin:"))
tahmini_fiyat=model.predict([[ev_buyuklugu,oda_sayisi]])
print(f"Bu evin tahmini fiyatı :{tahmini_fiyat[0]:.3f} TL")

