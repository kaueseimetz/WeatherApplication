from weather import main
import json

data = json.loads(main())
keys = list(data.keys())

#print(data[str(list(data.keys())[0])])

print(data[keys[0]])