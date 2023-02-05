# data-pipeline-unit-test-example

## Introduction
...

### Why unit tests?
...

### What to test?
...

### Difference between notebooks and python modules (in regards to testing)
...

## Repo Structure

- /notebooks - All notebooks which acts like entrypoint for the buisness logic
- /my_package - All buisness logic in plain python modules/classes.
- /tests - All tests for `my_package`
    - The testing framework `pytests` looks for all python modules starting with `test_...`, hence the test files should be named `test_<module_to_test.py>`.
    - Tests are just normal python functions starting with the `test` prefix.

## Setup

    # Install virtualenv if not installed

    pip3 install virtualenv

    # Unix
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

    # Windows
    python3 -m venv venv
    .\env\Scripts\activate
    pip3 install -r requirements.txt


## Running the tests

*Java is required to run the tests locally due to pyspark*

    python3 -m pytest tests/

## Resources

- [pytest](https://docs.pytest.org/en/7.2.x/)
- [pytest-spark](https://github.com/malexer/pytest-spark)
    - This fixture allows for running pyspark/spark locally and get a fresh spark context for each test.
