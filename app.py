from email_reader import read_unread_emails
from email_sender import send_reply
from intent_detector import detect_intent

def main():
    print("🚀 AI Email Automation Started")

    emails = read_unread_emails()
    print("📨 Emails fetched:", len(emails))

    for email_data in emails:
        sender = email_data["from"]
        subject = email_data["subject"]
        body = email_data["body"]

        print("\n📩 Email from:", sender)
        intent = detect_intent(body)
        print("🧠 Intent:", intent)

        # ❌ Skip system / no-reply / newsletter emails
        sender_lower = sender.lower()
        skip_words = [
            "no-reply", "noreply", "do-not-reply",
            "bankbazaar", "microsoft", "newsletter",
            "instagram", "adobe", "start daily"
        ]

        if any(word in sender_lower for word in skip_words):
            print("🚫 Skipped system/newsletter email")
            return

        # ✅ Reply ONLY to follow-up emails
        if intent == "Follow-up":
            send_reply(
                sender,
                "Re: " + subject,
                "Thanks for your follow-up. I will get back to you shortly"
                # "IM Garv And this is My first Ai Project."
            )
            print("✅ Auto-reply sent")
        else:
            print("ℹ️ Not a follow-up email")

if __name__ == "__main__":
    main()
