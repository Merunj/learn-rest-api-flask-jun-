from requests import get, post, put

print(put('http://localhost:5000/api/user/2',
           json={'name': 'Владимир',
                 'about': 'Врач',
                 'email': '47hospital@gmail.com'}).json())