"""Stream type classes for tap-columbiasports."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_columbiasports.client import ColumbiaSportsStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ColumbiaSportsImageDataStream(ColumbiaSportsStream):
    """Define custom stream."""

    name = "columbia-sports-wear"
    path = "/"
    primary_keys = ["fileName"]
    replication_key = "fileName"
    replicaton_method = "INCREMENTAL"

    schema = th.PropertiesList(
        th.Property("fileName", th.StringType, required=True),
        th.Property("sizeGroup", th.StringType),
        th.Property("styleDescription", th.StringType),
        th.Property("colorwayName", th.StringType),
        th.Property(
            "publicLinks",
            th.ArrayType(
                th.ObjectType(
                    th.Property("link", th.StringType),
                    th.Property("rendition", th.StringType),
                )
            ),
        ),
    ).to_dict()
