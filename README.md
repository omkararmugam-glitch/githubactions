# ML Pipeline Demo

This repository demonstrates a simple MLOps pipeline using GitHub Actions to automate machine learning model training and testing.

## Objective

The objective of this project is to automate the machine learning workflow using a CI/CD pipeline. The pipeline runs automatically when code is pushed to the repository.

## Workflow

The GitHub Actions workflow performs the following steps:

1. Checkout the repository code
2. Set up the Python environment
3. Install required dependencies
4. Run automated tests using pytest
5. Train the machine learning model
6. Save the trained model as an artifact

## Machine Learning Model

The project uses a **Random Forest Classifier** trained on the **Iris dataset** available in scikit-learn.

The training script performs the following tasks:

* Loads the dataset
* Splits data into training and testing sets
* Trains the model
* Evaluates accuracy
* Saves the trained model to the `models` folder

## Project Structure

ml-pipeline-demo/

.github/workflows/
  ml-pipeline.yml

src/
  train.py
  test_model.py

data/

models/

requirements.txt

README.md

## Running the Project Locally

Install dependencies:

pip install -r requirements.txt

Train the model:

python src/train.py

Run tests:

python -m pytest src/test_model.py -v

## CI/CD Pipeline

GitHub Actions automatically triggers the pipeline when code is pushed to the **main branch**. The pipeline ensures that the model training and testing processes run successfully before deployment.

## Output

After successful execution:

* The trained model is saved as `models/model.pkl`
* The model artifact is uploaded in the GitHub Actions workflow
[]
