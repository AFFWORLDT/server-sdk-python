# This file was auto-generated by Fern from our API Definition.

import typing
from ...types.byo_phone_number import ByoPhoneNumber
from ...types.twilio_phone_number import TwilioPhoneNumber
from ...types.vonage_phone_number import VonagePhoneNumber
from ...types.vapi_phone_number import VapiPhoneNumber
from ...types.telnyx_phone_number import TelnyxPhoneNumber

PhoneNumbersGetResponse = typing.Union[
    ByoPhoneNumber, TwilioPhoneNumber, VonagePhoneNumber, VapiPhoneNumber, TelnyxPhoneNumber
]
