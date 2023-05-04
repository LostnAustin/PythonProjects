import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
      "name" : "Quincy"
    }.
    
    { "id" : "002",
      "x" : "7",
      "name" : "Chad"
    }
  ]
'''

info = json.loads(data)
print(info[1]['name'])
