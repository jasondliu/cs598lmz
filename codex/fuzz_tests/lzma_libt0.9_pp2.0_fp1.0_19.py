import lzma
lzma.decompress(message['Payload'].read()).decode('utf-8')

with open("string.cpio", "w") as f:
    f.write(lzma.decompress(message['Payload'].read()).decode('utf-8'))

cpio = cpiofile.CpioFile("string.cpio")
cpio.get_data('etc/test.conf')

s3_client.delete_message(QueueUrl=url, ReceiptHandle=message['Messages'][0]['ReceiptHandle'])
bucket.upload_file('string.cpio', 'cpiofile.cpio')
s3_client.send_message(QueueUrl=url, MessageBody=json.dumps({'Bucket': 'mahou-bucket', 'Key': 'cpiofile.cpio'}))

response = s3_client.receive_message(QueueUrl=url, 
