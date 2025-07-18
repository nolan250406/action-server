from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import os

# Đường dẫn tuyệt đối tới file flights.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "flights.csv")


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Xin chào! Tôi có thể giúp gì cho bạn tại sân bay?")
        return []


class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tạm biệt và chúc bạn có chuyến bay thuận lợi!")
        return []


class ActionBotChallenge(Action):
    def name(self) -> Text:
        return "action_bot_challenge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tôi là chatbot hỗ trợ sân bay, rất vui được giúp đỡ bạn!")
        return []


class ActionFlightStatus(Action):
    def name(self) -> Text:
        return "action_flight_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flight_code = next(tracker.get_latest_entity_values("flight_code"), None)
        if not flight_code:
            flight_code = tracker.get_slot("flight_code")

        if not flight_code:
            dispatcher.utter_message(text="Vui lòng cung cấp mã chuyến bay để tôi kiểm tra tình trạng giúp bạn.")
            return []

        try:
            df = pd.read_csv(CSV_PATH)
            matched = df[df['flight_code'].str.upper() == flight_code.upper()]
            if not matched.empty:
                row = matched.iloc[0]
                message = (
                    f"✈️ Tình trạng chuyến bay {row['flight_code']}:\n"
                    f"- Hãng: {row['airline']}\n"
                    f"- Giờ cất cánh: {row['departure_time']}\n"
                    f"- Giờ hạ cánh: {row['arrival_time']}\n"
                    f"- Tình trạng: {row['status']}"
                )
                dispatcher.utter_message(text=message)
            else:
                dispatcher.utter_message(text=f"Không tìm thấy thông tin chuyến bay {flight_code}.")
        except Exception as e:
            dispatcher.utter_message(text="Đã xảy ra lỗi khi kiểm tra tình trạng chuyến bay.")
            print(f"[ERROR] action_flight_status: {e}")

        return []


class ActionCheckinTime(Action):
    def name(self) -> Text:
        return "action_checkin_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Thời gian mở quầy check-in thường là 2 tiếng trước giờ bay.")
        return []


class ActionFlightRoute(Action):
    def name(self) -> Text:
        return "action_flight_route_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bạn vui lòng cung cấp mã chuyến bay để tôi cung cấp lộ trình cụ thể.")
        return []


class ActionBaggageLost(Action):
    def name(self) -> Text:
        return "action_baggage_lost"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Rất tiếc về sự cố. Vui lòng đến quầy hỗ trợ hành lý thất lạc gần nhất hoặc gọi tổng đài.")
        return []


class ActionGateInfo(Action):
    def name(self) -> Text:
        return "action_gate_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Cửa ra máy bay thường được in trên thẻ lên máy bay. Vui lòng kiểm tra lại giúp tôi.")
        return []


class ActionServices(Action):
    def name(self) -> Text:
        return "action_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sân bay có đầy đủ dịch vụ như wifi, ăn uống, đổi tiền, sạc điện thoại. Bạn cần gì tôi có thể chỉ giúp.")
        return []


class ActionTicketChange(Action):
    def name(self) -> Text:
        return "action_ticket_change"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bạn vui lòng liên hệ đại lý hoặc hãng bay để đổi vé, phí đổi sẽ tùy vào từng điều kiện vé.")
        return []


class ActionTicketRefund(Action):
    def name(self) -> Text:
        return "action_ticket_refund"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bạn có thể hoàn vé tùy theo điều kiện vé. Vui lòng cung cấp mã đặt chỗ để kiểm tra.")
        return []


class ActionFlightDelayCompensation(Action):
    def name(self) -> Text:
        return "action_flight_delay_compensation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Nếu chuyến bay của bạn bị hoãn hoặc hủy, bạn có thể được đền bù hoặc đổi vé tùy theo chính sách của hãng."
        )
        return []
