from flask import Flask, render_template, request, redirect, url_for
from app import db
from app.models import Book


def create_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add', methods=['GET', 'POST'])
    def add_book():
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            isbn = request.form['isbn']
            new_book = Book(title=title, author=author, isbn=isbn)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('list_books'))
        return render_template('add_book.html')

    @app.route('/books')
    def list_books():
        books = Book.query.all()
        return render_template('book_list.html', books=books)

    @app.route('/search', methods=['GET', 'POST'])
    def search():
        if request.method == 'POST':
            search_title = request.form['title']
            books = Book.query.filter(Book.title.contains(search_title)).all()
            return render_template('search.html', books=books, search_title=search_title)
        return render_template('search.html', books=None)
