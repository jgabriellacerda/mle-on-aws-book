from __future__ import absolute_import


from prediction.prediction import predict as predict_function


def predict(json_input):
    """
    Prediction given the request input
    :param json_input: [dict], request input
    :return: [dict], prediction
    """
    return predict_function(json_input=json_input)
