import boto3

def insert_data(Items,table=None):
    table.put_item(Item=Items)
    print("inserting succeed")
