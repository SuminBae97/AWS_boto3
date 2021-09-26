from pprint import pprint
import boto3

def put_movie(title,year,plot,rating,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table("Movies")
    response = table.put_item(
        Item={
            'year':year,
            'title':title,
            'info':{
                'plot':plot,
                'rating':rating
            }
        }
    )

    return response

if __name__=="__main__":
    movie_resp = put_movie("the avengers",2019,"avengers assemble",10)
    print("put movie succeeded:")
    pprint(movie_resp)