######################################################################################
# Title:        lyft-apprentice-test
# Author:       Elmer Astudillo
# Date:         4/18/2018
# Description:  A web application written for Lyft's software engineer apprenticeship.
######################################################################################

from flask import Flask, request, json, jsonify
import sys

app = Flask(__name__)

# Assign str to unicode to handle string naming based on python version
if sys.version_info[0] >= 3:
    unicode = str

# ======
# Routes
# ======


@app.route('/test', methods=['POST'])
def post():
    """
    Post request route recieves a json object containing a string and
    returns either an exception or the original string parsed. (Every 3rd character)
    """
    if request.headers['Content-Type'] != 'application/json':
        error_value = "Unsupported Media Type"
        return error_handling(error_value, 415)
    json = request.json
    string_to_cut = json['string-to-cut']

    if string_to_cut == None:
        error_value = "User must provide a valid string in the body of the post request."
        return error_handling(error_value, 400)
    else:
        if type(string_to_cut) is not unicode:
            error_value = "User must provide input of string type."
            return error_handling(error_value, 400)
        elif len(string_to_cut) < 3:
            error_value = "User must provide a string with more than 3 characters."
            return error_handling(error_value, 400)
        parsedString = parseString(string_to_cut)
        json = jsonify(return_string=parsedString)
        return(json, 200, None)


# =======
# Helpers
# =======


def error_handling(error_response, status_code):
    """Returns a error response json object and status code."""
    json = jsonify(Error=error_response)
    return(json, status_code, None)


def parseString(org_string):
    """Returns a new string containing every 3rd character of the original str."""
    counter = 1
    str_builder = []
    for i in org_string:
        if i == " ":
            continue
        if counter == 3:
            str_builder.append(i)
            counter = 1
        else:
            counter += 1
    return ''.join(str_builder)


if __name__ == '__main__':
    app.run
