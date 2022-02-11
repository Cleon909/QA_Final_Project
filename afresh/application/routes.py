from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Academics, Papers, Authors
from application.forms import SearchDatabaseForm, UpdateAcademicForm, UpdatePaperForm, AddAcademicForm, AddPaperForm, DeleteAcademicForm, DeletePaperForm 



@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = SearchDatabaseForm()
    form.name.choices = [(g.id, g.name) for g in Academics.query.order_by('name')]
    form.title.choices = [(g.id, g.title) for g in Papers.query.order_by('title')]

    if request.method == 'POST':
        total_number = {'number_of_academics': Academics.query.count(),
        'number_of_papers': Papers.query.count()}
        academics_result = Academics.query.filter_by(id=form.name.data).first()

        #code below uses child table to find papers for author
        papers_id = [g.paper_id for g in Authors.query.filter_by(academic_id = form.name.data)]
        papers_by_author = []
        for pap in papers_id:
            papers_by_author.append(Papers.query.filter_by(id = pap).first())

        papers_result = Papers.query.filter_by(id=form.title.data).first()
         # code below uses child table to find aythors of paper
        acad_id = [g.academic_id for g in Authors.query.filter_by(paper_id = form.title.data)]
        authors_of_paper = []
        for acad in acad_id:
            authors_of_paper.append(Academics.query.filter_by(id = acad).first())

        return render_template('index.html',form=form, total_number=total_number, academics_result=academics_result, papers_by_author=papers_by_author, papers_result=papers_result, authors_of_paper=authors_of_paper)
    else:
        total_number = {'number_of_academics': Academics.query.count(),
        'number_of_papers': Papers.query.count()}
        return render_template('index.html', form=form, total_number=total_number) 


@app.route('/update_academic', methods = ['GET, POST'])
def update_academic():
    form = UpdateAcademicForm
    list_of_academics = []
    if form.academic_object.data == None:
        list_of_academics = Academics.query.all()
    else:
        Academics.query.filter_by(id=form.academic_object.data).all() #this hopefully will filter by what is entered into field
    #methods here will post from update fields
    if len(list_of_academics) == 1:
        return
        #then the fields to update will appear and will post to the list_of_academics[0] object. 
    return

@app.route('/update_paper', methods = ['GET, POST'])
def update_paper():
    form = UpdatePaperForm
    list_of_papers = []
    if form.paper_object.data == None:
        list_of_papers = Papers.query.all()
    else:
        Papers.query.filter_by(id=form.paper_object.data).all()
    if len(list_of_papers) == 1:
        return
        #code here to amend the object
    return


@app.route('/add_academic')
def add_academic():
    form = AddAcademicForm()
    name = form.name.data
    current_institution = form.current_instition.data
    field_of_study = form.field_of_study.data
    academic = Academics(name, current_institution, field_of_study)
    db.session.add(academic)
    db.session.commit()
    return (url_for('index'))

@app.route('/add_paper')
def add_paper():
    form = AddPaperForm()
    title = form.title.data
    date_published = form.date_published.data
    field_of_study = form.field_of_study.data
    authors = None # this should feed into a method that should add lines ot the child database , with the same paper_id and a new entry for each academic id
    paper = Papers(title, date_published, field_of_study)
    db.session.add(paper) #work out how to add authors to child table
    db.commit()
    return

@app.route('/delete_academic')
def delete_academic():
    form = DeleteAcademicForm()
    list_of_academics = []
    if form.academic_object.data == None:
        list_of_objects = Academics.query.all()
    else:
        list_of_objects = Academics.query.filter_by(id=form.academic.data)
    # method to delete here
    return

@app.route('/delete_paper')
def delete_paper():
    form = DeletePaperForm()
    list_of_papers = []
    if form.paper_object.data == None:
        list_of_papers = Papers.query.all()
    else:
        list_of_papers = Papers.query.filter_by(id=form.paper_object.data).all()
    # method to delete
    return

@app.route('/about')
def about():
    return
