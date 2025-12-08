from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Добавьте изображение'
            }
        )

        self.fields['category'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            }
        )

        self.fields['purchase_price'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }
        )
