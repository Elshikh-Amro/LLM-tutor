import pywhatkit as pwk

# Define the recipient's phone number (with country code) and the message
phone_number = (
    "+249906015904"  # Replace with the recipient's phone number including country code
)

message = "Hello, this is a test message!"  # Replace with your message

# Send the message instantly
pwk.sendwhatmsg_instantly(phone_number, message)
