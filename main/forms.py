from logging import PlaceHolder
from django import forms

class SearchForm(forms.Form):
    source=forms.CharField(label="Source", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Arad', 'value':'Arad', 'class':'form-control'}))
    destination=forms.CharField(label="Destination", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Bucharest', 'value':'Bucharest', 'class':'form-control'}))
    
class AddMapForm(forms.Form):
    
    romania_Cities=forms.CharField(widget=forms.Textarea(attrs={'name':'romania_Cities','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"City1 City2 distance\nCity1 City3 distance\n"})
                          ,initial='Arad Sibiu 140\nArad Timisoara 118\nArad Zerind 75\nBucharest Fagaras 211\nBucharest Giurgiu 90\nBucharest Pitesti 101\nBucharest Urziceni 85\nCraiova Dobreta 120\nCraiova Pitesti 138\nCraiova Rimnicu_Vilcea 146\nDobreta Mehadia 75\nEforie Hirsova 86\nFagaras Sibiu 99\nHirsova Urziceni 98\nIasi Neamt 87\nIasi Vaslui 92\nLugoj Mehadia 70\nLugoj Timisoara 111\nOradea Zerind 71\nOradea Sibiu 151\nPitesti Rimnicu_Vilcea 97\nRimnicu_Vilcea Sibiu 80\nUrziceni Vaslui 142')
    
    heuristic_Value=forms.CharField(widget=forms.Textarea(attrs={'name':'heuristic_Value','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"City1 value\nCity2 value\n"}), initial='Arad 366\nBucharest 0\nCraiova 160\nDobreta 242\nEforie 161\nFagaras 178\nGiurgiu 77\nHirsova 151\nIasi 226\nLugoj 244\nMehadia 241\nNeamt 234\nOradea 380\nPitesti 98\nRimnicu_Vilcea 193\nSibiu 253\nTimisoara 329\nUrziceni 80\nVaslui 199\nZerind 374')