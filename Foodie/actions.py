from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage



class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'Mexican':73,'italian':55,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		print(response)
		dispatcher.utter_message("-----"+response)
		return [SlotSet('address',response)]

# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		to_email = tracker.get_slot('email')
		email_body = tracker.get_slot('email_body')
		from_email = ''
		pwd = ''       
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls()
		s.login('from_email', 'pass')
		msg = EmailMessage()
		msg['From'] = from_email
		msg['To'] =to_email
		msg['Subject'] = "Details of TOP 10 Resturants \n \n"
		msg.set_content(email_body)

		try:
			s.sendmail(from_email, strip(str(to_email)), message)
			s.quit()
		except:
			dispatcher.utter_message(email)		
		return []


# Tier 1 and Tier 2 cities
cities_t1_t2 = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer','Aligarh','Amravati','Amritsar',
'Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bilaspur','Bokaro Steel City','Chandigarh',
'Coimbatore','Cuttack','Dehradun','Dhanbad','Bhilai','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
'Gwalior','Gurgaon','Guwahati','Hamirpur','Hubli–Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur','Jhansi',
'Jodhpur','Kakinada','Kannur','Kanpur','Kochi','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow','Madurai','Malappuram','Mathura',
'Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida','Patna','Pondicherry','Purulia Prayagraj','Raipur',
'Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Shimla','Siliguri','Solapur','Srinagar','Surat','Thiruvananthapuram','Thrissur',
'Tiruchirappalli','Tiruppur','Ujjain','Bijapur','Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Vellore', 'Warangal']
cities_t1_t2 = [city.lower() for city in cities_t1_t2]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_search_restaurants'
	
	def run(self, dispatcher, tracker, domain):
		city = tracker.get_slot('location')
		city = strip(str(city))
		if city.lower() in cities_t1_t2:
			return [SlotSet('location_check',"one")]
		else:
			return [SlotSet('location_check',"zero")]
			


