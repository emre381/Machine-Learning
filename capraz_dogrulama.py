import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import openpyxl



# df = pd.DataFrame(data)
df=pd.read_excel('karar_agaci_veri_100.xlsx')

# Hastalik sütununu hedef olarak kullanıyoruz, bu yüzden X'te yer almamalı
X = df[['Yas', 'Kan_Basinci', 'Kolesterol']]  # Özellikler (bağımsız değişkenler)
y = df['Hastalik']  # Hedef değişken (bağımlı değişken)

# Veriyi eğitim ve test setlerine ayırma
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model oluşturma ve eğitme
# classifier = DecisionTreeClassifier()
# classifier.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
# y_pred = classifier.predict(X_test)
# accuracy=accuracy_score(y_test,y_pred)
# print(f"Model doğruluk oranı:{accuracy}")
classifier=DecisionTreeClassifier(max_depth=3,min_samples_split=2,min_samples_leaf=2)
cross_val_scores=cross_val_score(classifier,X,y,cv=5 )
print(f"8-Katlamalı çapraz doğrulama skorları:{cross_val_scores}")
print(f"Ortalama doğruluk Skoru:{cross_val_scores.mean():.2f}")










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
