from rest_framework.response import Response


class SuccessResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
        if not data:
            data = {}
        data['Success'] = True
        super().__init__(data, status, template_name, headers, exception, content_type)


class SuccessNotResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
        if not data:
            data = {}
        data['Success'] = False
        super().__init__(data, status, template_name, headers, exception, content_type)
