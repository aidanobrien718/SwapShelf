from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # is_staff is Django's privilege flag and gates the department desk, so it
        # must never be editable from a user-facing form. Leaving it here let any
        # member POST is_staff=on and promote themselves. Only safe profile fields.
        fields = ["first_name", "last_name", "email"]
