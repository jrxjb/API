from rest_framework import generics, status
from rest_framework.response import Response

class BaseView(generics.GenericAPIView):

    def error_response(self, message, status_code=status.HTTP_400_BAD_REQUEST):
        """
        Helper method to generate error responses consistently.
        :param message: Error message or list of error messages.
        :param status_code: HTTP status code for the response. Default is 400 (Bad Request).
        :return: Response object with error details.
        """
        errors = message if isinstance(message, dict) else {"detail": message}
        return Response({"errors": errors}, status=status_code)
