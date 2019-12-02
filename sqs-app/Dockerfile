FROM python:3.7
RUN pip install --upgrade pip
RUN pip install boto3
COPY sqs-poppush.py .
CMD python sqs-poppush.py