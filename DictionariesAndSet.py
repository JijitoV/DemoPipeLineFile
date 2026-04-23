set1 = {25, 'Jijito', 25, 20.4, 'Navin'}
print(set1)
dict1 = {
    'Name' : 'jijito', 
    'Age' : 26, 
    'Language' : {'tamil', 'english', 'malayalam'}, 
    'Programming' : {'Frontend' : ['html', 'css'], 'Backend' : {'java', 'python'}, 'Tool' : {'java': {'eclipse','vscode'}}  }
    }
print(dict1['Programming']['Tool']['java'])
print(dict1.get('Lang', 'Not Found'))