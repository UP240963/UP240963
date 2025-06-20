letra = 'p|'
print(letra)
print(len(letra))
greeting ='Hola Mundo'
print(greeting)
print(len(greeting))
enunciado= 'Espero que estés disfrutando de estos los 30 días en Python'
print(enunciado)
multiline_string=''' Soy estudiante de la UPA en la carrera de tecnologías de la inovación e información digital, esto es lo que he creado con los recursos de los 30 días de python'''
print(multiline_string)
primer_nombre='Alexa'
apellido='Hernández'
espacio=' '
fullname=primer_nombre+espacio+apellido
print(fullname)
print(len(primer_nombre))
print(len(apellido))
print(len(primer_nombre)>len(apellido))
print(len(fullname))
print(len(primer_nombre))
print(len(apellido))
print(len(primer_nombre)>len(apellido))
print(len(fullname))
language= 'Alexa'
a,b,c,d,e=language
print(a)
print(b)
print(c)
print(d)
print(e)
language= 'Alexa'
primeraletra= language [0]
print(primeraletra)
second_letter = language[1]
print(second_letter) 
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
last_letter = language[-1]
print(last_letter) 
second_last = language[-2]
print(second_last)
language = 'Lidia'
first_three = language[0:3] 
last_three = language[3:5]
print(last_three)
language='Ana Lidia'
pto= language[0:6:2]
print(pto)
print('Espero que sea de su agrado las modificaciones que le hice a los textos de los 30 días de python')
print('Días\tTopicos\tEjercicios')
print(' 1\t3\t5')
print(' 2\t3\t5')
print(' 3\t3\t5')
print(' 4\t3\t5')
print('Este es el símbolo del guión al revés (\\)')
print('En todos los lenguajes de programación se inicia con un "Hola Mundo"')
challenge= 'treinta días de python'
print(challenge.capitalize())
challenge='Treinta días de python'
print(challenge.count('y')) 
print(challenge.count('a', 7, 14)) 
print(challenge.count('d'))
challenge='Treinta días de python'
print(challenge.endswith('on'))   
print(challenge.endswith('tion'))
challenge = 'Treinta días de python'
print(challenge.find ('y'))
print(challenge.find('a'))
primernombre= 'Alexa'
apellidos= 'Pineda'
job= 'Estudiante'
País= 'México'
Sentence= 'Yo soy {} {}. Soy {}. Vivo en {}.'.format(primernombre, apellidos, job, País)
print(Sentence)
radius = 10
pi = 3.14
area = pi 
result = 'El área del círculo con {} es {}'.format(str(radius), str(area))
print(result)
challenge= 'Treinta días de python'
print(challenge.find('d'))
print(challenge.find('t'))
challenge = 'TreintaDíasPython'
print(challenge.isalnum())
challenge = '30DíasPython'
print(challenge.isalnum()) 
challenge = 'treinta días de python'
print(challenge.isalnum()) 
challenge = 'treinta días de python 2023'
print(challenge.isalnum())
challenge = 'treinta días python'
print(challenge.isalpha()) 
num = '123'
print(num.isalpha())   
challenge = '30 días python'
print(challenge.find('y'))  
print(challenge.find('d')) 
challenge = 'Treinta'
print(challenge.isdigit()) 
challenge = '30'
print(challenge.digit())   
num = '10'
print(num.isdecimal()) 
num = '10.5'
print(num.isdecimal()) 
challenge = '30DíasDePython'
print(challenge.isidentifier())
challenge = 'treinta_días_de_python'
print(challenge.isidentifier())
challenge = 'Alexa Pineda'
print(challenge.islower()) 
challenge = 'Alexa Hernández'
print(challenge.islower())
challenge='treinta días de python'
print(challenge.isupper())
challenge='TREINTA DÍAS DE PYTHON'
print (challenge.isupper())
num='8'
print(num.isnumeric)
print('eight'.isnumeric)
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)
challenge = ' Alexa Hernández '
print(challenge.strip('a'))
challenge = 'treinta días de python'
print(challenge.replace('python', 'coding'))
challenge= 'Treinta días de python'
print(challenge.split())
challenge='treinta días de python'
print(challenge.title())
challenge='treinta días de python'
print(challenge.swapcase())
challenge='Treinta días de python' 
print(challenge.startswith('treinta')) # True
challenge = '30 días de python'
print(challenge.startswith('treinta'))
