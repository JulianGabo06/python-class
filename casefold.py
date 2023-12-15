# El casefold() sirve para pasar una string a minusculas sin importar
# que en su estado original este en mayusculas o minusculas

# Sin usar el casefold();
text1 = 'CatalinaFS'
text2 = 'catalinaFS'

print(text1 == text2)

# Usando el casefold();
text1 = 'CatalinaFS'
text2 = 'catalinaFS'

print(text1.casefold() == text2.casefold())