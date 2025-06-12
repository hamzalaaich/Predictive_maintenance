# Predictive Maintenance API

## Overview

A FastAPI-based API for predicting Remaining Useful Life (RUL) in predictive maintenance applications using a trained Random Forest model.

## Features

- **Single Prediction Endpoint**: `/predict`
- **Batch Prediction Endpoint**: `/batch_predict`
- **Input Validation and Error Handling**
- **Logging for Monitoring and Debugging**
- **Interactive API Documentation**

## Setup Instructions

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/predictive-maintenance.git
    cd predictive-maintenance
    ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # or
    venv\Scripts\activate     # On Windows
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```



5. **Run the API**:
in the root of the project run : 

    ```bash
    uvicorn src.api:app --reload
    ```

6. **Access the API Documentation**:

    - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

7. **Run  the Web service for RUL prediction**:    
first go inside the src folder : 
      ```bash
       cd src 
      ```
then launch the web service ( make sure the api is up and running before : )

    ```
     streamlit UI.py
    ```
 
## Usage

### Single Prediction

- **Endpoint**: `/predict`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
  - `access_token: your-secure-api-key`
- **Body**:

    ```json
    {
      "feature1": 0.5,
      "feature2": 1.2,
      "feature3": 3.4
    }
    ```

- **Response**:

    ```json
    {
      "predicted_rul": 15.2
    }
    ```

### Batch Prediction

- **Endpoint**: `/batch_predict`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
  - `access_token: your-secure-api-key`
- **Body**:

    ```json
    {
      "data": [
        {
          "feature1": 0.5,
          "feature2": 1.2,
          "feature3": 3.4
        },
        {
          "feature1": 0.6,
          "feature2": 1.3,
          "feature3": 3.5
        }
      ]
    }
    ```

- **Response**:

    ```json
    {
      "predictions": [15.2, 23.5]
    }
    ```

## Deployment

Refer to the [Deploying the API](#7-deploying-the-api) section in the previous guide for detailed deployment instructions using Uvicorn, Docker, and various cloud platforms.

## Testing

Run automated tests using `pytest`:

```bash
pytest
