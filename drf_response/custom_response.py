from rest_framework import status
from rest_framework.response import Response


class ResponseInterface(object):
    success = True

    def __init__(self, message, status):
        self.message = message
        self.status = status

    def get_response(self, message=None, status=None):

        if status:
            self.status = status
        if message:
            self.message = message

        obj = {
            "success": self.success,
            "message": self.message
        }

        return Response(obj, status=self.status)


class SuccessResponse(ResponseInterface):
    success = True


class ErrorResponse(ResponseInterface):
    success = False


class ResultResponse(ResponseInterface):

    def get_response(self, message={}, status=status.HTTP_200_OK):        
        self.status = status
        self.message = message
        return Response(self.message, status=self.status)


class CustomResponse():

    def response(self, response_type):

        return response_type


success = CustomResponse().response(SuccessResponse('Successfully Completed', status.HTTP_200_OK))
error = CustomResponse().response(ErrorResponse('Operation Faild', status.HTTP_400_BAD_REQUEST))
result = CustomResponse().response(ResultResponse({}, status.HTTP_200_OK))
