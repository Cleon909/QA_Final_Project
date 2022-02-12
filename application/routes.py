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
        papers_result = Papers.query.filter_by(id=form.title.data).first()
        return render_template('index.html',form=form, total_number=total_number, academics_result=academics_result , papers_result=papers_result)
    else:
        total_number = {'number_of_academics': Academics.query.count(),
        'number_of_papers': Papers.query.count()}
        return render_template('index.html', form=form, total_number=total_number) 


@app.route('/update_academic', methods = ['GET', 'POST'])
def update_academic():
    form = UpdateAcademicForm()
    form.academic_object.choices = [(g.id, g.name) for g in Academics.query.order_by('name')]

    if request.method == 'POST':
        acad = Academics.query.get(form.academic_object.data)
        if form.name != '':
            acad.name = form.name.data
        if form.current_institution.data != '':
            acad.current_institution = form.current_institution.data
        if form.field_of_study.data != '':
            acad.field_of_study = form.field_of_study.data
        db.session.commit()
        return render_template('update_academic.html', acad=acad)
    else:
        init = True
        return render_template('update_academic.html', form=form, init=init) 



@app.route('/update_paper', methods = ['GET', 'POST'])
def update_paper():
    form = UpdatePaperForm()
    form.paper_object.choices = [(g.id, g.title) for g in Papers.query.order_by('title')]

    if request.method == 'POST':
        pap = Papers.query.get(form.paper_object.data)
        if form.title.data != '':
            pap.title = form.title.data
        if form.year_published.data != '':
            pap.year_published = form.year_published.data
        if form.field_of_study.data != '':
            pap.field_of_study = form.field_of_study.data
        db.session.commit()
        return render_template('update_paper.html', pap=pap)
    else:
        init = True
        return render_template('update_paper.html', form=form, init=init)

        return
        #code here to amend the object
    return


@app.route('/add_academic', methods = ['GET', 'POST'])
def add_academic():
    form = AddAcademicForm()
    if request.method == 'POST':
        name = form.name.data
        current_institution = form.current_institution.data
        field_of_study = form.field_of_study.data
        academic = Academics(name, current_institution, field_of_study)
        db.session.add(academic)
        db.session.commit()
        return render_template('add_academic.html', academic=academic)
    else:
        return render_template('add_academic.html', form=form)



@app.route('/add_paper', methods = ['GET', 'POST'])
def add_paper():
    form = AddPaperForm()
    form.authors1.choices = [(g.id, g.name) for g in Academics.query.order_by('name')] 
    form.authors2.choices = [(g.id, g.name) for g in Academics.query.order_by('name')]
    form.authors3.choices = [(g.id, g.name) for g in Academics.query.order_by('name')]
    form.authors4.choices = [(g.id, g.name) for g in Academics.query.order_by('name')]

    if request.method == 'POST':
        title = form.title.data
        year_published = form.year_published.data
        field_of_study = form.field_of_study.data
        paper = Papers(title, year_published, field_of_study)
        db.session.add(paper) #work out how to add authors to child table
        db.session.commit()
        authors = []
        if form.no_of_authors.data == '1':
            author1 = Authors(form.authors1.data, paper.id)
            db.session.add(author1)
            db.session.commit()
            authors.append(author1)
        if form.no_of_authors.data == '2':
            author1 = Authors(form.authors1.data, paper.id)
            db.session.add(author1)
            db.session.commit()
            authors.append(author1)
            author2 = Authors(form.authors2.data, paper.id)
            db.session.add(author2)
            db.session.commit()
            authors.append(author2)
        if form.no_of_authors.data == '3':
            author1 = Authors(form.authors1.data, paper.id)
            db.session.add(author1)
            db.session.commit()
            authors.append(author1)
            author2 = Authors(form.authors2.data, paper.id)
            db.session.add(author2)
            db.session.commit()
            authors.append(author2)
            author3 = Authors(form.authors3.data, paper.id)
            db.session.add(author3)
            db.session.commit()
            authors.append(author3)
        if form.no_of_authors.data == '4':
            author1 = Authors(form.authors1.data, paper.id)
            db.session.add(author1)
            db.session.commit()
            authors.append(author1)
            author2 = Authors(form.authors2.data, paper.id)
            db.session.add(author2)
            db.session.commit()
            authors.append(author2)
            author3 = Authors(form.authors3.data, paper.id)
            db.session.add(author3)
            db.session.commit()
            authors.append(author3)
            author4 = Authors(form.authors4.data, paper.id)
            db.session.add(author4)
            db.session.commit()
            authors.append(author4)
        academic_authors = []
        for author in authors:
            academic_authors.append(Academics.query.filter_by(id=author.academic_id).first())
        return render_template('add_paper.html', paper=paper, academic_authors=academic_authors)
    else:
        return render_template('add_paper.html', form=form)

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

