import json
import datetime

def checkInformation(event, context):
    # Extract registration information from event
    registration_info = event['registration_info']

    # Check that all required fields are present
    required_fields = ['child', 'parents', 'daysOfWeek']
    for field in required_fields:
        if field not in registration_info:
            return {
                'statusCode': 400,
                'body': f'Missing required field: {field}'
            }

    # If all checks pass, return a success response
    return {
        'statusCode': 200,
        'body': json.dumps(registration_info)
    }





def checkAgeRange(event, context):
    # Parse the registration_info from the previous function's output
    registration_info = json.loads(event['body'])

    dob = registration_info['child']['dateOfBirth']

    # Calculate child's age
    today = datetime.date.today()
    dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

    # Check that child's age is within acceptable range (e.g., 2-5 years)
    if age < 2 or age > 5:
        return {
            'statusCode': 400,
            'body': json.dumps('Child is not within the acceptable age range for this daycare.')
        }

    # Include the age in the response for potential use in subsequent functions
    registration_info['child']['age'] = age

    # If all checks pass, return the updated registration_info
    return {
        'statusCode': 200,
        'body': json.dumps(registration_info)
    }


def checkSpotsAvailability(event, context):
    # Parse the registration_info from the previous function's output
    registration_info = json.loads(event['body'])

    # Placeholder for actual availability check logic
    spots_available = 20  # This should be dynamically determined, not hardcoded

    if spots_available <= 0:
        return {
            'statusCode': 400,
            'body': json.dumps('No spots available in the daycare.')
        }

    # If spots are available, return the registration_info without changes
    return {
        'statusCode': 200,
        'body': json.dumps(registration_info)
    }


import json

def checkInformation(event, context):
    # Extract registration information from event
    registration_info = event['registration_info']

    # Check that all required fields are present
    required_fields = ['child', 'parents', 'daysOfWeek']
    for field in required_fields:
        if field not in registration_info:
            return {
                'statusCode': 400,
                'body': f'Missing required field: {field}'
            }

    # If all checks pass, return a success response
    return {
        'statusCode': 200,
        'body': json.dumps(registration_info)
    }