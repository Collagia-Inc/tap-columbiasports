"""REST client handling, including ColumbiaSportsStream base class."""

import requests
import pickle
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk import Tap, Stream
import os

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ColumbiaSportsStream(Stream):
    """ColumbiaSports stream class."""

    def __init__(self, tap: Tap):
        try:
            with open(os.environ["STORAGE_INDEX_NAME"], "rb") as f:
                self.my_set = pickle.load(f)
        except:
            self.my_set = set()
        super().__init__(tap=tap, name=None, schema=None)

    def get_records(self, partition: dict) -> Iterable[dict]:
        url_base = self.config["api_url"]
        subscription_key = self.config["subscription_key"]
        record = requests.get(
            url_base,
            headers={"Ocp-Apim-Subscription-Key": subscription_key},
        )
        data_list = record.json()
        for data in data_list:
            if data["fileName"] not in self.my_set:
                self.my_set.add(data["fileName"])
                yield data
        with open(os.environ["STORAGE_INDEX_NAME"], "wb") as f:
            pickle.dump(self.my_set, f)

    # TODO: Set the API's base URL here:
