import json
import base64
import random


def text_to_morse(text):
    
    morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
    }
    morse_code = ""
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '  
    return {'encript_string': morse_code,'status': 'Success','statusCode': 200}

def encode_text(text):
    
    encoded_string = base64.b64encode(text.encode()).decode('utf-8')
    return {'encript_string': encoded_string,'status': 'Success','statusCode': 200}


def lambda_handler(event, context):
    k={}
    k['body']= json.dumps(event) 
    event = k
    response_db = False
    response = {'encript_string': 'Invalid Code','status': 'Failure','statusCode': 500}
    result = json.loads(event['body'])
    if result['code'] == 'mascode':
        response = text_to_morse(result['name'])
    elif result['code'] == 'encode':
        response = encode_text(result['name'])
    response_dict = {
        'name' : result['name'],
        'code' : result['code'],
        'encript_string' : response['encript_string'],
        'status' : response['status'],
    }
    return {
        'statusCode': response['statusCode'],
        'body': json.dumps(response_dict)
    }
