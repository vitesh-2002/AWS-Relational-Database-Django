import json
import os
import psycopg2
import twilio
import datetime
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    connection = psycopg2.connect(user = os.environ['USER'],
                                  password = os.environ['PASS'],
                                  host = os.environ['HOST'],
                                  database = os.environ['NAME'],
                                  port = "5432")
    cursor = connection.cursor()

    insert_query = "INSERT INTO book(book_title, book_isbn, pages) VALUES('Principles', 1118, 80)"

    print('The Query was: ')
    print(insert_query)
    cursor.execute(insert_query)
    connection.commit()
    #print("Name is " + os.environ['NAME'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
