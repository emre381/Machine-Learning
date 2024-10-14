import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import openpyxl

# Veriyi hazırlama: yaş, kan basıncı, kolesterol ve hastalık durumu verisi tahmin etme
# data = {
#     'Yas': [25, 50, 45, 30, 60],
#     'Kan_basinci': [120, 140, 130, 110, 150],
#     'Kolesterol': [180, 240, 200, 160, 220],
#     'Hastalik': [0, 1, 1, 0, 1]  # 0 hayır, 1 evet 
# }

# df = pd.DataFrame(data)
df=pd.read_excel('karar_agaci_veri_100.xlsx')

# Hastalik sütununu hedef olarak kullanıyoruz, bu yüzden X'te yer almamalı
X = df[['Yas', 'Kan_Basinci', 'Kolesterol']]  # Özellikler (bağımsız değişkenler)
y = df['Hastalik']  # Hedef değişken (bağımlı değişken)

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model oluşturma ve eğitme
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
y_pred = classifier.predict(X_test)
# confusion matrix hesaplama
cm=confusion_matrix(y_test,y_pred)

disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title('Matrix karar ağacı')
plt.show()
















# # Modelin doğruluğunu hesaplama
# accuracy = accuracy_score(y_test, y_pred)
# # print(f"Model doğruluk oranı: {accuracy}")
# yas = int(input("Yaşınızı giriniz:"))
# kan_basinci = int(input("Kan basıncınızı giriniz:"))
# kolesterol = int(input("Kolesterol seviyenizi giriniz:"))

# # tahmin olustur
# kullanici_verisi=pd.DataFrame([[yas,kan_basinci,kolesterol]],columns=['Yas','Kan_Basinci','Kolesterol'])
# tahmin = classifier.predict(kullanici_verisi)
# sonuc="Hastalık var" if tahmin[0]==1 else  "Hastalık yok"
# print(f"Tahmin:{sonuc}")
