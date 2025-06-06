# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Analysis(UncheckedBaseModel):
    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the summary of the call. Customize by setting `assistant.analysisPlan.summaryPrompt`.
    """

    structured_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="structuredData")
    ] = pydantic.Field(default=None)
    """
    This is the structured data extracted from the call. Customize by setting `assistant.analysisPlan.structuredDataPrompt` and/or `assistant.analysisPlan.structuredDataSchema`.
    """

    structured_data_multi: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Optional[typing.Any]]]],
        FieldMetadata(alias="structuredDataMulti"),
    ] = pydantic.Field(default=None)
    """
    This is the structured data catalog of the call. Customize by setting `assistant.analysisPlan.structuredDataMultiPlan`.
    """

    success_evaluation: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="successEvaluation")] = (
        pydantic.Field(default=None)
    )
    """
    This is the evaluation of the call. Customize by setting `assistant.analysisPlan.successEvaluationPrompt` and/or `assistant.analysisPlan.successEvaluationRubric`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
