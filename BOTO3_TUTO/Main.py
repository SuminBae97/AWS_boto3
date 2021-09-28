import boto3
from aws_boto3.BOTO3_TUTO import user_table_create as ct
from aws_boto3.BOTO3_TUTO import insert_item as it
from pprint import pprint

dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:8000")
db = boto3.client("dynamodb",endpoint_url="http://localhost:8000")


if __name__=="__main__":
    table_list = db.list_tables()
    print(table_list)

    #creatingn table
    #user_table = ct.create_table()
    #print("user table created",user_table.table_status)

    #calling table
    user_table = dynamodb.Table("users")
    pprint(user_table.creation_date_time)

    Items = {'account_type': 'standard_user',
        'username': 'johndoe',
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 25,
        'address': {
            'road': '1 Jefferson Street',
            'city': 'Los Angeles',
            'state': 'CA',
            'zipcode': 90001
        }

            }

    #it.insert_data(Items,user_table)

    response = user_table.scan()


    for people in response['Items']:
        pprint(people)



