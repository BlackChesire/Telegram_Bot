from datetime import datetime


def sample_responses(input_text):
    # response handling "input text" is the user massage
    user_messages = str(input_text)
    if user_messages in ("שלום", "?", "היי"):
        return "היי שלום"

    if user_messages in ("מי אתה ?", "מי אתה?"):
        return "אני הבוט של תל חי"
    if user_messages in ("מה קורה ?", "מה המצב?"):
        return "אני בסדר איך אוכל לעזור?"
    if user_messages in ("שעה?", "תאריך?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    if user_messages in("מי יצר אותך?"):
        return  "@ChesireIL"

    return "ממממ סורי לא הבנתי אותך תנסה להיות יותר ספציפי"
