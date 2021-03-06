# -*- coding: utf-8 -*-
from CHPP import CHPP

# create a new helper object
oauth_helper = CHPP()

# 1) Obtain user authorization
# This steps contains the logic for obtaining an Access Token from the end
# user (steps A...F on the Hattrick OAuth Authentication flow diagram).

# Obtain and URL for a Request Token that will be passed to the end user
# diagram: steps A, B
registration_url = oauth_helper.get_request_token_url()

# At this point, the user needs to open the 'registration_url' (which points
# to chpp.hattrick.org) and enter his username and password. At the end of the
# process, a PIN is presented on their browser ('pin').
# diagram: steps C, D
print( "enter pin")
pin = input().__str__()

# Get a valid Access Token, by using the generated pin.
# diagram: steps E, F
access_token = oauth_helper.get_access_token(pin)
print( "Your access tokens are", access_token)

# The Access Token is now ready to be used. For convenience, the key and
# secret should be stored on a database or permanent storage:
user_key = access_token.key
user_secret = access_token.secret

# 2) Access protected resources
# Once a valid Access Token for a particular user is obtained, it is used for
# retrieving the information needed for the application.
# The oauth_helper.request_resource_with_key() method wraps the needed logic.
# diagram: steps G, H

# example: get the list of youth players
xmldoc = oauth_helper.request_resource_with_key(
                                                user_key,
                                                user_secret,
                                                'youthplayerlist',
                                                {
                                                 'actionType' : 'details',
                                                 'showScoutCall' : 'true',
                                                 'showLastMatch' : 'true'
                                                }
                                               )
