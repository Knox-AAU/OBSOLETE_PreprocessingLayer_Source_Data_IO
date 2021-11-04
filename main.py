from knox_source_data_io.io_handler import IOHandler
import json
import traceback

def test():
    try:
        f = open("schemas/2019-07-12_2sektion.json")
        data = json.load(f)
        f.close()
        print(data)
        print(type(data))
        IOHandler.validate_json(data, "schemas/publication.schema.json")
    except Exception as e:
        print(e)
        traceback.print_exc(e)
test()