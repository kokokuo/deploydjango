from django import forms
from . models import ImageModel

class ImageModelForm(forms.ModelForm):
	class Meta:
		model = ImageModel

		labels = {
			'img_name': '圖片名稱',
			'image': '上傳圖片'
		}