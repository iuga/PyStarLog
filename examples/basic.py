from starlog import log_experiment
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

log_experiment(
    description="Some description",
    tag="ml", version="1.0", number=17,
    records={
        "AUC": 0.798,
        "CV": [0.5, 0.45],
        "Iris dataset": iris_df,
        "Iris columns": iris_df.columns,
        "Iris column": iris_df['petal width (cm)']
    }
)
