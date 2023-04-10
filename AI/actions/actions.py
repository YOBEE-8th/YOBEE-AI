from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAskIngredient(Action):

    def name(self) -> Text:
        return "action_ask_ingredient"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the latest message from user
        latest_message = tracker.latest_message

        # Get the entities from the latest user message
        entities = latest_message.get("entities", [])

        # Log the entities to console
        # print(entities[0]['value'])
        print(entities)


        for entity in entities:
            if entity['entity'] == 'ingredient':
                ingredient = entity['value']

                # ingredient = entities[0]['value']
                if ingredient:
                    dispatcher.utter_message(template="utter_ask_ingredient", ingredient=ingredient)
                else:
                    dispatcher.utter_message(text="재료 이름을 다시 말씀해주시겠어요?")
                    print("재료 없는 경우")

        return []