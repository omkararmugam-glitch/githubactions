import os
import sys

sys.path.append(os.path.dirname(__file__))

from train import train_model


def test_model_training():
    accuracy = train_model()
    assert accuracy > 0


def test_model_accuracy_threshold():
    accuracy = train_model()
    assert accuracy > 0.85


def test_model_saved():
    train_model()
    assert os.path.exists("models/model.pkl")
