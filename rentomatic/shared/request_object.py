from typing import List, Dict, Any

class InvalidRequestObject(object):

    def __init__(self):
        self.errors: List[dict] = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


class ValidRequestObject(object):

    @classmethod
    def from_dict(cls, adict:Dict[str, Any]):
        raise NotImplementedError

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__
