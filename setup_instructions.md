# 🎄 Christmas Advert Review Website

A beautiful, festive web application for reviewing Christmas adverts from major UK brands!

## Features

- ✨ Multi-step review form with star ratings
- 🎅 Beautiful Christmas forest theme with gold accents
- 📊 Real-time results dashboard with charts
- 💬 User comments display
- ❄️ Animated snowflakes
- 📱 Fully responsive design

## Quick Start

### 1. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Project Structure

Create the following folder structure:

```
christmas-adverts/
├── app.py
├── requirements.txt
└── templates/
    ├── base.html
    ├── welcome.html
    ├── thank_you.html
    └── results.html
```

### 3. Create the Files

Copy each artifact into its respective file:
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `templates/base.html` - Base template with Christmas theme
- `templates/welcome.html` - Main review form
- `templates/thank_you.html` - Thank you page
- `templates/results.html` - Results dashboard

### 4. Run the Application

```bash
python3 app.py
```

The app will start at: **http://127.0.0.1:5000**

## How It Works

1. **Welcome Screen** - Users enter their name
2. **Review Screens** - Rate 6 brands (Amazon, Tesco, Waitrose, John Lewis, Sainsbury's, Barbour)
3. **Thank You Screen** - Confirmation message
4. **Results Screen** - View all responses with:
   - Average ratings for each brand
   - Rating distribution charts
   - User comments

## Database

- Uses SQLite (`christmas_reviews.db`) - automatically created on first run
- All reviews are stored persistently
- No manual database setup required!

## Customization

### Change Brands
Edit the `brands` list in `app.py` and update the corresponding review screens in `welcome.html`

### Modify Colors
Update the Tailwind classes in the templates:
- Gold accents: `gold-shine`, `border-amber-400`
- Christmas green: `bg-emerald-*`

### Add More Questions
1. Add fields to the `Review` model in `app.py`
2. Add corresponding form fields in `welcome.html`
3. Update the results calculation in the `/results` route

## Deployment

For production deployment:

1. **Change the secret key** in `app.py`:
   ```python
   app.config['SECRET_KEY'] = 'your-secure-random-key'
   ```

2. **Use a production server** (not Flask's development server):
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **Consider using PostgreSQL** for better performance with many users

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge
- Firefox
- Safari
- Mobile browsers

## Features Highlights

- **Animated Background**: Christmas forest with falling snow
- **Interactive Stars**: Click to rate with visual feedback
- **Progress Tracking**: Multi-step form with back/next buttons
- **Beautiful Charts**: Gold-themed bar charts for rating distributions
- **Comments Section**: Display all user feedback
- **Print Support**: Print results directly from the browser

## Troubleshooting

**Database doesn't exist?**
- Delete `christmas_reviews.db` and restart the app - it will recreate automatically

**Port 5000 already in use?**
- Change the port in `app.py`: `app.run(debug=True, port=5001)`

**CSS not loading?**
- Make sure you have internet connection (Tailwind loads from CDN)

Enjoy your festive review session! 🎅✨