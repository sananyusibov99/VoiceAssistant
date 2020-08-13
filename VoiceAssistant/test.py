import wolframalpha

import io
from urllib.request import urlopen
from tkinter import Tk, Button, Canvas, Label, Toplevel, BOTH
from PIL import Image, ImageTk


def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']


root = Tk()
root.title("Voice Assistant")
root.minsize(500, 500)


query = "Where am i"
app_id = "AQ36PG-QEWLVH4YKE"
client = wolframalpha.Client(app_id)
res = client.query(query)

if res['@success'] == 'false':
   print('Question cannot be resolved')
else:
   result = ''
   pod0 = res['pod'][0]
   pod1 = res['pod'][1]
   
   if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
       result = resolveListOrDict(pod1['subpod'])
       print(result)
   else:
        pic_url = pod1["subpod"]["img"]["@src"]
        print(pod1["subpod"]["img"]["@src"])
        novi = Toplevel()
        canvas = Canvas(novi, width = 500, height = 260)

        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        canvas.create_image(0, 0, image = tk_img, anchor="nw")
        canvas.pack()


root.mainloop()