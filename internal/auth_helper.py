class ProxiedUser:
    def __init__(self, headers):
        self.id = int(headers.get("User-Id", -1))
        self.permissions = {permission for permission in headers.get("Permissions", "").split(",")}
        self.school_id = int(headers.get("School-Id", -1))

    def has_permissions(self, permissions):
        return permissions.issubset(self.permissions)

    def headers_dict(self):
        return {
            'School-Id': str(self.school_id),
            'User-Id': str(self.id),
            'Permissions': ",".join([p for p in self.permissions])
        }
