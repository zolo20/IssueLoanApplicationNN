import json

from app import app
from flask import request

from models import ResultIssueLoan
from neural_network import ApplicationScoringNN
from session import save_request_borrower, save_result

network = ApplicationScoringNN(0.1)


@app.route('/predict', methods=['POST'])
def predict():
    inputs = []
    content = dict(request.get_json())
    analize_data = {}
    for key, value in content.items():
        if key != 'id' and key != 'result':
            inputs.append(value)
            analize_data[key] = value

    score = network.predict(inputs)[0]
    answer = score > 0.5
    result_issue_loan = ResultIssueLoan(answer, score)
    save_result(result_issue_loan)
    save_request_borrower(analize_data, result_issue_loan)
    return str(score)
