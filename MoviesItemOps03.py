import boto3
from pprint import pprint
from decimal import Decimal
from botocore.exceptions import  ClientError
from aws_boto3 import MoviesItemOps02
from aws_boto3 import MoviesItemsOps01


def increase_rating(title,year,rating_increase,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table("Movies")
    response = table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression = "set info.rating = info.rating+:val",
        ExpressionAttributeValues={
            ':val':Decimal(rating_increase)
        },
        ReturnValues = "UPDATED_NEW"
    )
    return response


def remove_actors(title,year,actor_count,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table("Movies")
    try:
        response = table.update_item(
            Key={
                'year':year,
                'title':title
            },
            UpdateExpression = "remove info.actors[0]",
            ConditionExpression = "size(info.actors)>num",
            ExpressionAttributeValues = {'num':actor_count},
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])

        else:
            return False
    else:
        return response


def delete_underrated_movie(title,year,rating,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table("Movies")
    response = table.delete_item(
        Key={
            'year':year,
            'title':title
        },
        ConditionExpression = "info.rating <= :val",
        ExpressionAttributeValues = {
            ":val":Decimal(rating)

        }
    )

    return response





def update_movie(title,year,rating,plot,actors,genre,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table("Movies")
    response = table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression="set info.rating=:r , info.plot=:p, info.actors=:a , info.genres=:g",
        ExpressionAttributeValues={
            ':r':Decimal(rating),
            ':p':plot,
            ':a':actors,
            ':g':genre
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__=="__main__":
    # update_response = update_movie("the avengers",2019,5.5,"Lets role",['chris','scarlett'],['action','comic'])
    # print("movie updated")
    # pprint(update_response)
    # update_response = increase_rating("the avengers",2019,3)
    # print("rating updated")
    # pprint(update_response)

    # movie = MoviesItemOps02.get_movie('the avengers', 2019)
    # print("Attempting conditional update (expecting failure)...")
    # update_response = remove_actors("the avengers", 2019, 3)
    # if update_response:
    #     print("Update movie succeeded:")
    #     pprint(update_response)
    #
    # print(movie)
    movie_resp = MoviesItemsOps01.put_movie("the avengers",2019,"avengers assemble",10)
    print("put movie succeeded:")
    pprint(movie_resp)

    print("Deleting underrated movies")
    delete_response = delete_underrated_movie("the avengers",2019,10)
    if delete_response:
        print("succeded deleting")
        pprint(delete_response)


