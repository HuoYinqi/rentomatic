import collections.abc

from typing import Dict, Union, Optional

from rentomatic.shared import request_object as req


class StorageRoomListRequestObject(req.ValidRequestObject):

    def __init__(self, filters: Optional[dict] = None) -> None:
        self.filters = filters

    @classmethod
    def from_dict(cls, adict: Dict[str, dict]) -> Union['StorageRoomListRequestObject', req.InvalidRequestObject]:
        invalid_req = req.InvalidRequestObject() # type: req.InvalidRequestObject

        if 'filters' in adict and not isinstance(adict['filters'], collections.abc.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req
            
        return StorageRoomListRequestObject(filters=adict.get('filters', None))
