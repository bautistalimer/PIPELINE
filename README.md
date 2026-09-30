# **🚀 Pipeline de Procesamiento del Lenguaje Natural (NLP)**

En este repositorio se desarrolla un **pipeline end-to-end de Procesamiento del Lenguaje Natural (PLN / NLP)** implementado en TP PIPELINE.py. El objetivo es preprocesar, analizar y vectorizar un conjunto de textos informáticos comparativos utilizando técnicas avanzadas de minería de texto y **TF-IDF**.

## **📌 Objetivo Principal**

Procesar un corpus de 10 oraciones en inglés centradas en las características de diversos lenguajes de programación (**Python, C++, JavaScript, Rust, Go, Java**). El proyecto transforma texto plano sin estructurar en representaciones numéricas vectoriales y reportes estadísticos de frecuencia.

## **🛠️ Tecnologías y Herramientas**

| Tecnología / Librería | Función Principal |
| :---- | :---- |
| **Python 3** | Lenguaje base del proyecto |
| **NLTK** | Tokenización, eliminación de *stopwords*, etiquetado gramatical (*POS Tagging*) y lematización con WordNet |
| **scikit-learn** | Vectorización matricial de texto refinado a través de TfidfVectorizer |
| **pandas** | Estructuración, tabulación y presentación formal de matrices de datos |
| **matplotlib** | Generación de gráficos analíticos para la distribución de frecuencias |

## **⚙️ Componentes y Etapas del Pipeline**

graph TD  
    A\[Corpus Crudo\] \--\> B\[1. Tokenización y Limpieza\]  
    B \--\> C\[2. Lematización Contextual POS\]  
    C \--\> D\[3. Vectorización TF-IDF\]  
    D \--\> E\[4. Análisis y Métricas FreqDist\]  
    E \--\> F\[5. Visualización Gráfica\]

### **1\. Limpieza y Filtrado de Stopwords (quitarStopwords\_eng)**

* Tokenización inicial del texto.  
* Conversión uniforme a minúsculas.  
* Filtrado de palabras vacías en inglés (*stopwords*).  
* Depuración de caracteres especiales y artefactos de puntuación ('s, |, \--, etc.).

### **2\. Lematización Contextual (lematizar / get\_wordnet\_pos)**

* Asignación de categoría gramatical (*POS Tagging*) a cada término (sustantivo, verbo, adjetivo, adverbio).  
* Lematización precisa utilizando WordNet para reducir palabras a su raíz canónica de diccionario.

### **3\. Vectorización TF-IDF**

* Construcción del vocabulario representativo final.  
* Transformación de oraciones procesadas en una matriz densa de pesos de relevancia de términos.

### **4\. Análisis e Informes de Resultados**

* **Jerarquía de Frecuencia:** Identificación de las palabras más y menos utilizadas mediante FreqDist.  
* **Análisis Intrasentencial:** Detección de repeticiones internas relevantes por oración.  
* **Visualización:** Generación de un gráfico con la distribución de frecuencias de los 20 términos principales.

## **🚀 Ejecución**

Asegúrate de tener instaladas las dependencias necesarias antes de ejecutar el script:

pip install nltk pandas scikit-learn matplotlib  
python "TP PIPELINE.py"  
