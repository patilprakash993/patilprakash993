## Happy path1
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese","price": "300"}
	- action_search_restaurants
* affirm
    - utter_goodbye
    - export
	
## Happy path2
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
* affirm
    - utter_goodbye
    - export


## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
* affirm
    - utter_goodbye
    - export
	
## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "300"}
	- slot{"price": "399"}
	- action_search_restaurants
	- slot {"address":"No result found"}
    
