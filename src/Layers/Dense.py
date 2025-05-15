import numpy as np

class Dense:

    # Layer initialization
    def __init__(self,n_inputs, n_neurons):
        # Initialization weights and biases
        self.weights =  0.01 * np.random.rand(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    
    # forwards pass
    def forward(self, inputs):
        # Calculate output values from inputs, weights, biases
        self.output = np.dot(inputs,self.weights) + self.biases