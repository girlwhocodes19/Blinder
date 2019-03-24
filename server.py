# FLASK code goes here
from flask import Flask, render_template, request
import os
import urllib3, requests, json


app = Flask(__name__)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

wml_credentials={
"url": "https://us-south.ml.cloud.ibm.com",
"username": "32212487-8cb9-4ebd-812f-b861b557f651",
"password": "78c55dda-1d80-40fb-b7d8-fe5ae72e3488"
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
url = '{}/v3/identity/token'.format(wml_credentials['url'])
response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

@app.route("/")
@app.route('/index')
def index():
    user = {'usernames': 'Insert Username Here' }
    return render_template('index.html', title = 'Home', user=user)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        form = request.form
        # print("/////")
        # print(request)
        # print("???????")
        # print("???")
        # print(form["Name"])
        # print(form)
        # user = form["user"]
        # age = form["age"]
        # language = form["language"]
        # dialect = form["dialect"]
        # proficiency_level = form["proficiency level"]
        # language_to_learn = form["language to learn"]
        # dialect_to_learn = form["dialect to learn"]
        # proficiency_level_so_far = form["proficiency level so far"]
        # country = form["country"]
        # occupation = form["occupation"]
        # interests = form["interests"]
        users = payload_scoring (form)
        # user = {'usernames': user}
        return render_template("results.html", title='Home', users=users)


def payload_scoring (formdata):
    #resultarray = '[{"Name":"Bob", "Percent of Match": "7%"},{"Name":"Bobby", "Percent of Match": "9%"}]'
    #NOTE: manually define and pass the array(s) of values to be scored in the next line
    #payload_scoring = {"fields": ["name", "age", "language", "dialect", "proficiency level", "language to learn", "dialect to learn", "proficiency level so far", "country", "occupation", "interests"], "values": formdata}
    payload_scoring = {"fields": ["user", "age", "language", "dialect", "proficiency level", "language to learn", "dialect to learn", "proficiency level so far", "country", "occupation", "interests"], "values": formdata}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/3b5682e2-bd59-4db8-a018-6bfc1d4a624e/deployments/bbddb035-ea0e-4e01-81f9-aa7f95fb9322/online', json=payload_scoring, headers=header)
    print("Scoring response")
    print(response)
    print(json.loads(response_scoring.text))
    return json.loads(response_scoring.text)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)


