#!/bin/bash

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Conda is not installed. Please install Conda first."
    exit 1
fi

# Initialize conda
source "$(conda info --base)/etc/profile.d/conda.sh"

# Create conda environment with Python 3.11
conda create -n neuron-network python=3.11 -y

# Activate the environment
conda activate neuron-network

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found in the current directory."
    exit 1
fi

echo "Conda environment 'neuron-network' set up successfully."