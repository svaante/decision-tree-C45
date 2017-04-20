import numpy as np
from numpy.testing import assert_almost_equal, assert_equal
from id3 import Id3Estimator
from id3 import ErrorPruner
from id3.data import load_contact_lenses, load_will_wait, load_weather
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_iris
from id3 import export_graphviz

id3Estimator = Id3Estimator()


"""
def test_entropy():
    y = np.array([0, 1, 2, 2, 3])
    x = 1 / 5. * np.log2(1 / (1 / 5.)) + 1 / 5. * np.log2(1 / (1 / 5.)) + \
        2 / 5. * np.log2(1 / (2 / 5.)) + 1 / 5. * np.log2(1 / (1 / 5.))
    assert_almost_equal(Id3Estimator()._entropy(y), x)
"""


def test_fit():
    X, y, targets = load_weather()
    #bunch = load_weather()

    estimator = Id3Estimator()
    estimator.fit(X, y, targets, pruner=ErrorPruner())
    export_graphviz(estimator.tree_, "tree.dot")


def test_predict():
    X, y, targets = load_weather()
    #bunch = load_weather()

    estimator = Id3Estimator()
    estimator.fit(X, y, targets)
    assert_equal(estimator.predict(X), y)
