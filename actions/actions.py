# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("I am Rasa built health chatbot")
#         dispatcher.utter_message(text="Hello World!")

#         return []
    
    
from datetime import datetime, timedelta
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmAppointment(Action):

    def name(self):
        return "action_confirm_appointment"

    def run(self, dispatcher, tracker, domain):
        date = tracker.get_slot("appointment_date")
        time = tracker.get_slot("appointment_time")
        name = tracker.get_slot("name")

        dispatcher.utter_message(
            text=f"✅ Appointment confirmed!\n👤 Name: {name}\n📅 Date: {date}\n⏰ Time: {time}"
        )
        return []


import openai
openai.api_key = "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"

class ActionOpenAIFallback(Action):

    def name(self):
        return "action_openai_fallback"

    def run(self, dispatcher, tracker, domain):

        user_message = tracker.latest_message.get("text")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful health support assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        dispatcher.utter_message(
            text=response.choices[0].message["content"]
        )

        return []


from typing import Any, Dict, Text
from rasa_sdk import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
# from datetime import datetime, timedelta

class ValidateAppointmentForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_appointment_form"

    def validate_appointment_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        text = slot_value.lower()

        if "tomorrow" in text:
            date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            return {"appointment_date": date}

        if "today" in text:
            date = datetime.now().strftime("%Y-%m-%d")
            return {"appointment_date": date}

        # basic date fallback
        return {"appointment_date": slot_value}

    def validate_appointment_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        return {"appointment_time": slot_value}
