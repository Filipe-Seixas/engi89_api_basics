import requests

# Call API
check_response_postcode = requests.get("https://api.postcodes.io/postcodes/lu15ft")

# First iteration
if check_response_postcode.status_code == 200:
    print("The postcode is valid and status code is", check_response_postcode.status_code)
else:
    print("Oops something went wrong. Please try again later.")


# Second Iteration
class WebStatusCode:
    def checking_status_code(self):
        if check_response_postcode:
            return "Success"
        else:
            return "Unavailable"


stat_code = WebStatusCode()
print(stat_code.checking_status_code())

# Third Iteration
response_dict = check_response_postcode.json()
print(response_dict)  # Get data about postcode in JSON format
print(type(response_dict))

result_dict = response_dict['result']
print(result_dict)
for key in result_dict.keys():
    print(f"The name of they key is '{key}' and the value inside the key is '{result_dict[key]}'")

# Fourth Iteration


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
