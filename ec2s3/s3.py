from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver
#from credentials import *
import boto3
from datetime import datetime, timedelta


# init s3 resource and client .
s3_resource = boto3.resource('s3',
         aws_access_key_id='AKIAZEIYANLANJRHZJ72',
         aws_secret_access_key= '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')


# init s3 client .
s3_client = boto3.client('s3',
         aws_access_key_id='AKIAZEIYANLANJRHZJ72',
         aws_secret_access_key= '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')



# loop through s3 buckets and get bucket name
bucket_name = ""
bucket_object=""
s3_all= s3_resource.buckets.all()

for bucket in s3_all:
    print("\nAvailable Bucket is: ", bucket.name )
    bucket_name = bucket.name
   


# AccessPermissions
access_control_list = s3_client.get_bucket_acl(Bucket=bucket_name)
print("\nAccess Permissions List Are :\n")
for Permission in access_control_list:
	print(Permission)
    
# Public/Private
# METHOD 1
response = s3_client.get_public_access_block(Bucket=bucket_name)
if response['PublicAccessBlockConfiguration']['BlockPublicAcls'] and response['PublicAccessBlockConfiguration']['BlockPublicPolicy'] :
    print("Bucket Is Private")
else:
    print("Bucket Is Public")




#s3 = boto3.resource('s3')













'''
filename="personal-jw"

access_control_list_size = s3_client.get_object(Bucket=bucket_name ,key=filename )
print(access_control_list_size)
'''









# s3_connection = s3_resource
# bucket_obj = s3_connection.get_bucket(bucket_name)
# print(bucket_obj)

# s3 = boto.connect_s3()
# s3 = boto3.resource('s3')
# the_bucket = s3_resource.Bucket(bucket_name)
# bucket = s3_client.lookup(bucket_name)
# total_bytes = 0
# for key in the_bucket:
#            total_bytes += key.size
# print(total_bytes)
# print(dir(the_bucket))

# bucket_size = sum(obj['Size'] for obj in s3_client.list_objects(Bucket=bucket_name))#['Contents']
# print(bucket_size)

# response = client.list_objects(
#         Bucket=bucket_name,
#         # Marker='moe'
#     )
# for content in response['Contents']:
#     size = content['Size'] / 1024
#     print(str(size) + " KB")




# s3 = boto3.resource('s3')
# for my_bucket_object in my_bucket.objects.all():
#     print(my_bucket_object)




# bucket = s3_client.Bucket(bucket_name)
# size = sum(1 for _ in bucket.objects.all())
# print(size)

# response = s3_client.list_objects(Bucket=bucket_name)#['Contents']
# bucket_size = sum(obj['Size'] for obj in response)
# print(bucket_size)


########################################################################################################
# LIBCLOUD
# client = get_driver(Provider.S3)

# s3 = client(Access_key_ID, Secret_access_key)

# container = s3.get_container(container_name='personal-jw')

# objects = s3.list_container_objects(container)



# print(container)
# print(objects.list_objects)

# # print(dir(container))
# download_to = r"C:\Users\ahmed.mosaad\Desktop\py\automatedsys"
# # s3.download_object(objects, download_to)


# from libcloud.storage.types import Provider
# from libcloud.storage.providers import get_driver
# from my_credentials import *

# # Path to a very large file you want to upload
# FILE_PATH = r'C:\Users\Mos2d\Downloads\panda.jpg'

# cls = get_driver(Provider.S3)
# driver = cls(Access_key_ID, Secret_access_key)

# container = driver.get_container(container_name='my-image-12345')

# # This method blocks until all the parts have been uploaded.
# extra = {'content_type': 'application/octet-stream'}

# with open(FILE_PATH, 'rb') as iterator:
#     obj = driver.upload_object_via_stream(iterator=iterator,
#                                           container=container,
#                                           object_name='backup.jpg',
#                                           extra=extra)