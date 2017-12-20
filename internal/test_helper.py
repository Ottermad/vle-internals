class AuthUser:
    def __init__(self, user_id=1, school_id=1, permissions=[]):
        self.user_id = user_id
        self.school_id = school_id
        self.permissions = permissions

    def headers_dict(self):
        return {
            'School-Id': self.school_id,
            'User-Id': self.user_id,
            'Permissions': ",".join([p for p in self.permissions])
        }
