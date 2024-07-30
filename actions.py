from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from llmbot import query_llm
import json
import os

# Загрузка данных RAG из JSON
data_path = 'C:/rasa/llmrs/data/cyprus-bot-data.json'
if os.path.exists(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = {}

class ActionQueryLLM(Action):
    def name(self) -> Text:
        return "action_query_llm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_query = tracker.latest_message.get('text')
        llm_response = query_llm(user_query)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionHousingRent(Action):
    def name(self) -> Text:
        return "action_housing_rent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных из RAG
        rag_data = data.get("housing_rent", {}).get("real_estate_services", "")
        prompt = f"Информация о риелторах и аренде жилья на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionRentalTips(Action):
    def name(self) -> Text:
        return "action_rental_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных из RAG
        rag_data = data.get("housing_rent", {}).get("rental_tips", "")
        prompt = f"Советы по аренде жилья на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionBankInfo(Action):
    def name(self) -> Text:
        return "action_bank_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных из RAG
        rag_data = data.get("banks", {}).get("bank_info", "")
        prompt = f"Информация о банках на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        # Запрос к LLM
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionWaterSupply(Action):
    def name(self) -> Text:
        return "action_water_supply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных из RAG
        rag_data = data.get("water_supply", {}).get("general_info", "")
        prompt = f"Информация о водоснабжении на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionUtilitiesRegistration(Action):
    def name(self) -> Text:
        return "action_utilities_registration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных из RAG
        rag_data = data.get("utilities_registration", {}).get("water_registration", "")
        prompt = f"Информация о регистрации коммунальных услуг на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionPaymentSystems(Action):
    def name(self) -> Text:
        return "action_payment_systems"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных из RAG
        rag_data = data.get("payment_systems", {}).get("jcc_info", "")
        prompt = f"Информация о платежных системах на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionWasteManagement(Action):
    def name(self) -> Text:
        return "action_waste_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных
        rag_data = data.get("waste_management", {}).get("waste_sorting", "")
        prompt = f"Информация о сортировке мусора на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []

class ActionEmergencyNumber(Action):
    def name(self) -> Text:
        return "action_emergency_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получение данных
        rag_data = data.get("emergency_number", {}).get("emergency_contact", "")
        prompt = f"Информация об экстренных номерах на Кипре: {rag_data}\n\nВопрос пользователя: {tracker.latest_message.get('text')}\n\nОтвет:"
        
        llm_response = query_llm(prompt)
        
        dispatcher.utter_message(text=llm_response)
        return []
class ActionHandleLLMResponse(Action):
    def name(self) -> Text:
        return "action_handle_llm_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        llm_response = tracker.get_slot("llm_response")
        
        if not llm_response or "Ошибка" in llm_response:
            dispatcher.utter_message(response="utter_fallback")
            return [SlotSet("fallback", True)]
        
        dispatcher.utter_message(text=llm_response)
        return [SlotSet("fallback", False)]
