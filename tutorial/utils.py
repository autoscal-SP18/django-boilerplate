from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # TODO: custom handling to be done here. and exception block to exist at views level. All other levels throw
    #  exceptions. Read https://www.django-rest-framework.org/api-guide/exceptions/#api-reference for custom
    #  Exception class implementation Idea is to extend base Exception class, then create specific exceptions - API,
    #  Parsing, DAO, etc. Action for @vishal-sp18 to read more.

    return response
