"""ColumbiaSports tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_columbiasports.streams import (
    ColumbiaSportsImageDataStream,
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    ColumbiaSportsImageDataStream,
]


class TapColumbiaSports(Tap):
    """ColumbiaSports tap class."""

    name = "tap-columbiasports"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://api-dev.columbia.com/ContentHubExternal/api/external/image/GetSeasonalAssetsBulk",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
