from django import forms


class CreateNewTask(forms.Form):
    # Esto es para enviarle al html un input
    # del tipo de dato que le indiquemos
    title = forms.CharField(label='title', max_length=200, required=True,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(
        label='description', widget=forms.Textarea(attrs={'class': 'input'}))


class CreateNewProjects(forms.Form):
    name = forms.CharField(label='name', max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))
