from knox_source_data_io.models.publication import *
from knox_source_data_io.io_handler import *
import os

# Generate publication
publication = Publication()
publication.publisher = "Nordjyske Medier"
publication.published_at = "Some time"
publication.publication = "A newspaper"
publication.pages = 0

# Generate article
article = Article()
article.headline = "Some headline..."
article.subhead = ""
article.lead = ""
article.byline = Byline(name="Hans", email="hans@hansen.net")
article.extracted_from.append("/path/to/source-file")
article.confidence = 1.0
article.id = 0
article.page = 0

for x in range(10):
    p = Paragraph()
    p.kind = "paragraph"
    p.value = f'This is paragraph number {x}'
    article.add_paragraph(p)

publication.add_article(article)

# Generate
handler = IOHandler(Generator(app="This app", version=1.0), "link/to/schema.json")
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.json')

# Serialize object to json
with open(filename, 'w', encoding='utf-8') as outfile:
    handler.write_json(publication, outfile)
print("Json written to output.json")

# Deserialize json to object
with open(filename, 'r', encoding='utf-8') as json_file:
    obj: Wrapper = handler.read_json(json_file)
print("Json read from output.json")
