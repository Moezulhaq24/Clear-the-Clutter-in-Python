import os


def directories(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def filemove(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


files = os.listdir()
files.remove('main.py')
# print(files)
directories('Image')
directories('Docs')
directories('Media')
directories('Others')

imgExtn = ['.png', '.jpg', '.jpeg']
images = [file for file in files if os.path.splitext(file)[
    1].lower() in imgExtn]

docsExtn = ['.txt', '.pdf', 'docs']
docs = [file for file in files if os.path.splitext(file)[
    1].lower() in docsExtn]

mediaExtn = ['.mp4', '.mp3']
media = [file for file in files if os.path.splitext(
    file)[1].lower() in mediaExtn]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExtn) and (ext not in docsExtn) and (ext not in mediaExtn) and os.path.isfile(file):
        others.append(file)

# print(others)
filemove("Media", media)
filemove("Images", images)
filemove("Docs", docs)
filemove("Others", others)


# for medias in media:
#     os.replace(medias, f"Media/{medias}")


# for image in images:
#     os.replace(image, f"Image/{image}")


# for doc in docs:
#     os.replace(doc, f"Docs/{doc}")

# for other in others:
#     os.replace(other, f"Others/{other}")
