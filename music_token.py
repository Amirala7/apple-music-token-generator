# requires pyjwt (https://pyjwt.readthedocs.io/en/latest/)
# pip install pyjwt


import datetime
import jwt


alg = 'ES256'







if __name__ == "__main__":
	print("Enter you Private Key obtained from your developer account, without begin and end tags")
	secret = input()
	print("\nEnter your Key Id, available in your developer account under the key name")
	keyId = input()
	print("\nEnter your Apple development team Id")
	teamId = input()
	print("\nEnter the validity duration of the token in hours :")
	hours = int(input())

	
	time_now = datetime.datetime.now()
	time_expired = datetime.datetime.now() + datetime.timedelta(hours=hours)

	headers = {
	"alg": alg,
	"kid": keyId
	}

	payload = {
	"iss": teamId,
	"exp": int(time_expired.strftime("%s")),
	"iat": int(time_now.strftime("%s"))
	}

	"""Create an auth token"""
	token = jwt.encode(payload, secret, algorithm=alg, headers=headers)

	print ("----TOKEN----")
	print (token)

	print ("----CURL----")
	print( "curl -v -H 'Authorization: Bearer %s' \"https://api.music.apple.com/v1/catalog/us/artists/36954\" " % (token))

