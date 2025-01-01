#!/bin/bash

# Step 1: Preprocess Data
python preprocess_data.py

# Step 2: Retrain Model
python retrain_model.py

# Step 3: Evaluate Model
python evaluate_model.py

# Step 4: Deploy Model
python deploy_model.py
