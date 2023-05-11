import os
import json
from unittest.mock import patch
from weather import handler

def test_handler():
    # Test with valid input
    event = {'country_code': 'US'}
    response = handler(event, {})
    data = json.loads(response['body'])
    assert response['statusCode'] == 200
    assert data['weather_description']
    assert data['temperature']

    # Test with invalid input
    event = {'country_code': 'XX'}
    response = handler(event, {})
    data = json.loads(response['body'])
    assert response['statusCode'] == 400
    assert data['message'] == 'Invalid input'

    # Test with missing input
    event = {}
    response = handler(event, {})
    data = json.loads(response['body'])
    assert response['statusCode'] == 400
    assert data['message'] == 'Invalid input'
