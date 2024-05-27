import os
import pytest

from fileforge.client import Fileforge
from fileforge.types.generate_request_options import GenerateRequestOptions

FILEFORGE_API_KEY = "YOUR_API_KEY"

# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="Unimplemented")
def test_client() -> None:
    assert True == True

def test_generate_pdf_link():
    cwd = os.path.dirname(__file__) #<-- absolute dir the script is in

    HTML = open(os.path.join(cwd, "test.html"), "rb")
    CSS = open(os.path.join(cwd, "test.css"), "rb")

    html_file = ("index.html", HTML, "text/html")
    css_file = ("style.css", CSS, "text/css")

    ff = Fileforge(api_key=FILEFORGE_API_KEY)
    optionsValue = GenerateRequestOptions(host=True, test = False)
    pdf_iter = ff.generate(
        options= optionsValue,
        files=[html_file, css_file]
    )

    pdf_content = bytearray()
    for chunk in pdf_iter:
        pdf_content.extend(chunk)
    
    pdf_base64_string = pdf_content.decode('utf-8')
    print(pdf_base64_string)
    assert len(pdf_content) > 0