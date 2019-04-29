import json

from app import db
from models import InputWeights, RequestBorrower, ResultIssueLoan


def get_input_weights(numberLayer, weights_id):
    weights = InputWeights.query.filter_by(id=weights_id).first()
    if numberLayer == 0:
        return json.loads(weights.weights_0_1)
    elif numberLayer == 1:
        return json.loads(weights.weights_1_2)
    elif numberLayer == 2:
        return json.loads(weights.weights_2_3)


def update_input_weights(network, weights_id):
    weights = InputWeights.query.filter_by(id=weights_id).first()
    weights.weights_0_1 = json.dumps(network.weights_0_1.tolist())
    weights.weights_1_2 = json.dumps(network.weights_1_2.tolist())
    weights.weights_2_3 = json.dumps(network.weights_2_3.tolist())
    db.session.commit()


def save_request_borrower(analize_data, result):
    request_borrower = RequestBorrower(analize_data['mortgage'], analize_data['autoLoan'], analize_data['instantLoan'],
                                       analize_data['beginDateOfSeniority'],
                                       analize_data['salary'], analize_data['certificate'],
                                       analize_data['otherLoan'], analize_data['dateOfBirth'],
                                       analize_data['creditHistoryAssessment'],
                                       analize_data['coBorrowerBeginDateOfSeniority'], analize_data['coBorrowerSalary'],
                                       analize_data['coBorrowerCertificate'],
                                       analize_data['coBorrowerOtherLoan'], analize_data['coBorrowerDateOfBirth'],
                                       analize_data['coBorrowerCreditHistoryAssessment'], analize_data['loanAmount'],
                                       analize_data['loanInitialFee'], analize_data['loanInterestRate'],
                                       analize_data['loanCreditTerm'], result)

    db.session.add(request_borrower)
    db.session.commit()


def save_result(result_issue_loan):
    db.session.add(result_issue_loan)
    db.session.commit()
