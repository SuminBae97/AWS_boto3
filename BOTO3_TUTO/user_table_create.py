import boto3



#creating table
def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
            TableName = 'users',
            KeySchema=[
                {
                    'AttributeName':'username',
                    'KeyType':'HASH'

                },
                {
                    'AttributeName': 'last_name',
                    'KeyType':'RANGE'
                }

            ],
            AttributeDefinitions=[
                {
                    'AttributeName':'username',
                    'AttributeType':'S'

                },
                {
                    'AttributeName':'last_name',
                    'AttributeType':'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':5,
                'WriteCapacityUnits':5
            }
    )
    return table


