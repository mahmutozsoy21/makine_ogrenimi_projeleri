import pandas as pd
from sklearn.model_selection import train_test_split

# Dataset'i oku
df = pd.read_csv("spam_email_dataset_2000_clean.csv")

# X ve y ayır
X = df["text"]
y = df["label"]

# %80 eğitim, %20 test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Eğitim veri sayısı:", len(X_train))
print("Test veri sayısı:", len(X_test))

from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF vektörleştirici
tfidf = TfidfVectorizer(
    max_features=1000
)

# Eğitim verisini fit + transform
X_train_tfidf = tfidf.fit_transform(X_train)

# Test verisini sadece transform
X_test_tfidf = tfidf.transform(X_test)

print("Vektör boyutu:", X_train_tfidf.shape)

from sklearn.linear_model import LogisticRegression

# Logistic Regression modeli
model = LogisticRegression(
    max_iter=300,
    class_weight="balanced"
)

# Modeli eğit
model.fit(X_train_tfidf, y_train)

print("Model eğitildi!")

from sklearn.metrics import accuracy_score, classification_report

# Test verisi üzerinde tahmin
y_pred = model.predict(X_test_tfidf)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk (Accuracy):", accuracy)

# Detaylı rapor
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))


# ---- Yeni e-posta testi ----
ornek_eposta = [
    "Tebrikler! Büyük ödül kazandınız, hemen linke tıklayın.",
    "Toplantı yarın saat 10:00'da yapılacaktır."
]

ornek_tfidf = tfidf.transform(ornek_eposta)
tahminler = model.predict(ornek_tfidf)

for mail, sonuc in zip(ornek_eposta, tahminler):
    print(f"\nE-posta: {mail}")
    print("Tahmin:", sonuc)
