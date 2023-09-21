from flask import Flask, render_template,jsonify
app = Flask(__name__) #if the python code is run deirectly then in that case __name__ = __main__
JOBS = [
    {
        'id' : 1,
        'title' : "Data Analyst",
        'location' : 'Nashik Bharat',
        'salary' : 'Rs. 10,00,000'
    },
    {
        'id' : 2,
        'title': "Frontend Engineer",
        'location' : 'Nashik Bharat',
        'salary' : 'Rs. 15,00,000',
    },
    {
        'id' : 3,
        'title': 'data scientist',
        'location' : 'Remote',
       
    }
    
]
@app.route('/')
def hello_world():
   return render_template('home.html', jobs = JOBS, company_name='SSC.coporates') #passing the job dictionary as arguement


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)  #info is returned as JSON 





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)