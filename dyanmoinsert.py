import boto3

#AKIAX6LH5R6T6JNLAS6D
#V3qiRBXnuX3B2bWC3GWbqCbyEp9/gFYS2DKldvIg
dynamodb=boto3.resource('dynamodb',aws_access_key_id='AKIAX6LH5R6T6JNLAS6D',aws_secret_access_key='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',region_name='us-east-2')
dyanmoTB=dynamodb.Table('wonhoMessages')
#the last entry number is count
count=158;
i=0
msglist=["So the girl you saw before is pretty? Is she better than me? Good, you deserve her"]

print (len(msglist))
for i in range(len(msglist)):
         
    count=count+1   
    dyanmoTB.put_item(
        Item={
            'count':count,
            'msg':msglist[i]
            }
        
    )
