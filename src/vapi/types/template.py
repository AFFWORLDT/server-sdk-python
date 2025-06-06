# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .template_details import TemplateDetails
import typing_extensions
from .template_provider_details import TemplateProviderDetails
from ..core.serialization import FieldMetadata
from .tool_template_metadata import ToolTemplateMetadata
from .template_visibility import TemplateVisibility
import pydantic
from .template_provider import TemplateProvider
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Template(UncheckedBaseModel):
    details: typing.Optional[TemplateDetails] = None
    provider_details: typing_extensions.Annotated[
        typing.Optional[TemplateProviderDetails], FieldMetadata(alias="providerDetails")
    ] = None
    metadata: typing.Optional[ToolTemplateMetadata] = None
    visibility: typing.Optional[TemplateVisibility] = None
    type: typing.Literal["tool"] = "tool"
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the template. This is just for your own reference.
    """

    provider: typing.Optional[TemplateProvider] = None
    id: str = pydantic.Field()
    """
    The unique identifier for the template.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    The unique identifier for the organization that this template belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    The ISO 8601 date-time string of when the template was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    The ISO 8601 date-time string of when the template was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
