from starlog import log_experiment
from sklearn.datasets import load_iris
import pandas as pd

# Load a mock dataframe
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Register the experiment results
log_experiment(
    # What did you do?
    # Did you add new features? change the validation method?
    description="Adding the monthly_mean_ads_crt feature into the model",
    # Tag to describe the line of experiments, like:
    # - ml for machine learning model progress
    # - feateng for feature engineering
    # - ensemble for model ensembling
    tag="ml",
    # Major version of your model
    version="1.0",
    # Experiment number: You can not override previous experiments
    number=1,
    # All the experiment context and results:
    records={
        # Record the key performance metric on the test set
        "AUC": 0.798,
        # Record the performance on the folds
        "CV": [0.5, 0.45, 0.453, 0.5132, 0.4987],
        # Record some data frame
        # It could be the feature importance
        "Iris dataset": iris_df,
        # Or the features used to train the model
        "Iris columns": iris_df.columns,
        # Or some examples:
        "Iris column": iris_df['petal width (cm)']
        # And any other information you want ...
    }
)
