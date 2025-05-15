import numpy as np


class Loss:
    
    #Calculate the data and regularization losses
    # Given model output and ground truth values
    def calculate(self, output,y):
        
        # Calculate sample losses
        sample_losses = self.forward(output,y)

        # Calculate mean loss

        data_loss = np.mean(sample_losses)


        return data_loss