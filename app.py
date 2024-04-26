import requests
from flask import Flask , jsonify, request



app = Flask(__name__)

@app.route('/iiyiu/check_email/email=<email>', methods=['GET'])
def check(email):
	def insta(email):
		if "@" in email:
			email=email.split("@")[0]
		email=f"{email}@gmail.com"
		response=requests.get(f"https://check-instagram-5574ad333942.herokuapp.com/check_email/{email}").json()
		if "html" in response:
			gmail(email)
		else:
			print({"by":"@iiyiu","message":"unAvailble","status":"bad"})
	
	def gmail(email):
		req=requests.get(f"https://api-check-gmail-db235a1a3749.herokuapp.com/check_email/email={email}").json()['status']
		if 'good' in req:
			print({"by":"@iiyiu","message":"Available In insta and Gmail","status":"good"})
		else:
			print({"by":"@iiyiu","message":"unAvailble","status":"bad"})
	insta(email)

if __name__ == '__main__':
	app.run(debug=True)
