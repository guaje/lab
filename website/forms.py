from django.forms import ModelForm
from .models import *


class EditFixedSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown']


class AddEditPageSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown',
                  'website_position_id',
                  'show_in_nav']


class AddEditBlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'authors']


class AddEditNewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'body_markdown', 'post_date', 'description']


class AddEditPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'url', 'author', 'doi', 'entry_type',
                  'published_in', 'publisher', 'year_of_publication',
                  'month_of_publication', 'bibtex']


class AddEditCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'acronym', 'level', 'prerequisite', 'description',
                  'syllabus']


class AddEditCarouselImageForm(ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image_url', 'image_caption',
                  'image_description', 'target_url']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar_img', 'contact_number', 'contact_url', 'description',
                  'profile_page_markdown']
