# Flask Number Analysis API

This is a simple Flask application that provides an API to analyze numbers. It checks if a given number is an Armstrong number and a palindrome.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the `app.py` file to your local machine.

2. Navigate to the directory containing the `app.py` file.

3. Install Flask using pip:

    ```bash
    pip install Flask
    ```

## Running the Application

1. Open a terminal or command prompt.

2. Navigate to the directory where your `app.py` file is located.

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. You should see output indicating the Flask development server is running. By default, it will run on `http://127.0.0.1:5000/`.

## Using the API

### Welcome Endpoint

- **URL:** `/`
- **Method:** GET
- **Description:** Returns a welcome message.

Example:

```plaintext
http://127.0.0.1:5000/
```

Response
```bash
My First API
```

Analyze Number Endpoint
- **URL:** `/analyze_number/<int:n>`
- **Method:** GET
- **Description:** Analyzes the given number to check if it is an Armstrong number and a palindrome.

Example:
```bash
http://127.0.0.1:5000/analyze_number/153
```

Response:
```bash
{
  "number": 153,
  "armstrong": true,
  "palindrome": false
}
```