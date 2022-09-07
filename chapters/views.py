from django.shortcuts import render, redirect
from .models import Chapter
from .forms import ChapterForm
from .models import Picture
from .forms import PictureForm
import base64


# Create your views here.


# chapters = [
#     {'id': 1, 'name': 'Chapter 1'},
#     {'id': 2, 'name': 'Chapter 2'},
#     {'id': 3, 'name': 'Chapter 3'}
# ]


def home(request):
    chapters = Chapter.objects.all()

    context = {'chapters': chapters}
    return render(request, 'chapters/home.html', context)


def chapter(request, pk):
    chapter = Chapter.objects.get(id=pk)
    picture = chapter.picture_set.all()

    context = {'chapter': chapter, 'picture': picture}
    return render(request, 'chapters/chapter.html', context)


def create_chapter(request):
    form = ChapterForm()

    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'chapters/chapter_form.html', context)


def update_chapter(request, pk):
    chapter = Chapter.objects.get(id=pk)
    form = ChapterForm(instance=chapter)

    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'chapters/chapter_form.html', context)


def delete_chapter(request, pk):
    chapter = Chapter.objects.get(id=pk)

    if request.method == 'POST':
        chapter.delete()
        return redirect('home')

    return render(request, 'chapters/delete.html', {'obj': chapter})


def create_picture(request, chapter_pk):
    chapter = Chapter.objects.get(id=chapter_pk)
    name = ""
    img = ""

    if request.method == 'POST':
        name = request.POST["name"]
        image = request.FILES["image"]
        encodedBytes = base64.b64encode(image.encode("utf-8"))
        img = str(encodedBytes, "utf-8")

        picture = Picture(chapter=chapter, name=name, img=img)
        picture.save()
        return redirect('chapter')

    context = {'chapter': chapter, 'name': name, 'img': img}
    return render(request, 'chapters/picture_form.html', context)


def update_picture(request, pk):
    picture = Picture.objects.get(id=pk)
    name = ""
    img = ""

    if request.method == 'POST':
        name = request.POST["name"]
        image = request.FILES["image"]
        encodedBytes = base64.b64encode(image.encode("utf-8"))
        img = str(encodedBytes, "utf-8")

        picture.name = name
        picture.img = img
        picture.save()

        return redirect('chapter')

    context = {'name': name, 'img': img}
    return render(request, 'chapters/picture_form.html', context)


def delete_picture(request, pk):
    picture = Picture.objects.get(id=pk)

    if request.method == 'POST':
        picture.delete()
        return redirect('chapter')

    return render(request, 'chapters/delete.html', {'obj': picture})
