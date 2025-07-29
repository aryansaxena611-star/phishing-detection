# phishing_app.py

import streamlit as st

# Title and instructions
st.title(" Phishing Email Detection Tool")
st.write("Paste any email message below to check for potential phishing attempts.")

# Input box
email_content = st.text_area("Enter Email Content:", height=250)

# List of phishing keywords
phishing_keywords = [
    "urgent", "click here", "verify", "password", "account suspended",
    "login", "confirm", "security", "update", "alert", "verify account"
]

# Process the email
if st.button(" Scan Email"):
    if email_content.strip() == "":
        st.warning(" Please paste some email content.")
    else:
        lower_content = email_content.lower()
        detected = []

        for keyword in phishing_keywords:
            if keyword in lower_content:
                detected.append(keyword)

        # Show results
        if detected:
            st.error("Potential Phishing Detected!")
            st.write("Suspicious keywords found:")
            for word in detected:
                st.write(f"• **{word}**")
        else:
            st.success("✅ No phishing keywords detected. Email appears safe.")
