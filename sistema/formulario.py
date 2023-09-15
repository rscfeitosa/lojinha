from django.forms import ModelForm
from sistema.models import Produto

# Create the form class.
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "valor", "data_de_validade","quantidade"]


