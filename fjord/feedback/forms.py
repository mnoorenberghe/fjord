from django import forms

from tower import ugettext as _


class URLInput(forms.TextInput):
    """Text field with HTML5 URL Input type."""
    input_type = 'url'


class ResponseForm(forms.Form):
    """Basic response feedback form."""

    # NB: The class 'url' is hard-coded in the Testpilot extension to
    # accommodate pre-filling the field client-side.
    url = forms.URLField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'http://', 'class': 'url'}))

    description = forms.CharField(widget=forms.Textarea(), required=True)
    # required=False means this allowed to be False, not that it can
    # be blank.
    happy = forms.BooleanField(required=False, widget=forms.HiddenInput())

    email_ok = forms.BooleanField(required=False)
    email = forms.EmailField(required=False)

    # These are hidden fields on the form which we have here so we can
    # abuse the fields for data validation.
    manufacturer = forms.CharField(required=False, widget=forms.HiddenInput(
            attrs={'class': 'manufacturer'}))
    device = forms.CharField(required=False, widget=forms.HiddenInput(
            attrs={'class': 'device'}))

    def clean(self):
        cleaned_data = super(ResponseForm, self).clean()

        email_ok = cleaned_data.get('email_ok')
        email = cleaned_data.get('email')

        if email_ok and not email or 'email' in self._errors:
            self._errors['email'] = self.error_class([
                    _(u'Please enter a valid email address, or uncheck the '
                      'box allowing us to contact you.')
            ])

        # If email_ok is not checked, ignore errors on email.
        if not email_ok and 'email' in self._errors:
            del self._errors['email']

        return cleaned_data

    def clean_description(self):
        # If the response description consists solely of whitespace,
        # kick up an error.
        description = self.cleaned_data.get('description')
        if not description or not description.strip():
            raise forms.ValidationError(_(u'This field is required.'))

        return description
