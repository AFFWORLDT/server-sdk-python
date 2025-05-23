# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawFilesClient
from ..core.request_options import RequestOptions
from ..types.file import File
from .. import core
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawFilesClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[File]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]

        """
        response = self._raw_client.list(request_options=request_options)
        return response.data

    def create(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File uploaded successfully
        """
        response = self._raw_client.create(file=file, request_options=request_options)
        return response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File

        """
        response = self._raw_client.get(id, request_options=request_options)
        return response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File

        """
        response = self._raw_client.delete(id, request_options=request_options)
        return response.data

    def update(
        self, id: str, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> File:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]
            This is the name of the file. This is just for your own reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File

        """
        response = self._raw_client.update(id, name=name, request_options=request_options)
        return response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[File]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]

        """
        response = await self._raw_client.list(request_options=request_options)
        return response.data

    async def create(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File uploaded successfully
        """
        response = await self._raw_client.create(file=file, request_options=request_options)
        return response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File

        """
        response = await self._raw_client.get(id, request_options=request_options)
        return response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File

        """
        response = await self._raw_client.delete(id, request_options=request_options)
        return response.data

    async def update(
        self, id: str, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> File:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]
            This is the name of the file. This is just for your own reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File

        """
        response = await self._raw_client.update(id, name=name, request_options=request_options)
        return response.data
