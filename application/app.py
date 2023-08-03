from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client['balasai']
collection = db['data']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    job_role = request.form.get('job_role')
    address = request.form.get('address')
    city = request.form.get('city')
    pincode = request.form.get('pincode')
    date = request.form.get('date')
    upload = request.form.get('upload')

    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'job_role': job_role,
        'address': address,
        'city': city,
        'pincode': pincode,
        'date': date,
        'upload': upload
    }
    collection.insert_one(user)
    return render_template('result.html', first_name=first_name, last_name=last_name, email=email, job_role=job_role,
                           address=address, city=city, pincode=pincode, date=date, upload=upload)

@app.route('/form_submit', methods=["POST"])
def ok():
    if request.method=='POST':
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        job_role=request.form.get('job_role')
        address=request.form.get('address')
        city=request.form.get('city')
        pincode=request.form.get('pincode')
        date=request.form.get('date')
        upload=request.form.get('upload')

        user={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'job_role':job_role,
            'address':address,
            'city':city,
            'pincode':pincode,
            'date':date,
            'upload':upload
        }
        collection.insert_one(user)
        return render_template("last.html")

if __name__ == '__main__':
    app.run(debug=True)