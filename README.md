# simpleapi
Api para cadastros ShePlays.

Usa [Flask](https://flask.palletsprojects.com/en/1.0.x/), [MongoDB](https://docs.mongodb.com/) hosteado no [Mlab](https://mlab.com), e está deployada no [PythonAnywhere](https://guidalonso.pythonanywhere.com).


#### Rotas

###### GET: /listUsers

Lista todos os usuários no banco de dados 

###### POST: /newUser 

Cria um usuário, recebe os parâmetros

``` {
    "firstname": ("string", "person's first name"),
    "lastname": ("string", "person's lastname name"),
    "fromEmail": ("string", "person's fromEmail"),
    "games": ("list", "list of games the person plays"),
    "onlineHour": ("string", "descrição de horas ativas da usuária"),
    "nickname": ("string", "person's nickname"),
   } 
```

###### DELETE: /deleteUser/<_userid>  
Deleta uma usuária, recebe o id dessa usuária em forma de string na url

#### setup aplicação local

##### Cria e ativa o virtual env

`virtualenv venvflaskblog`

`source venvsimpleapi/bin/activate`

##### instala os requisitos
`sudo python3 Setup.py install`

##### exporta e roda a aplicação
`export FLASK_APP=app.py`

`flask run`
