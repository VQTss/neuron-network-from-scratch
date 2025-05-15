import numpy as np

class Activation_Softmax:

    # Forward pass

    def forward(self,inputs):

        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs,axis=1,keepdims=True))

        # Normalized them for each sample

        probabilities =  exp_values / np.sum(exp_values, axis=1, keepdims=True)

        self.outputs = probabilities