# ProjectRescue

commands to be executed to run the project-:
<pre>
pip3 install django-cors-headers
pip3 install django-rest-framework
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 
pip3 install channels_redis
docker run -p 6379:6379 -d redis:2.8

</pre>
The project will start on http://localhost:8000/home/

<h3>API'S-:</h3>

1) /save_user/
 
   <h4>method-: POST</h4>
   <h4>body-: </h4>
   <pre>
       name-:String,
       phone_number-: Integer,
       detail-: JSON Object having keys and value. (example-: {"address":"415/12,jiya lal gate", "school":"BVM", "roll_numer":"10"} ),
       firebase_token-: String
    </pre>

2) /save_message/

   <h4>method-: POST</h4>
   <h4>body-: </h4>
   <pre>
       phone_number-: Integer,
       message-:String
    </pre>
