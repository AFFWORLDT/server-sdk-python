# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .fallback_talkscriber_transcriber_language import FallbackTalkscriberTranscriberLanguage
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackTalkscriberTranscriber(UncheckedBaseModel):
    provider: typing.Literal["talkscriber"] = pydantic.Field(default="talkscriber")
    """
    This is the transcription provider that will be used.
    """

    model: typing.Optional[typing.Literal["whisper"]] = pydantic.Field(default=None)
    """
    This is the model that will be used for the transcription.
    """

    language: typing.Optional[FallbackTalkscriberTranscriberLanguage] = pydantic.Field(default=None)
    """
    This is the language that will be set for the transcription. The list of languages Whisper supports can be found here: https://github.com/openai/whisper/blob/main/whisper/tokenizer.py
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
