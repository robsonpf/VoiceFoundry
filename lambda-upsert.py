# import boto3
import vanitynumber # Used Python Module to implement wordification  functionalities generation.
# dynamodb = boto3.resource("dynamodb")
# table = dynamodb.Table("contact-list")

def validWord(word):
    with open('dictionary.txt', 'r') as f:
        dict_words = f.read().splitlines()
        for line in dict_words:
            if word.lower() in line:
                return True
        return False

def vowelWord(word):
    vowels = ['a','e','i','o','u']
    if word[1].lower() in vowels:
        return False
    return True
bestResults = []
words = vanitynumber.all_wordifications("1-404-289-4567") # Pass phoneNumber as input

for i in words:
    if validWord(i[6:]):
        bestResults.append(i)
    else:
        firstWord = i[6:][0:3]
        secondWord = i[6:][3:]
        if (validWord(firstWord) and (not vowelWord(firstWord))) and validWord(secondWord):
            bestResults.append(i)

if not bestResults:
    print(words[:3])
else:
    print(bestResults[:3])
    print(bestResults[:3])

def lambda_handler(event, context):
    phoneNumber = event['Details']['ContactData']['CustomerEndpoint']['Address']


    if not phoneNumber:
        raise("JSON object is invalid")

    transferTo = event['Details']['ContactData']['CustomerEndpoint']['Address']


    if transferTo:
        put(phoneNumber, transferTo) # Replace phoneNumber with bestResults
    else:
        return get(phoneNumber)


# Here I will send the bestResults number to AWS Connect
def put(phoneNumber, transferTo):
    table.put_item(Item={'origin': address, 'transferTo': transferTo})


# Here I will get the caller ID and will use the input to words in line 21
def get(phoneNumber):
    response = table.get_item(Key={'origin': address})
    if "Item" not in response:
        raise Exception("not found")

    return response.get("Item")
