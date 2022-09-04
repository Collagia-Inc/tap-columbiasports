"""REST client handling, including ColumbiaSportsStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk import Tap, Stream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ColumbiaSportsStream(Stream):
    """ColumbiaSports stream class."""

    def __init__(self, tap: Tap):
        super().__init__(tap=tap, name=None, schema=None)

    def get_records(self, partition: dict) -> Iterable[dict]:

        # url_base = "https://api-dev.columbia.com/ContentHubExternal/api/external/image/GetSeasonalAssetsBulk"
        # record = requests.get(
        #    url_base,
        #    headers={"Ocp-Apim-Subscription-Key": "e9c1a47a48684093864ad583f0a87770"},
        # )
        # data_list = record.json()
        # For Testing use below data
        data_list = [
            {
                "styleDescription": "SOREL GO\u2122 COFFEE RUN",
                "colorwayName": "Pure Silver, Moonstone",
                "sizeGroup": "Womens",
                "publicLinks": [
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/5075beb63b3e4914972c4f3618dd8123?v=0efa8340",
                        "rendition": "columbia_small",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/2b6fcbc33db84aafbd6c246f26fbe331?v=2ce11b56",
                        "rendition": "eCommerce_small",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/ab7c8e3d46c844e79db059fac23cda5f?v=fa861b1b",
                        "rendition": "eCommerce_medium",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/070c73fa35e84f8397284bb60e724646?v=3968440a",
                        "rendition": "thumbnail",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/01ebdf01dbab47b480e73441ebe1881e?v=a20379ea",
                        "rendition": "photoshot_high-res",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/e3f754e8c5934b8896ddfda49184e653?v=d4f9924f",
                        "rendition": "columbia_medium",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/8612030b8dfe42f49101bd88af6eff9a?v=79643458",
                        "rendition": "columbia_large",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/0ad1b218ce8a4bf094f4843755ed3011?v=ecb1c1a5",
                        "rendition": "eCommerce_large",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/b45890cd040e4f5990db5665cec138ec?v=c588431d",
                        "rendition": "columbia_icon",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/be4a7fbfd6d24bf4be8aa0e658ac7287?v=961c61b7",
                        "rendition": "White_Background_SOREL",
                    },
                ],
            },
            {
                "styleDescription": "SOREL GO\u2122 COFFEE RUN",
                "colorwayName": "Pure Silver, Moonstone",
                "sizeGroup": "Womens",
                "publicLinks": [
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/5075beb63b3e4914972c4f3618dd8123?v=0efa8340",
                        "rendition": "columbia_small",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/2b6fcbc33db84aafbd6c246f26fbe331?v=2ce11b56",
                        "rendition": "eCommerce_small",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/ab7c8e3d46c844e79db059fac23cda5f?v=fa861b1b",
                        "rendition": "eCommerce_medium",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/070c73fa35e84f8397284bb60e724646?v=3968440a",
                        "rendition": "thumbnail",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/01ebdf01dbab47b480e73441ebe1881e?v=a20379ea",
                        "rendition": "photoshot_high-res",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/e3f754e8c5934b8896ddfda49184e653?v=d4f9924f",
                        "rendition": "columbia_medium",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/8612030b8dfe42f49101bd88af6eff9a?v=79643458",
                        "rendition": "columbia_large",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/0ad1b218ce8a4bf094f4843755ed3011?v=ecb1c1a5",
                        "rendition": "eCommerce_large",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/b45890cd040e4f5990db5665cec138ec?v=c588431d",
                        "rendition": "columbia_icon",
                    },
                    {
                        "link": "https://delivery-qa.contenthub.columbia.com/api/public/content/be4a7fbfd6d24bf4be8aa0e658ac7287?v=961c61b7",
                        "rendition": "White_Background_SOREL",
                    },
                ],
            },
        ]
        for data in data_list:
            yield data

    # TODO: Set the API's base URL here:
