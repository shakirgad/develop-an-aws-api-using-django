import boto3 



#using client object     
class AWS_EC2:
    def connect_ec2():
        #Instances information
        #using client object  
        Myec2_cli=boto3.client('ec2')
        response_cli=Myec2_cli.describe_instances()
        Reservations = response_cli['Reservations'] 
        ResponseMetadata = response_cli['ResponseMetadata']
        return Reservations, ResponseMetadata

'''  
#using client object to print Instances info if EC2 instances created   
        for each in response_cli ['Reservations']:
            for instance in each['Instances']:
                ins_type = instance['InstancesType']
                ins_state = instance['State']['Name']
                sec_group=instance['SecurityGroup'][0]['GroupId']
                return (ins_type , ins_state , sec_group)
                #print(instance['InstancesType'],instance['State']['Name'],instance['SecurityGroup'][0]['GroupId])
        '''