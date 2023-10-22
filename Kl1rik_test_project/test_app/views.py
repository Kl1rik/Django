from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django import db

import mysql.connector
import random























def index(request):
    if request.method == "POST":
        # change host-name for each platform(EX. mysql-pod/mysql-container)
        conn = mysql.connector.connect(
                host='mysql-pod',
                user='test',
                password='testtest',
                database='test'
            )
        cursor = conn.cursor()
        print("connect success")
        name = request.POST.get("name")
        age_group = request.POST.get("age_group")
        feedback = request.POST.get("feedback")
        print(name,age_group,feedback)
        # query = """
        #     CREATE TABLE Feedback (
        #         Name CHAR(255),
        #         AgeGroup CHAR(255),
        #         Feedback CHAR(255)
        #         )
        #     VALUES (%s, %s, %s)
        #     """
        # values = (name,age_group,feedback)
        # cursor.execute(query, values)
        query = """
            INSERT INTO Feedback (Name,AgeGroup,Feedback)
            VALUES (%s, %s, %s)
            """
        values = (name,age_group,feedback)
        cursor.execute(query, values)


        
        conn.commit()
        cursor.execute("SELECT * FROM Feedback")
        rows = cursor.fetchall()
        for row in rows : 
            print(row)
        db.connections.close_all()
        return HttpResponse(f"<h3>Спасибо за ваш отзыв , {name}</h3>" 
                            f"<h3>Всего отзывов : {random.randint(0,999)}</h3>" 
                           )
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})