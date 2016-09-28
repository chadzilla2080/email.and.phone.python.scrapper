#! python3

import re, pyperclip

# Create a RegEx object for phone numbers

phoneRegex = re.compile(r'''

# 415-555-0000, 555-0000, (415) 555-000, 555-000 ext 12345, ext. 12345, x12345

(                            # this is the first group for all
((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
(\s|-)                       # first separator
\d\d\d                       # first 3 digits
-                            # separator
\d\d\d\d                     # last four digits
(((ext(\.)?\s) |x)           # extension (optional)
 (\d{2,5}))?                 # extension number-part (optional)
)                            # end the first all group
''', re.VERBOSE)

# Create a RegEx object for email addresses

emailRegex = re.compile(r'''

# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+  # name part
@                # @ symbol
[a-zA-Z0-9_.+]+  # domain name part

''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# TODO: Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# This loop sets an empty list for phone number, then sets a variable for phone numbers in each tuple, then append the first phone number to allPhoneNumbers

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
print(extractedPhone)  # Just a test to see what was found in phone numbers
print(extractedEmail)  # Just a test to see what is found from emails
print(allPhoneNumbers) # Just a test to see if we got the single full phone number from each tuple in the loop

# Copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
