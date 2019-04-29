from sqlalchemy.orm import relationship

from app import db


class ResultIssueLoan(db.Model):
    __tablename__ = 'Result_Issue_Loan'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Boolean, nullable=False)
    score = db.Column(db.Float, nullable=False)
    borrower = relationship("RequestBorrower", uselist=False, back_populates="result")

    def __init__(self, answer, score):
        self.answer = answer
        self.score = score

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RequestBorrower(db.Model):
    __tablename__ = 'Request_Borrower'
    id = db.Column(db.Integer, primary_key=True)
    mortgage = db.Column(db.Integer, nullable=False)
    autoLoan = db.Column(db.Integer, nullable=False)
    instantLoan = db.Column(db.Integer, nullable=False)
    beginDateOfSeniority = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    certificate = db.Column(db.Integer, nullable=False)
    otherLoan = db.Column(db.Integer, nullable=False)
    dateOfBirth = db.Column(db.Integer, nullable=False)
    creditHistoryAssessment = db.Column(db.Integer, nullable=False)
    coBorrowerBeginDateOfSeniority = db.Column(db.Integer)
    coBorrowerSalary = db.Column(db.Integer)
    coBorrowerCertificate = db.Column(db.Integer)
    coBorrowerOtherLoan = db.Column(db.Integer)
    coBorrowerDateOfBirth = db.Column(db.Integer)
    coBorrowerCreditHistoryAssessment = db.Column(db.Integer)
    loanAmount = db.Column(db.Integer, nullable=False)
    loanInitialFee = db.Column(db.Integer, nullable=False)
    loanInterestRate = db.Column(db.Integer, nullable=False)
    loanCreditTerm = db.Column(db.Integer, nullable=False)
    resultId = db.Column(db.Integer, db.ForeignKey('Result_Issue_Loan.id'))
    result = relationship("ResultIssueLoan", back_populates="borrower")

    def __init__(self, mortgage, autoLoan, instantLoan, beginDateOfSeniority, salary, certificate, otherLoan,
                 dateOfBirth, creditHistoryAssessment, coBorrowerBeginDateOfSeniority, coBorrowerSalary,
                 coBorrowerCertificate, coBorrowerOtherLoan, coBorrowerDateOfBirth, coBorrowerCreditHistoryAssessment,
                 loanAmount, loanInitialFee, loanInterestRate, loanCreditTerm, result
                 ):
        self.mortgage = mortgage
        self.autoLoan = autoLoan
        self.instantLoan = instantLoan
        self.beginDateOfSeniority = beginDateOfSeniority
        self.salary = salary
        self.certificate = certificate
        self.otherLoan = otherLoan
        self.dateOfBirth = dateOfBirth
        self.creditHistoryAssessment = creditHistoryAssessment
        self.coBorrowerBeginDateOfSeniority = coBorrowerBeginDateOfSeniority
        self.coBorrowerSalary = coBorrowerSalary
        self.coBorrowerCertificate = coBorrowerCertificate
        self.coBorrowerOtherLoan = coBorrowerOtherLoan
        self.coBorrowerDateOfBirth = coBorrowerDateOfBirth
        self.coBorrowerCreditHistoryAssessment = coBorrowerCreditHistoryAssessment
        self.loanAmount = loanAmount
        self.loanInitialFee = loanInitialFee
        self.loanInterestRate = loanInterestRate
        self.loanCreditTerm = loanCreditTerm
        self.result = result


class InputWeights(db.Model):
    __tablename__ = 'Input_Weights'
    id = db.Column(db.Integer, primary_key=True)
    weights_0_1 = db.Column(db.String, nullable=False)
    weights_1_2 = db.Column(db.String, nullable=False)
    weights_2_3 = db.Column(db.String, nullable=False)

    def __init__(self, weights_0_1, weights_1_2, weights_2_3):
        self.weights_0_1 = weights_0_1
        self.weights_1_2 = weights_1_2
        self.weights_2_3 = weights_2_3
