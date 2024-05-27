import os
import pytest
import aiofiles
import ast
from fileforge.client import Fileforge, AsyncFileforge, MergeRequestOptions
from fileforge.types.generate_request_options import GenerateRequestOptions

FILEFORGE_API_KEY = os.environ.get("FILEFORGE_API_KEY")

# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="Unimplemented")
def test_client() -> None:
    assert True == True

def test_generate_pdf_buffer():
    cwd = os.path.dirname(__file__) #<-- absolute dir the script is in

    HTML = open(os.path.join(cwd, "test.html"), "rb")
    CSS = open(os.path.join(cwd, "test.css"), "rb")

    html_file = ("index.html", HTML, "text/html")
    css_file = ("style.css", CSS, "text/css")

    ff = Fileforge(api_key=FILEFORGE_API_KEY)
    optionsValue = GenerateRequestOptions(host=False, test = False)
    pdf_iter = ff.generate(
        options= optionsValue,
        files=[html_file, css_file]
    )

    print(pdf_iter)

    output_path = os.path.join(cwd, "output.pdf")
    with open(output_path, "wb") as output_file:
            for chunk in pdf_iter.get("file").iter_bytes():
                output_file.write(chunk)


# @pytest.mark.asyncio
# async def test_generate_pdf_buffer_async():
#     cwd = os.path.dirname(__file__)  # Absolute dir the script is in

#     # Open HTML and CSS files asynchronously
#     async with aiofiles.open(os.path.join(cwd, "test.html"), "rb") as html_file, \
#                aiofiles.open(os.path.join(cwd, "test.css"), "rb") as css_file:

#         html_content = await html_file.read()
#         css_content = await css_file.read()

#         html_file_tuple = ("index.html", html_content, "text/html")
#         css_file_tuple = ("style.css", css_content, "text/css")

#         ff = AsyncFileforge(api_key=FILEFORGE_API_KEY)
#         optionsValue = GenerateRequestOptions(host=False, test=False)
#         pdf_iter = ff.generate(
#             options=optionsValue,
#             files=[html_file_tuple, css_file_tuple]
#         )

#         output_path = os.path.join(cwd, "outputAsync.pdf")
#         async with aiofiles.open(output_path, "wb") as output_file:
#             async for chunk in pdf_iter:
#                 await output_file.write(chunk)

#         print(f"PDF generated successfully and written to {output_path}")

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

    # pdf_content = bytearray()
    # for chunk in pdf_iter:
    #     pdf_content.extend(chunk)
    
    # pdf_base64_string = pdf_content.decode('utf-8')
    # url_object = ast.literal_eval(pdf_base64_string)
    assert 'url' in pdf_iter.json()

# @pytest.mark.asyncio
# async def test_generate_pdf_link_async():
#     cwd = os.path.dirname(__file__)  # Absolute dir the script is in

#     # Open HTML and CSS files asynchronously
#     async with aiofiles.open(os.path.join(cwd, "test.html"), "rb") as html_file, \
#                aiofiles.open(os.path.join(cwd, "test.css"), "rb") as css_file:

#         html_content = await html_file.read()
#         css_content = await css_file.read()

#         html_file_tuple = ("index.html", html_content, "text/html")
#         css_file_tuple = ("style.css", css_content, "text/css")

#         ff = AsyncFileforge(api_key=FILEFORGE_API_KEY)
#         optionsValue = GenerateRequestOptions(host=True, test=False)
#         pdf_iter = ff.generate(
#             options=optionsValue,
#             files=[html_file_tuple, css_file_tuple]
#         )

#         pdf_content = bytearray()
#         async for chunk in pdf_iter:
#             pdf_content.extend(chunk)

#         pdf_base64_string = pdf_content.decode('utf-8')
#         url_object = ast.literal_eval(pdf_base64_string)
#         assert 'url' in url_object

# def test_merge_pdf():
#     cwd = os.path.dirname(__file__)  # Absolute dir the script is in

#     # Open sample PDF files
#     pdf_file1_path = os.path.join(cwd, "output.pdf")
#     pdf_file2_path = os.path.join(cwd, "outputAsync.pdf")

#     with open(pdf_file1_path, "rb") as pdf_file1, \
#          open(pdf_file2_path, "rb") as pdf_file2:

#         pdf_file1_tuple = ("sample1.pdf", pdf_file1, "application/pdf")
#         pdf_file2_tuple = ("sample2.pdf", pdf_file2, "application/pdf")

#         ff = Fileforge(api_key=FILEFORGE_API_KEY)
#         optionsValue = MergeRequestOptions()
#         pdf_iter = ff.merge(
#             options=optionsValue,
#             files=[pdf_file1_tuple, pdf_file2_tuple]
#         )

#         output_path = os.path.join(cwd, "merged_output.pdf")
#         with open(output_path, "wb") as output_file:
#             for chunk in pdf_iter:
#                 output_file.write(chunk)



# @pytest.mark.asyncio
# async def test_merge_pdf_async():
#     cwd = os.path.dirname(__file__)  # Absolute dir the script is in

#     # Open sample PDF files asynchronously
#     async with aiofiles.open(os.path.join(cwd, "output.pdf"), "rb") as pdf_file1, \
#                aiofiles.open(os.path.join(cwd, "outputAsync.pdf"), "rb") as pdf_file2:

#         pdf_file1_content = await pdf_file1.read()
#         pdf_file2_content = await pdf_file2.read()

#         pdf_file1_tuple = ("sample1.pdf", pdf_file1_content, "application/pdf")
#         pdf_file2_tuple = ("sample2.pdf", pdf_file2_content, "application/pdf")

#         ff = AsyncFileforge(api_key=FILEFORGE_API_KEY)
#         optionsValue = MergeRequestOptions()
#         pdf_iter = ff.merge(
#             options=optionsValue,
#             files=[pdf_file1_tuple, pdf_file2_tuple]
#         )

#         output_path = os.path.join(cwd, "merged_output_async.pdf")
#         async with aiofiles.open(output_path, "wb") as output_file:
#             async for chunk in pdf_iter:
#                 await output_file.write(chunk)

#         print(f"PDFs merged successfully and written to {output_path}")