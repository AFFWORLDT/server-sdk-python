from vapi import Vapi

# Vapi क्लाइंट को इनिशियलाइज़ करें
client = Vapi(
    token="6e572e66-e52c-4855-beec-dc04ba6a767c"
)

try:
    # assistant_id पैरामीटर के साथ कॉल बनाएं
    response = client.calls.create(
        assistant_id="a0ec6009-b9d9-4279-acee-5174eb9eaef8",
        transport={"provider": "vapi.websocket"}
    )
    print("वेब कॉल लिंक/response:", response)
except Exception as e:
    print("एरर आया:", str(e)) 