def my_cron_job():
    endpoint='127.0.0.1:8000/dashboard/'
    url="google.com"
    email="emai@mail.com"
    get_response=requests.post(endpoint,json={"site_url":url,"email":email})
    return get_response.text
    