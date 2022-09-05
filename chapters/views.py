from django.shortcuts import render, redirect
from .models import Chapter
from .forms import ChapterForm
from .models import Picture
from .forms import PictureForm


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
    pictures = chapter.picture_set.all()

    context = {'chapter': chapter, 'pictures': pictures}
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


def create_picture(request):
    form = PictureForm()

    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chapter')

    context = {'form': form}
    return render(request, 'chapters/picture_form.html', context)


def update_picture(request, pk):
    picture = Picture.objects.get(id=pk)
    form = PictureForm(instance=picture)

    if request.method == 'POST':
        form = PictureForm(request.POST, instance=picture)
        if form.is_valid():
            form.save()
            return redirect('chapter')

    context = {'form': form}
    return render(request, 'chapters/picture_form.html', context)


def delete_picture(request, pk):
    picture = Picture.objects.get(id=pk)

    if request.method == 'POST':
        picture.delete()
        return redirect('chapter')

    return render(request, 'chapters/delete.html', {'obj': picture})
