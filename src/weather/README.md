# Project Name

## Description

This project is a Python AWS Lambda function that takes a 2-letter country code and provides the time in that country's capital.

## Usage

To use the function, you will need to invoke it with a 2-letter country code as input.

1. Deploy the Lambda function to AWS by uploading the script file as a zip file using the AWS Management Console or AWS CLI.
2. Invoke the function using the AWS CLI or through the AWS Management Console by passing a JSON payload containing the `country_code` value as follows:

```json
{
  "country_code": "US"
}
```

This will invoke the function in AWS and return the current time in the country's capital.

## Testing
To test the project, run the pytest command in the project directory to run the tests:

```bash
pytest
```
This will run the test_handler() function and output the results to the terminal.




