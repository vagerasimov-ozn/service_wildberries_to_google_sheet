from wildberries_api import api_request
from format import format_to_google
from google_integration import add_to_sheet

if __name__ == "__main__":
    api_response = api_request()
    if api_response:
        values_to_add = format_to_google(api_response)
        if values_to_add:
            add_to_sheet(values_to_add)
