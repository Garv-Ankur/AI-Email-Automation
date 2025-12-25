def detect_intent(email_text):
    text = email_text.lower()

    if "follow up" in text or "following up" in text or "reminder" in text:
        return "Follow-up"

    if "complaint" in text or "issue" in text or "problem" in text:
        return "Complaint"

    if "price" in text or "interested" in text or "buy" in text:
        return "Lead"

    if "meeting" in text or "schedule" in text:
        return "Meeting"

    return "General"
