import os
from pathlib import Path
import numpy as np
import torch


_MODEL_PATH = os.path.join("/opt/ml/", "model")  # Path where all your model(s) live in


class Model:
    def __init__(self, model_path: Path):
        self.model = torch.nn.Sequential(
            torch.nn.Linear(1, 100),
            torch.nn.Dropout(0.01),
            torch.nn.ReLU(),
            torch.nn.Linear(100, 100),
            torch.nn.Dropout(0.01),
            torch.nn.ReLU(),
            torch.nn.Linear(100, 100),
            torch.nn.Dropout(0.01),
            torch.nn.ReLU(),
            torch.nn.Linear(100, 1),
        )
        self.model.load_state_dict(torch.load(model_path, weights_only=True))
        self.model.eval()

    def predict(self, x: float) -> np.float16:
        with torch.no_grad():
            output: torch.Tensor = self.model(torch.Tensor([x]))
        return output.numpy()[0]


class ModelService(object):
    model: Model | None = None

    @classmethod
    def get_model(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model is None:
            cls.model = Model(Path(_MODEL_PATH) / "model.pth")
        return cls.model

    @classmethod
    def preprocess(cls, input: dict):
        """For the input, do the predictions and return them."""
        return input["x"]

    @classmethod
    def predict(cls, input: float) -> np.float16:
        """For the input, do the predictions and return them."""
        clf = cls.get_model()
        return clf.predict(input)

    @classmethod
    def postprocess(cls, output: np.float16):
        """For the input, do the predictions and return them."""
        return float(output)


def predict(json_input):
    """
    Prediction given the request input
    :param json_input: [dict], request input
    :return: [dict], prediction
    """
    model_input = ModelService.preprocess(json_input)
    prediction = ModelService.predict(model_input)
    print(prediction)
    result = ModelService.postprocess(prediction)
    return result
