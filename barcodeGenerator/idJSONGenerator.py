import airtablewrapper
import json

participantList = airtablewrapper.get_participants()
participantJSONArray = []

for participant in participantList:
    newParticipant = {
        'id': participant['fields']['Barcode']['text'],
        'name': participant['fields']['First Name'] + " " + participant['fields']['Last Name'],
        'role': participant['fields']['Role'].lower()
    }
    participantJSONArray.append(newParticipant)

participantJSONStr = json.dumps(participantJSONArray)

myFile = open('participants.json', 'w')

myFile.write(participantJSONStr)
