from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
from .models import Story, Category

def story_list(request, category_slug=None): #used in urls.py for tagging
    category=None
    categories=Category.objects.all()
    story=Story.objects.all()
    paginator = Paginator(story,4)
    page = request.GET.get('page') #takes current number of page`

    try:
        story=paginator.page(page)
    except PageNotAnInteger:
        story=paginator.page(1)
    except EmptyPage:
        story=Paginator.page(paginator.num_pages)
    if category_slug:   #user clicks category
        story = Story.objects.all()
        category=get_object_or_404(Category,slug=category_slug)
        #searching from Category model w/ slug is attribute of Category class
        #user clicks on category,
        story=story.filter(category=category)   #must return object(story), not model
        # user selects the category
        paginator = Paginator(story,4)
        page = request.GET.get('page') #takes current number of page`
        try:
            story=paginator.page(page)
        except PageNotAnInteger:
            story=paginator.page(1)
        except EmptyPage:
            story=Paginator.page(paginator.num_pages)



    return render(request,'story/story_list.html',{'categories':categories,
                        'story':story,'category':category,
                        'page':page})
                        # 'category' is the unique category selected by user,
                        # note 'story' variable is dynamic


def story_detail(request,id):
    story = get_object_or_404(Story, id=id) # filter them by their id

    return render(request, 'story/story_detail.html', context = {'story':story})
