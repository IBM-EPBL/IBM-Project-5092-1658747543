
from mailjet_rest import Client
import os

API_KEY = "222608684c590c76a082499702d4e21d"        # USERNAME
SECRET_KEY = "1a1e2806664c9775bc131029024094a2"     # PASSWORD

SENDER_EMAIL = "2019503059@smartinternz.com"
RECIPIENT_EMAIL = "pvs1135.3@gmail.com"
USERNAME = ""

mailjet = Client(auth=(API_KEY, SECRET_KEY), version='v3.1')
data = {
  'Messages': [
				{
						"From": {
								"Email": SENDER_EMAIL,
								"Name": "Team: PNT2022TMID35705"
						},
						"To": [
								{
										"Email": RECIPIENT_EMAIL,
										"Name": USERNAME
								}
						],
						"Subject": "My first Mailjet Email!",
						"TextPart": "Greetings from Mailjet!",
						"HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
				}
		]
}
# result = mailjet.send.create(data=data)
# print (result.status_code)
# print (result.json())

result1 = mailjet.message.get(id=288230391169235723)
print(result1)

