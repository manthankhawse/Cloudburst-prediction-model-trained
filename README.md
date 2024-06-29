# Cloudburst Prediction Model

## Overview

This project is a cloudburst prediction model. The model predicts the likelihood of a cloudburst based on various meteorological parameters.

## Features

- **Support Vector Classifier**: Model trained for predictions.
- **FastAPI**: Used for building the API.
- **Pydantic**: Used for data validation.
- **CORS Middleware**: Configured to allow cross-origin requests.
- **Model Prediction Endpoint**: Exposes an endpoint to make predictions using the trained model.

## Requirements

- Python 3.8+
- `requirements.txt` lists the necessary packages:
  ```
  fastapi
  uvicorn
  pydantic
  scikit-learn==1.2.2
  numpy==1.23.5
  ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/manthankhawse/Cloudburst-prediction-model-trained.git
   cd cloudburst-prediction
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

3. **Make a prediction**:
   Send a POST request to the `/predict` endpoint with the following JSON payload:
   ```json
   {
     "temperature": 25.0,
     "humidity": 80,
     "dew_point": 22.0,
     "sea_level_pressure": 1012.0,
     "cloud": 75,
     "wind_speed": 5.5
   }
   ```
   The response will be a JSON object with the prediction result.

## File Structure

```
.
├── main.py
├── requirements.txt
├── cloudburst_prediction_trained.sav
└── README.md
```

- `main.py`: The main application file containing the FastAPI app.
- `requirements.txt`: Lists the dependencies required for the project.
- `cloudburst_prediction_trained.sav`: The serialized trained model file.
- `README.md`: This README file.

## Troubleshooting

### Binary Compatibility Issue

If you encounter a binary compatibility issue similar to `ValueError: numpy.dtype size changed`, ensure you have the correct versions of numpy and scikit-learn installed as specified in the `requirements.txt`. Recreate the virtual environment if necessary.

### Steps to Recreate the Virtual Environment

1. **Remove the existing virtual environment**:
   ```bash
   rm -rf .venv
   ```

2. **Create a new virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss what you would like to change.
