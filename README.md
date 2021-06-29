# Application Programming Interface (API)
- It's a connection between two systems or programs.
- It is used to offer or get a service from other software.

## REST API
- Representational State Transfer (REST) is an internet protocol used to guide the design and development of the WWW architecture.
- A REST API or RESTful API is an API that is used on the web and that conforms to the REST architecture.

### Postcode API Exercise
```python
import requests

class PostcodeToLocation:
    
    def get_postcode(self, post):
        # Call API
        check_response_postcode = requests.get("https://api.postcodes.io/postcodes/" + post)
        # If the response is successful, code 200
        if check_response_postcode:
            # Turn response to json format
            json_response = check_response_postcode.json()
            # Get result dict
            result = json_response['result']
            # Return location
            return f"Location: {result['admin_district']}"
        else:
            return "Sorry something went wrong, please make sure you type your postcode correctly."


# Get user input for postcode
post_code = input("Please enter your postcode:  ")
# Create class object
location = PostcodeToLocation()
# Output location by passing the input to the get_postcode function
print(location.get_postcode(post_code))
```