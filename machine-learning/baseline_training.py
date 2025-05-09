# === 1. Import Library ===
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline
from sklearn.utils.class_weight import compute_class_weight
from sklearn.utils import resample
import joblib

# === 2. Load Dataset ===
df = pd.read_csv("labeled_data_clean.csv")
df = df.dropna(subset=['clean_tweet'])  # Hapus baris dengan nilai NaN di kolom clean_tweet

# === 3. Normalisasi Panjang Teks (Opsional Text Clipping) ===
def clip_text(text, max_len=200):
    return text if len(text) <= max_len else text[:max_len] + "..."

df['clean_tweet'] = df['clean_tweet'].apply(lambda x: clip_text(x))

# === 4. Tangani Imbalanced Dataset dengan Oversampling ===
df_minority_0 = df[df['class'] == 0]
df_minority_2 = df[df['class'] == 2]
df_majority_1 = df[df['class'] == 1]

# Upsample minority classes
df_minority_0_upsampled = resample(df_minority_0, 
                                    replace=True, 
                                    n_samples=len(df_majority_1), 
                                    random_state=42)

df_minority_2_upsampled = resample(df_minority_2, 
                                    replace=True, 
                                    n_samples=len(df_majority_1), 
                                    random_state=42)

# Gabungkan kembali
balanced_df = pd.concat([df_majority_1, df_minority_0_upsampled, df_minority_2_upsampled])

# === 5. Persiapan Fitur dan Label ===
X = balanced_df['clean_tweet']
y = balanced_df['class']

# === 6. Split Data ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 7. Pipeline TF-IDF + Logistic Regression ===
logreg_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000, class_weight='balanced'))
])

# === 8. Training Logistic Regression ===
logreg_pipeline.fit(X_train, y_train)

# === 9. Evaluasi Logistic Regression ===
y_pred_logreg = logreg_pipeline.predict(X_test)
print("--- Logistic Regression ---")
print("Accuracy:", accuracy_score(y_test, y_pred_logreg))
print("Precision:", precision_score(y_test, y_pred_logreg, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_logreg, average='weighted'))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_logreg))
print(classification_report(y_test, y_pred_logreg))

# === 10. Simpan Model Logistic Regression ===
joblib.dump(logreg_pipeline, 'model_logreg.pkl')

# === 11. Pipeline TF-IDF + Naive Bayes ===
nb_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# === 12. Training Naive Bayes ===
nb_pipeline.fit(X_train, y_train)

# === 13. Evaluasi Naive Bayes ===
y_pred_nb = nb_pipeline.predict(X_test)
print("--- Naive Bayes ---")
print("Accuracy:", accuracy_score(y_test, y_pred_nb))
print("Precision:", precision_score(y_test, y_pred_nb, average='weighted'))
print("Recall:", recall_score(y_test, y_pred_nb, average='weighted'))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_nb))
print(classification_report(y_test, y_pred_nb))
