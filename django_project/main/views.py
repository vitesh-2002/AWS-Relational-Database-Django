from django.shortcuts import render, HttpResponse
from random import randint, choice, shuffle
import datetime
import json
from main.models import *
# Create your views here.
def main_page(request):
    myList = [1, 2, 3, 4]
    myRandom = randint(0,10)
    return HttpResponse(f"<h1 style = 'color: red;'>{myList}:{myRandom}</h1>")

def quiz_page(request):
    all_questions = Question.objects.filter(quiz_id = 8)
    for question in all_questions:
        question.shuffled_answers = [question.correct_answer,
                                     question.incorrect_answer]
        shuffle(question.shuffled_answers)
        print(question.shuffled_answers)
    '''
    print("Question: " + all_questions[0].text)
    print("Correct Answer: " + all_questions[0].correct_answer)
    print("Quiz: " + all_questions[0].quiz.title)
    '''

    return render(request = request,
                  template_name = "main/quizzes.html",
                  context = {"num": 100,
                             "all_questions": all_questions})



def login_page(request):
    '''
    randDuration = randint(20,30)
    randOpen = choice([True, False])
    new_quiz = Quiz(duration = randDuration, is_open = randOpen)
    new_quiz.save()
    '''
    '''trickQ = Question(text = "What is 1 divided by 0", points = 10, correct_answer = "undefined", incorrect_answer = "1", quiz_id = 8)
    trickQ.save()'''

    allquizzes = Quiz.objects.all()
    print(allquizzes)
    open_quizzes = Quiz.objects.filter(is_open = True).order_by('quizOrder')
    returnedresult = Quiz.objects.filter(is_open = True, title = "Quiz 01")[0]
    print(returnedresult)
    single = Quiz.objects.get(id=8)
    print(single)
    rand1 = randint(0,100)
    rand2 = randint(0,111)
    randSum = rand1 + rand2
    return render(request = request,
                  template_name = "main/default.html",
                  context={"rand1":rand1,
                           "rand2":rand2,
                           "randsum": randSum,
                           "all_quizzes": open_quizzes,
                           "single":single,
                           "returned": returnedresult})


def week10page(request):

    ##Book.objects.all().delete()
    #Author.objects.all().delete()

    new_book = Book(book_title = "Book 1", genre = "History", publish_date = datetime.datetime.now())
    new_book.save()
    new_author = Author(first_name= "JK", last_name = "Rowling")
    new_author.save()
    second_book = Book(book_title = "Book 2", genre = "Psychology", publish_date = datetime.datetime.now())
    second_book.save()
    second_author = Author(first_name = "Jeff", last_name = "Bezos")
    second_author.save()
    new_author.books.add(new_book)
    new_author.books.add(second_book)
    #use related_name so that you can just use 'authors' to access authors
    new_book.authors.add(second_author)
    #use author_set to access authors without having to use related_name
    '''new_book.author_set.add(second_author)'''
    #print(Book.__dict__)
    return HttpResponse("This is Week 10")


def week12page(request):
    json_string = '{"name": "Jordan", "age":23}'
    result = json.loads(json_string)
    print(result["name"])

    #traditional dictionary
    student_info = {"name": "Jordan", "age":23, "is_student": True, "courses": [], "major": None}
    #convert it to a JSON
    student_info_json = json.dumps(student_info, indent = 4)
    print(student_info_json)
    somebooks = Book.objects.filter(additional_info__age__gt = 50)|Book.objects.filter(additional_info__name="Jordan")
    for book in somebooks:
        print(book.book_title)
    print(somebooks)

    mybooks = Book.objects.filter(numofpages__gt=150)
    mybooks = Book.objects.filter(numofpages__in=[150,100])
    print(mybooks)
    return HttpResponse("Testing Week 12")
def discussion_page(request):
    '''
    curr_quiz = Quiz.objects.filter(title = "Quiz 01")
    quiz_id_val = curr_quiz[0].id
    '''
    curr_questions = Question.objects.filter(quiz__title = "Quiz 03")
    print(curr_questions)

    return render(request=request,
                  template_name = "main/discussion.html",
                  context={"curr_questions":curr_questions})
    #return HttpResponse("Discussion Page")
