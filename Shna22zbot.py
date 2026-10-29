import time
import requests

# 1. ضع التوكن الذي أعطاك إياه BotFather هنا بين القوسين
TOKEN = "AAHmP0Kbit6BmoG-p_BAlb5VTN_pkSLsOiM"

# 2. ضع آي دي الجروب هنا (مهم أن تبدأ بالإشارة السالبة إذا كان جروب خارجي)
CHAT_ID = "1004468118068"

# 3. قائمة الرسائل التي سيرسلها البوت بالتدوب أو بشكل عشوائي
messages = [
    "مرحباً بالجميع! كيف تجري أموركم اليوم؟ 😊",
    "لا تنسوا مشاركة مواضيعكم واستفساراتكم هنا في الكروب.",
    "من لديه اقتراح أو فكرة يريد مناقشتها؟ الباب مفتوح للجميع!",
    "يسعد مساكم/صباحكم يا شباب، منورين الكروب دائماً 🌹",
]


def send_message_to_group(text):
  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": text}
  try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
      print("تم إرسال الرسالة بنجاح!")
    else:
      print(f"فشل الإرسال: {response.text}")
  except Exception as e:
    print(f"حدث خطأ: {e}")


if __name__ == "__main__":
  print("البوت بدأ العمل وسيبقى يرسل رسائل بشكل دوري...")
  i = 0
  while True:
    # اختيار رسالة من القائمة بالدور
    current_message = messages[i]
    send_message_to_group(current_message)

    # الانتقال للرسالة التالية، وإذا انتهت القائمة يعود للأولى
    i = (i + 1) % len(messages)

    # ⏳ حدد الفاصل الزمني بالثواني:
    # 7200 ثانية تعني ساعتين (أنصح بألا تقل عن ساعة لكي لا يحظر تيليجرام البوت)
    time.sleep(7200)
