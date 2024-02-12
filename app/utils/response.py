class ApiResponse:
    def __init__(self, status_code, success, message, data=None):
        self.status_code = status_code
        self.success = success
        self.message = message
        self.data = data

    def to_dict(self):
        response_dict = {'status_code': self.status_code, 'success': self.success, 'message': self.message}
        if self.data:
            response_dict['data'] = self.data
        return response_dict
