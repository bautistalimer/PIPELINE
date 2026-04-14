import nltk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
import string


#DESCARGA DE RECURSOS (Se ejecuta una sola vez)
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('stopwords')


#STOPWORDS
def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``", ".-"] ]
    return texto_limpio

#LEMATIZACION
def get_wordnet_pos(word):
    """Mapeo de etiquetas POS según ejemploLematizacion3.py"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def lematizar(texto):
    """Lematización usando el lema de diccionario"""
    return [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]

lemmatizer = WordNetLemmatizer()



#CORPUS
raw_docs = [
    "Python is an interpreted and high-level language, while CPlus is a compiled and low-level language .-",
    "JavaScript runs in web browsers, while Python is used in various applications, including data science and artificial intelligence.",
    "JavaScript is dynamically and weakly typed, while Rust is statically typed and ensures greater data security .-",
    "Python and JavaScript are interpreted languages, while Java, CPlus, and Rust require compilation before execution.",
    "JavaScript is widely used in web development, while Go is ideal for servers and cloud applications.",
    "Python is slower than CPlus and Rust due to its interpreted nature.",
    "JavaScript has a strong ecosystem with Node.js for backend development, while Python is widely used in data science .-",
    "JavaScript does not require compilation, while CPlus and Rust require code compilation before execution .-",
    "Python and JavaScript have large communities and an extensive number of available libraries.",
    "Python is ideal for beginners, while Rust and CPlus are more suitable for experienced programmers."
]

#PIPELINE
corpus_preparado_tokens = []
for doc in raw_docs:
    tokens = word_tokenize(doc)
    limpios = quitarStopwords_eng(tokens)
    lemas = lematizar(limpios)
    corpus_preparado_tokens.append(lemas)


corpus_final = [" ".join(tokens) for tokens in corpus_preparado_tokens]

#APLICAR TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_final)
vocabulario = vectorizer.get_feature_names_out()

#RESULTADOS:
print("--- 1. CORPUS PREPARADO ---")
for i, doc in enumerate(corpus_final): print(f"{i+1}: {doc}")

print("\n--- 2. VOCABULARIO GENERADO ---")
print(vocabulario)

print("\n--- 3. MATRIZ TF-IDF (Tabulada como en el PDF) ---")
df_tfidf = pd.DataFrame(X.toarray(), columns=vocabulario, index=[f"Oración {i+1}" for i in range(10)])
print(df_tfidf.to_string())


#INFORME DE LOS RESULTADOS
palabras_totales = [p for sub in corpus_preparado_tokens for p in sub]
fdist = FreqDist(palabras_totales)

print("\n--- 4. INFORME DE CONCLUSIONES ---")

print(f"A. Jerarquía de las 6 palabras más usadas: {fdist.most_common(6)}")

print(f"B. La palabra menos utilizada es: '{min(fdist, key=fdist.get)}'")

print("C. Palabras repetidas en la misma oración:")
print("   - Oración 1: 'language' (se repite al definir tipos de lenguaje)")
print("   - Oración 8: 'compilation' y 'require' (se repiten por énfasis técnico)")

plt.figure(figsize=(10, 5))
fdist.plot(20, title="Distribución de Frecuencia de Palabras", cumulative=False)
plt.show()