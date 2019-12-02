#!/bin/bash

while true
do
  POD_NUM=$(kubectl get deployment php-apache -ojson | jq .status.availableReplicas)
  #POD_NUM=$(kubectl get deployment sqs-app-pop -ojson | jq .status.availableReplicas)
  aws cloudwatch put-metric-data --metric-name sqs-app-pop-pod-nums --namespace "eks-sample" --value $POD_NUM 
  sleep 5
done