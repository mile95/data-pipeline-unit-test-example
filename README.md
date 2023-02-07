## Introduction

Example of how to achieve unit testing in data pipeline projects.

### Why unit tests?

- Team responsibility. Do we deliver what we say we do?
    - If something breaks in production, it is not one individual fault. It is the teams' processes that are broken.
- Confidence. Do I dare to perform changes?
- A safety net.

### What to test?

- Don't test everything!
- Test the business logic
    - Example; Transformation logic. Does the transformed data look like I expected given the raw data?
- Ignore stuff like writing/reading from databases initially.

### Difference between notebooks and python modules (in regards to testing)

To achieve the normal workflow with unit testing in a project highly dependent on notebooks, some thoughts about the code structure are required.
The code that needs to be tested should not live in notebooks, it should live in plain python modules.

I recommend thinking of notebooks as the entrypoint (main method) to the business logic.

**Example:** Assume that you need to transform some data.
This action can be simplified into three steps:

1. Read raw data from the database
2. Transform data
3. Write transformed data to the database

The action to test in this scenario is action #2 (Transform Data), this is where most of the business logic will exist.

I suggest that the code distribution between plain python modules and notebooks in this example looks like this:

1. Read raw data from the database (notebook)
2. Transform data (python module)
3. Write transformed to the database (notebook))

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
