import imaplib
import email
from config import EMAIL, APP_PASSWORD

def read_unread_emails():
    print("🔐 Connecting to Gmail IMAP...")

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    print("✅ Logged in")

    mail.select("INBOX")
    print("📂 Inbox selected")

    # 🔍 Get UNREAD emails
    status, messages = mail.search(None, "UNSEEN")
    email_ids = messages[0].split()
    print("📨 Unread emails found:", len(email_ids))

    if not email_ids:
        mail.logout()
        return []

    # ✅ PICK ONLY THE LATEST UNREAD EMAIL
    latest_email_id = email_ids[-1]
    print("📥 Fetching latest email ID:", latest_email_id)

    emails = []

    _, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])

            sender = msg.get("From", "")
            subject = msg.get("Subject", "")
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        payload = part.get_payload(decode=True)
                        if payload:
                            body = payload.decode(errors="ignore")
                        break
            else:
                payload = msg.get_payload(decode=True)
                if payload:
                    body = payload.decode(errors="ignore")

            emails.append({
                "from": sender,
                "subject": subject,
                "body": body
            })

    mail.logout()
    print("🔒 Logged out")
    return emails
