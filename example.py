from knox_source_data_io.io_handler import *
from knox_source_data_io.models.model import Model
import os


class SubModelClass(Model):
    name: str
    email: str

    def __init__(self, values: dict = None, **kwargs):
        values = values if values is not None else kwargs
        self.name = values.get("name", "")
        self.email = values.get("email", "")


export_able_object = SubModelClass()
export_able_object.name = "Hans"
export_able_object.email = "hans@hansen.dk"

# Generate
handler = IOHandler(Generator(app="This app", version=1.0), "link/to/schema.json")
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.json')

# Serialize object to json
with open(filename, 'w', encoding='utf-8') as outfile:
    handler.write_json(export_able_object, outfile)
print("Json written to output.json")

# Deserialize json to object
with open(filename, 'r', encoding='utf-8') as json_file:
    obj: Wrapper = handler.read_json(json_file)
print("Json read from output.json")










