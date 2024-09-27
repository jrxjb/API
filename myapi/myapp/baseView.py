from rest_framework import generics, status

class BaseView(generics.GenericAPIView):
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        status_code = response.status_code

        error_messages = {
            status.HTTP_400_BAD_REQUEST: "Solicitud incorrecta.",
            status.HTTP_401_UNAUTHORIZED: "No autorizado.",
            status.HTTP_403_FORBIDDEN: "Prohibido.",
            status.HTTP_404_NOT_FOUND: "No encontrado.",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Error interno del servidor.",
        }
        
        message = error_messages.get(status_code, str(exc))

        response.data = {
            'error': message,
            'status_code': status_code
        }
        return response