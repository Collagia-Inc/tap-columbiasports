"""REST client handling, including ColumbiaSportsStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk.streams import RESTStream

import os

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ColumbiaSportsStream(RESTStream):

    # limit: int = 10

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    @property
    def http_headers(self) -> dict:
        """Retaurns Header for API"""
        subscription_key = self.config["subscription_key"]
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        return headers

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        return {
            # "Perspective": "b",
            # "colorwayName": "black"
        }

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        data_list = response.json()

        for data in data_list:
            yield data
