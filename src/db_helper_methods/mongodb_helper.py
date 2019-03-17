class MongoDbSchema(object):
    class User(object):
        _first_name = None
        _last_name = None
        _user_id = None
        _description = None
        def __init__(self, first_name, last_name, user_id, description):
            self._first_name = first_name
            self._last_name = last_name
            self._user_id = user_id
            self._description = description
        def is_usable(self):
            if not all(self._first_name, self._last_name, self._user_id):
                return False
            if not self._description:
                self._description = 'Fill in text here describing yourself'
            return True

