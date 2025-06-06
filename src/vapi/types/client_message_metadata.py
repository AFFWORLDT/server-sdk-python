# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientMessageMetadata(UncheckedBaseModel):
    type: typing.Literal["metadata"] = pydantic.Field(default="metadata")
    """
    This is the type of the message. "metadata" is sent to forward metadata to the client.
    """

    metadata: str = pydantic.Field()
    """
    This is the metadata content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
