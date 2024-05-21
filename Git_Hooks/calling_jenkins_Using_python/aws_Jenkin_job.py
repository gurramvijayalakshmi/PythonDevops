"""this module will have codeto call Jenkins job
"""

import os
import requests

JENKINS_URL = os.getenv("JENKINS_URL","https://13.123.234.345:8080") 
# https://13.123.234.345:8080  this is an dummy value

JENKINS_JOB = os.getenv("JENKINS_JOB","Deploy_app")
#Deploy_app is dummy name we have to specify the jenkin job name we used 

JENKINS_TOKEN = os.getenv ("JENKINS_TOKEN", "jdhalfjjvdfgyrfjjfjnbvavhajjfhgh")
#jdhalfjjvdfgyrfjjfjnbvavhajjfhgh is an dummy token we have generate the token in the jenkins job 

JENKINS_USER = os.getenv("JENKINS_USER","pythonDevops")
#pythonDevops is an dummy user name
 
def trigger_jenkins_job():
    """ This function will trigger jenkins job
    """
    job_url = f"{JENKINS_URL}/job/{JENKINS_JOB}/build"
    response = requests.post(job_url,auth= (JENKINS_USER,JENKINS_TOKEN), timeout= 30)

    if response.status_code == 201:
        print("Jenkins job is triggered successfully")
    else :
        print(f"Failed to trigger Jenkins job {response.txt}")

def get_last_build_number():
    """This function will get the last build number"""
    job_url = f"{JENKINS_URL}/job/{JENKINS_JOB}/lastBuild/api/json"
    response = requests.get(job_url, auth=(JENKINS_USER, JENKINS_TOKEN), timeout=30)
    if response.status_code == 200:
        return response.json()["number"]
    else:
        print(f"Failed to get last build number {response.text}")

def get_build_status(build_number):
    """This function will get the build status"""
    job_url = f"{JENKINS_URL}/job/{JENKINS_JOB}/{build_number}/api/json"
    response = requests.get(job_url, auth=(JENKINS_USER, JENKINS_TOKEN), timeout=30)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print(f"Failed to get build status {response.text}")


if __name__ == "__main__":
    trigger_jenkins_job()
    time.sleep(10)
    build_id = get_last_build_number()
    status = get_build_status(build_id)
    print(f"build id: {build_id} build_status: {status}")
         