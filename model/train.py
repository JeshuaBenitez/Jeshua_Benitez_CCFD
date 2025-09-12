from os import PathLike
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path('data/creditcard.csv'))
y = df.pop('Class')
X = df
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

print ('Training model.. ')
clf = RandomForestClassifier(
    # actualice el bosque de 10 árboles a 100, ya que puede quedarse corto
    # para problemas complejos (con el dataset que tengo de 284,208 datos).
    # esto ayuda ya que tiene mejor capacidad de generalización, más robusto, menos azar.
    # tardará en entrenar un poco mas pero sigue siendo razonable.
    n_estimators = 100,
    # actualixe que cada árbol tuviera como máximo 2 niveles de profundidad,
    # muy "chatos", con poco capacidad de aprender patrones.
    # ahora los árboles puedes crecer hasta que sea necesario (se detienen cuando 
    # no hay más ganancia o quedan pocos datos), esto permite que el modelo capture
    # patrones más complejos.
    max_depth=None,
    random_state=0,
    # agregue class_weight ya que el algoritmo pone más peso a la clase minoritaira.
    # esto obliga al bosque a prestar más atención a detectar la clase 1.
    class_weight="balanced")
clf.fit(X_train, y_train)
print ('Saving model..')

dump(clf, pathlib.Path('model/creditcard-v1.joblib'))
