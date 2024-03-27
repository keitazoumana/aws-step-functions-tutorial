# Mastering AWS Step Functions: A Comprehensive Guide for Beginners

Welcome to the comprehensive guide for beginners on mastering AWS Step Functions. This guide provides a step-by-step approach to using AWS Step Functions, integrating them with AWS Lambda to build scalable and efficient serverless workflows.

## Overview

AWS Step Functions allow you to coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using AWS Lambda, you can run code without provisioning or managing servers. Together, they enable you to create robust and extendable applications.

This guide uses an example of a daycare registration system to illustrate how to set up a workflow using AWS Step Functions. It includes checks for registration information, age range validation, and spots availability, culminating in the confirmation of registration.

## Repository Structure

The repository consists of two main files:

- `LambdaFunctions/LambdaFunctions.py`: This Python script contains all the AWS Lambda functions that are invoked by the step functions. Each function is designed to perform a specific task in the workflow, such as validating registration information, checking the age range, and confirming registration.

- `state_language_code.json`: This file contains the Amazon States Language definition of the step function workflow. It outlines the states and transitions based on the outcome of the Lambda functions.

## Workflow Diagram

The workflow for the daycare registration system is depicted in an image attached to this guide. It showcases the sequence of steps involved in the registration process:

![Alt text](/images/stepfunctions_graph.png "States Machine")


1. **Check Information**: Validates that all necessary information is present in the registration.
2. **Check Age Range**: Ensures that the child's age is within the acceptable range for the daycare.
3. **Check Spots Availability**: Checks if there are open spots available in the daycare.
4. **Confirm Registration**: Finalizes the registration process and calculates fees.

Each step in the workflow diagram corresponds to a Lambda function that either transitions to the next step upon success or handles errors accordingly.

## Getting Started

To get started with this guide:

1. Review the `LambdaFunctions.py` to understand the individual functions and how they process the data.
2. Examine the `state_language_code.json` to see how the states are defined and how they interact with the Lambda functions.
3. Upload the Lambda functions to AWS Lambda.
4. Create a Step Function in the AWS Management Console and define the workflow using the content of `state_language_code.json`.
5. Execute the Step Function with a valid input JSON to test the workflow.

## Prerequisites

Before you begin, ensure you have the following:

- An AWS account with necessary permissions to create Lambda functions and Step Functions.
- Basic understanding of Python programming language.
- Familiarity with AWS Lambda and AWS Step Functions.

## Input Format

### Failure Case
A sample input JSON is provided to illustrate the format expected by the workflow:

```json
{
  "registration_info": {
    "child": {
      "firstName": "Mohamed",
      "lastName": "Diallo",
      "dateOfBirth": "2016-07-01"
    },
    "parents": {
      "mother": {
        "firstName": "Aicha",
        "lastName": "Cisse",
        "email": "aicha.cisse@example.com",
        "phone": "123-456-7890"
      },
      "father": {
        "firstName": "Ibrahim",
        "lastName": "Diallo",
        "email": "ibrahim.diallo@example.com",
        "phone": "098-765-4321"
      }
    },
    "daysOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "specialInstructions": "Mohamed has a peanut allergy."
  }
}
```
![Alt text](/images/failure_case.png "Failure Scenario")


### Success Case
```json
{
  "registration_info": {
    "child": {
      "firstName": "Mohamed",
      "lastName": "Diallo",
      "dateOfBirth": "2021-03-27"
    },
    "parents": {
      "mother": {
        "firstName": "Aicha",
        "lastName": "Cisse",
        "email": "aicha.cisse@example.com",
        "phone": "123-456-7890"
      },
      "father": {
        "firstName": "Ibrahim",
        "lastName": "Diallo",
        "email": "ibrahim.diallo@example.com",
        "phone": "098-765-4321"
      }
    },
    "daysOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "specialInstructions": "Mohamed has a peanut allergy."
  }
}
```
![Alt text](/images/success_case.png "Success Scenario")
