import pathlib
import textwrap

import google.generativeai as genai

import PIL.Image

img = PIL.Image.open('image.jpg')


# Used to securely store your API key

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=('AIzaSyC4tS3rn-LtGI_g3dkShwoN-wYRxwoIAX8')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


#model = genai.GenerativeModel('gemini-pro')

#response = model.generate_content("What is the meaning of life?")


model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

print(response.text)  #to_markdown idi çalışmadı

print(response.text)