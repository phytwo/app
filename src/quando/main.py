import datetime
import pytz
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def handler(event, context):
    logger.debug(f"Received event: {json.dumps(event)}")
    
    try:
        if 'country_code' in event:
            # Get the country code from the input event
            country_code = event['country_code']

            # Get the timezone of the country's capital using the pytz library
            capital_timezone = pytz.country_timezones[country_code][0]
            logger.info(f"Successfully retrieved timezone {capital_timezone} for country code {country_code}")

            # Get the current time in the country's capital timezone using the datetime library
            current_time = datetime.datetime.now(pytz.timezone(capital_timezone))

            # Format the current time as a string
            time_str = current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

            # Return the current time as a response
            response = {
                'statusCode': 200,
                'body': json.dumps({'message': f'The current time in {country_code} capital is: {time_str}'})
            }
            logger.info(f"Successfully returned response: {response}")
        else:
            # Return missing country code message
            response = {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing country_code parameter in query string'})
            }
            logger.error(f"Failed to retrieve country_code parameter from query string: {json.dumps(event)}")
    except Exception as e:
        # Something unexpected has happened
        response = {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error: {str(e)}'})
        }
        logger.error(f"An error occurred: {str(e)}")

    return response
