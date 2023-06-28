from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django import db
import sqlite3
import random

def index(request):
    if request.method == "POST":
        my_path = "C:\\Users\\kyrill\\Documents\\GitHub\\Django_python\\Kl1rik_test_project\\feedback.db"
        connection = sqlite3.connect(my_path)
        cursor = connection.cursor()
 
        name = request.POST.get("name")
        age_group = request.POST.get("age_group")
        feedback = request.POST.get("feedback")
        print(name,age_group,feedback)
        cursor.execute("INSERT INTO Feedback (Name,AgeGroup,Feedback) VALUES (?,?,?)",(name,age_group,feedback,))
        connection.commit()
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