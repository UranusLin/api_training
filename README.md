# FastAPI Predict API

This project implements a FastAPI-based prediction API with input validation, error handling, and logging.

## Project Structure

```
project_root/
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── router.py
│   ├── controller.py
│   └── service.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_service.py
│   └── test_controller.py
├── .flake8
├── requirements.txt
└── README.md
```

## Features

- Input validation for customer number and date
- Mock prediction processing
- Error handling and logging
- Follows FastAPI best practices with separate router, controller, and service layers

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:
   ```
   uvicorn api.main:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8000`

3. You can access the automatic interactive API documentation at `http://127.0.0.1:8000/docs`

## API Endpoints

### POST /predict/v1

Accepts a JSON payload with the following structure:

```json
{
    "business_unit": "C170",
    "request_id": "C170-20220107-094050-0001",
    "inputs": {
        "cust_no": "176ZpUZczEtk29&9+w1Fgw==",
        "date": "2022-01-07 09:40:50"
    }
}
```

Returns a prediction result with status code, active product count, and average number.

## Running Tests

To run the tests, use the following command:

```
pytest tests
```

## Code Style

This project uses flake8 for code style checking. To run flake8:

```
flake8 .
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.