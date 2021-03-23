from datetime import datetime


def sample_responses(input_text):
    user_messages = str(input_text).lower()
    if user_messages in ("שלום"):
        return  "היי שלום מה קורה ?"

    if user_messages in ("מי אתה ?","מי אתה?"):
        return  "אני הבוט של תל חי"

    if user_messages in ("שעה?","תאריך?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    return "I dont understand you ! try again!"