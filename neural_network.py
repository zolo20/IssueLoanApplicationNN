import numpy as np
import scipy.special as scipy

from session import get_input_weights


class ApplicationScoringNN:

    def activate_function(self, x):
        return 1 / (1 + scipy.expit(-x))

    def __init__(self, learning_rate):
        self.weights_0_1 = np.asarray(get_input_weights(0, 1))
        self.weights_1_2 = np.asarray(get_input_weights(1, 1))
        self.weights_2_3 = np.asarray(get_input_weights(2, 1))
        self.activate_function_mapper = np.vectorize(self.activate_function)
        self.learning_rate = np.array([learning_rate])

    def predict(self, inputs):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.activate_function_mapper(inputs_1)
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.activate_function_mapper(inputs_2)
        inputs_3 = np.dot(self.weights_2_3, outputs_2)
        outputs_3 = self.activate_function_mapper(inputs_3)
        return outputs_3

    def train(self, inputs, expected_predict):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.activate_function_mapper(inputs_1)
        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.activate_function_mapper(inputs_2)
        inputs_3 = np.dot(self.weights_2_3, outputs_2)
        outputs_3 = self.activate_function_mapper(inputs_3)
        actual_predict = outputs_3[0]

        error_layer_3 = np.array([actual_predict - expected_predict])
        gradient_layer_3 = outputs_3 * (1 - outputs_3)
        weights_delta_layer_3 = error_layer_3 * gradient_layer_3
        self.weights_2_3 -= np.dot(weights_delta_layer_3, outputs_3) * self.learning_rate

        error_layer_2 = np.dot(weights_delta_layer_3, self.weights_2_3)
        gradient_layer_2 = outputs_2 * (1 - outputs_2)
        weights_delta_layer_2 = error_layer_2 * gradient_layer_2
        self.weights_1_2 -= (np.dot(weights_delta_layer_2, outputs_2)) * self.learning_rate

        error_layer_1 = np.dot(weights_delta_layer_2, self.weights_1_2)
        gradient_layer_1 = outputs_1 * (1 - outputs_1)
        weights_delta_layer_1 = error_layer_1 * gradient_layer_1
        self.weights_0_1 -= np.dot(weights_delta_layer_1, outputs_1) * self.learning_rate
