import selectable.radioselect
from django import forms
from django.forms.util import ErrorList
from django.forms import ModelForm
from django.contrib.comments.forms import CommentDetailsForm

from testapp2.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','location','time','repeat','repeat_amount','repeat_unit','repeats')

    repeat = selectable.radioselect.RadioSelectField(
        choices = (
            [(False, 'Does Not Repeat')],
            [(True, 'Repeats')]
            )
        )
    repeat_amount = forms.IntegerField(label="Times")
    repeat_unit = selectable.radioselect.RadioSelectField(
        choices = (
            [(1, 'Day(s)')],
            [(2, 'Week(s)')],
            [(3, 'Month(s)')]
            )
        )
    name = forms.CharField(label="Headline")
    location = forms.CharField(label="Where?"
