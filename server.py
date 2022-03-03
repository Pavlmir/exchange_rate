import random

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

import xml.etree.ElementTree as ET
import service_pb2, service_twirp
import requests

URL = "http://www.cbr.ru/scripts/XML_daily.asp"
    

class DollarRate(object):
    async def GetDollarRate(self, context, empty):
        # sending get request and saving the response as response object
        dollar_req = requests.get(url = URL)
        if dollar_req.status_code == 200:
            courses = ET.fromstring(dollar_req.text)
            dollar_course = courses.find("Valute[@ID='R01235']").find('Value').text.replace(',', '.')
        else:
            dollar_course = 0
            
        return service_pb2.Dollar(
            value=float(dollar_course)
        )


service = service_twirp.DollarRateServer(service=DollarRate())
app = TwirpASGIApp()
app.add_service(service)