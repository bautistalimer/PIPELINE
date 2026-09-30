En este repositorio se desarrolla un pipeline de Procesamiento del Lenguaje Natural (PLN / NLP) diseñado para preprocesar, analizar y vectorizar un conjunto de textos informáticos comparativos utilizando técnicas de minería de texto y TF-IDF.

Objetivo principal
Procesar un corpus de 10 oraciones en inglés sobre características de lenguajes de programación (Python, C++, JavaScript, Rust, Go, Java) mediante un flujo estandarizado que transforma texto crudo en representaciones numéricas vectoriales e informes de frecuencia.

🛠️ Tecnologías y herramientas
Python 3

NLTK (Natural Language Toolkit): Tokenización, eliminación de stopwords, etiquetado gramatical (POS Tagging) y lematización mediante WordNet.

scikit-learn: Vectorización del texto refinado con TfidfVectorizer.

pandas: Generación y tabulación de matrices de datos.

matplotlib: Visualización de gráficos de distribución de palabras.

⚙️ Componentes y etapas del Pipeline
Limpieza y Filtrado de Stopwords (quitarStopwords_eng):
Tokeniza el texto, convierte a minúsculas y elimina palabras vacías en inglés junto con signos de puntuación y artefactos ('s, |, --, etc.).

Lematización Contextual (lematizar / get_wordnet_pos):
Mapea cada palabra a su categoría gramatical (sustantivo, verbo, adjetivo o adverbio) para reducir las palabras a su raíz canónica de diccionario.

Vectorización TF-IDF:
Construye el vocabulario final y convierte las oraciones lematizadas en una matriz de pesos de relevancia de términos.

Análisis e Informes de Resultados:

Calcula la jerarquía de las palabras más repetidas y menos utilizadas (FreqDist).

Detecta repeticiones internas por oración.

Grafica la distribución de frecuencias de las 20 palabras más comunes.
