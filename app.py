from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

def load_data():
    tree = ET.parse('data/data.xml')
    return tree.getroot()

@app.route('/')
def home():
    root = load_data()
    personal = root.find('personal')
    return render_template('home.html', personal=personal)

@app.route('/portfolio')
def portfolio():
    root = load_data()
    projects = root.find('projects')
    return render_template('portfolio.html', projects=projects)

@app.route('/skills')
def skills():
    root = load_data()
    skills = root.find('skills')
    return render_template('skills.html', skills=skills)

@app.route('/organizations')
def organizations():
    root = load_data()
    orgs = root.find('organizations')
    return render_template('organizations.html', orgs=orgs)

@app.route('/services')
def services():
    root = load_data()
    services = root.find('services')
    return render_template('services.html', services=services)

@app.route('/testimonials')
def testimonials():
    root = load_data()
    testimonials = root.find('testimonials')
    return render_template('testimonials.html', testimonials=testimonials)

@app.route('/contact')
def contact():
    root = load_data()
    contact = root.find('contact')
    return render_template('contact.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True)
