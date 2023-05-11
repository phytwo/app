import json
from quando import handler

def test_handler():
    # Test with valid input
    valid_input = {"country_code": "US"}
    expected_output = "The current time in US capital is:"
    response = handler(valid_input, None)
    assert response["statusCode"] == 200
    assert expected_output in response["body"]
    
    # Test with invalid input
    invalid_input = {"country_code": "XX"}
    response = handler(invalid_input, None)
    assert response["statusCode"] == 400
    assert "Invalid input" in response["body"]

    # Test with no input
    response = handler(None, None)
    assert response["statusCode"] == 400
    assert "Invalid input" in response["body"]
