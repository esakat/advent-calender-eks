import boto3
import uuid
import os
import time
 
queue_name = os.environ['QUEUE_NAME']
action_type = os.environ['ACTION_TYPE']
sqs = boto3.resource('sqs', endpoint_url='https://sqs.ap-northeast-1.amazonaws.com', region_name="ap-northeast-1")
queue = sqs.get_queue_by_name(QueueName=queue_name)

if action_type == 'push':
  while True:
    msg_list = [{'Id' : '{}'.format(uuid.uuid4()), 'MessageBody' : 'msg_{}'.format(uuid.uuid4())} for i in range(10)]
    response = queue.send_messages(Entries=msg_list)

if action_type == 'pop':
  while True:
      msg_list = queue.receive_messages(MaxNumberOfMessages=10)
      if msg_list:
          for message in msg_list:
              print(message.body)
              message.delete()
      else:
          print('queue is empty!!')
          time.sleep(5)