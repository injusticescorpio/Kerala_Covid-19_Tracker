# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from .covid19 import Covid_19
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# first action
class ActionFirst(Action):

    def name(self) -> Text:
        return "action_show_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        district = tracker.get_slot("district")
        reply = tracker.get_slot("reply")
        details = Covid_19(str(district))
        print('hai')
        print(details.covid_19_details_total())
        dispatcher.utter_message(text=details.covid_19_details_total())

        return []
#Second action
class ActionSecond(Action):

    def name(self) -> Text:
        return "action_total_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        district = tracker.get_slot("district")
        reply = tracker.get_slot("reply")
        details = Covid_19(str(district))
        print('REPLY='+reply.lower())
        print(reply.lower() =='no')
        if reply.lower() =='no':
            dispatcher.utter_message(text="Okey very well")

        else:
            dispatcher.utter_message(text=details.total_covid_19())


        return []

#third action

class ActionThird(Action):

    def name(self) -> Text:
        return "action_short_show_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        district=tracker.get_slot("district")
        reply=tracker.get_slot("reply")
        details = Covid_19(str(district))
        dispatcher.utter_message(text=details.covid_19_details_total())


        return []

class ActionFourth(Action):

    def name(self) -> Text:
        return "action_respond_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        district=tracker.get_slot("district")
        reply=tracker.get_slot("reply")
        details =Covid_19(str(district))
        dispatcher.utter_message(text=details.total_covid_19())

        return []
