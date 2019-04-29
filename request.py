import urllib.request as request
import json
import numpy as np
import sys

from neural_network import ApplicationScoringNN
from session import update_input_weights

network = ApplicationScoringNN(0.1)


def mse(y, Y):
    return np.mean((y - Y) ** 2)


def get_data():
    response = request.urlopen('http://localhost:9080/learning?id=1&length=1500')
    data = json.loads(response.read())
    input_value = []
    for element in data:
        input_value.append((
            [element['mortgage'],
             element['autoLoan'],
             element['instantLoan'],
             element['beginDateOfSeniority'],
             element['salary'],
             element['certificate'],
             element['otherLoan'],
             element['dateOfBirth'],
             element['creditHistoryAssessment'],
             element['coBorrowerBeginDateOfSeniority'],
             element['coBorrowerSalary'],
             element['coBorrowerCertificate'],
             element['coBorrowerOtherLoan'],
             element['coBorrowerDateOfBirth'],
             element['coBorrowerCreditHistoryAssessment'],
             element['loanAmount'],
             element['loanInitialFee'],
             element['loanInterestRate'],
             element['loanCreditTerm']],
            element['result'])
        )
    return input_value


def training(epochs=1000):
    input_value = get_data()
    for e in range(epochs):
        inputs_ = []
        correct_predictions = []
        for input_stat, correct_predict in input_value:
            network.train(np.array(input_stat), correct_predict)
            inputs_.append(np.array(input_stat))
            correct_predictions.append(np.array(correct_predict))
        train_loss = mse(network.predict(np.array(inputs_).T), np.array(correct_predictions))
        sys.stdout.write("\rProgress: {}, Training loss: {}".format(str(100 * e / float(epochs))[:4], str(train_loss)[:5]))

    update_input_weights(network, 1)
