from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['Paras'] = 'Python'
favorite_languages['Anmol'] = 'C++'
favorite_languages['Manoj'] = 'PHP'
print(favorite_languages.items())
for name, language in favorite_languages.items():
    print(name.title()+"`s favorite language is "+ language.title()+'.')
