# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawAnalyticsClient
from ..types.analytics_query import AnalyticsQuery
from ..core.request_options import RequestOptions
from ..types.analytics_query_result import AnalyticsQueryResult
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawAnalyticsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyticsClient
        """
        return self._raw_client

    def get(
        self, *, queries: typing.Sequence[AnalyticsQuery], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnalyticsQueryResult]:
        """
        Parameters
        ----------
        queries : typing.Sequence[AnalyticsQuery]
            This is the list of metric queries you want to perform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnalyticsQueryResult]

        """
        response = self._raw_client.get(queries=queries, request_options=request_options)
        return response.data


class AsyncAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyticsClient
        """
        return self._raw_client

    async def get(
        self, *, queries: typing.Sequence[AnalyticsQuery], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnalyticsQueryResult]:
        """
        Parameters
        ----------
        queries : typing.Sequence[AnalyticsQuery]
            This is the list of metric queries you want to perform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnalyticsQueryResult]

        """
        response = await self._raw_client.get(queries=queries, request_options=request_options)
        return response.data
