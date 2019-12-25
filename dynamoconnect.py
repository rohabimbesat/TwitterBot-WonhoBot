import boto3
from random import randint
#AKIAX6LH5R6T6JNLAS6D
#V3qiRBXnuX3B2bWC3GWbqCbyEp9/gFYS2DKldvIg

def dynamoget():
    dynamodb=boto3.resource('dynamodb',aws_access_key_id='AKIAX6LH5R6T6JNLAS6D',aws_secret_access_key='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',region_name='us-east-2')
    dynamoTB=dynamodb.Table('wonhoMessages')
    maxcount=dynamoTB.item_count -1
    random_num=randint(0, maxcount)
    #print(random_num)
    items = dynamoTB.get_item(Key={"count": random_num})
    #print(items)
    message="empty"
    for x in items.values():
        message=x['msg']
        break;
   # print(message)
    return message


#dynamoget()

