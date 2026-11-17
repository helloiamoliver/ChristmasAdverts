from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Pull Supabase connection string from Vercel Environment Variables
database_url = os.environ.get('DATABASE_URL', '')
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key-change-me')

db = SQLAlchemy(app)

# Database Models
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    disney_rating = db.Column(db.Integer, nullable=False)
    disney_comment = db.Column(db.Text)
    mands_rating = db.Column(db.Integer, nullable=False)
    mands_comment = db.Column(db.Text)
    waitrose_rating = db.Column(db.Integer, nullable=False)
    waitrose_comment = db.Column(db.Text)
    johnlewis_rating = db.Column(db.Integer, nullable=False)
    johnlewis_comment = db.Column(db.Text)
    lidl_rating = db.Column(db.Integer, nullable=False)
    lidl_comment = db.Column(db.Text)
    argos_rating = db.Column(db.Integer, nullable=False)
    argos_comment = db.Column(db.Text)
    barbour_rating = db.Column(db.Integer, nullable=False)
    barbour_comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables in Supabase if they don't exist yet
with app.app_context():
    if database_url:
        db.create_all()

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/review/<int:step>', methods=['GET', 'POST'])
def review(step):
    if request.method == 'POST':
        if step == 1:
            return redirect(url_for('review', step=2, name=request.form.get('name')))
        elif step < 7:
            return redirect(url_for('review', step=step+1))
    
    brands = ['johnlewis', 'waitrose', 'disney', 'barbour', 'mands', 'lidl', 'argos']
    if step <= len(brands):
        return render_template('review_form.html', step=step, brand=brands[step-1])
    
    return redirect(url_for('thank_you'))

@app.route('/submit', methods=['POST'])
def submit():
    new_review = Review(
        name=request.form.get('name'),
        disney_rating=int(request.form.get('disney_rating')),
        disney_comment=request.form.get('disney_comment', ''),
        mands_rating=int(request.form.get('mands_rating')),
        mands_comment=request.form.get('mands_comment', ''),
        waitrose_rating=int(request.form.get('waitrose_rating')),
        waitrose_comment=request.form.get('waitrose_comment', ''),
        johnlewis_rating=int(request.form.get('johnlewis_rating')),
        johnlewis_comment=request.form.get('johnlewis_comment', ''),
        lidl_rating=int(request.form.get('lidl_rating')),
        lidl_comment=request.form.get('lidl_comment', ''),
        argos_rating=int(request.form.get('argos_rating')),
        argos_comment=request.form.get('argos_comment', ''),
        barbour_rating=int(request.form.get('barbour_rating')),
        barbour_comment=request.form.get('barbour_comment', ''),
    )
    db.session.add(new_review)
    db.session.commit()
    
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/results')
def results():
    reviews = Review.query.all()
    brands = ['johnlewis', 'waitrose', 'disney', 'barbour', 'mands', 'lidl', 'argos']
    stats = {}
    
    for brand in brands:
        ratings = [getattr(r, f'{brand}_rating') for r in reviews]
        comments = [
            {'name': r.name, 'comment': getattr(r, f'{brand}_comment')} 
            for r in reviews if getattr(r, f'{brand}_comment')
        ]
        
        if ratings:
            stats[brand] = {
                'average': round(sum(ratings) / len(ratings), 1),
                'distribution': {i: ratings.count(i) for i in range(1, 11)},
                'comments': comments,
                'total': len(ratings)
            }
    
    return render_template('results.html', stats=stats, brands=brands)

@app.route('/api/stats')
def api_stats():
    reviews = Review.query.all()
    brands = ['johnlewis', 'waitrose', 'disney', 'barbour', 'mands', 'lidl', 'argos']
    stats = {}
    
    for brand in brands:
        ratings = [getattr(r, f'{brand}_rating') for r in reviews]
        if ratings:
            stats[brand] = {
                'average': round(sum(ratings) / len(ratings), 1),
                'distribution': {str(i): ratings.count(i) for i in range(1, 11)},
                'total': len(ratings)
            }
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
