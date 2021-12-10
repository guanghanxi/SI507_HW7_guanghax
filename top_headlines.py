from flask import Flask, render_template
import secrets
import requests

def get_stories():
    NYT_API = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    print(secrets.api_key)
    param = {'api-key': secrets.api_key}
    results = requests.get(NYT_API, param).json()
    return results['results'][:5]

def get_link(stories_list):
    stories = []
    for element in stories_list:
        stories.append([element['title'], element['url']])
    return stories

def get_image(stories_list):
    stories = []
    for element in stories_list:
        media_list = element['multimedia']
        with_image = False
        for media in media_list:
            if media['type'] == 'image':
                stories.append([element['title'], element['url'], media['url'], media['caption']])
                with_image = True
                break
        if with_image == False:
            stories.append([element['title'], element['url'], '', 'No Thumbnail'])
    return stories

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name = nm)

@app.route('/headlines/<nm>')
def headline_name(nm):
    five_stories = get_stories()
    headlines_page = f"<h1>Hello, {nm}!</h1> <p>Today's technology headlines are...</p> <ol>"
    for element in five_stories:
        headlines_page += f"<li>{element['title']}</li>"
    headlines_page += "</ol>"
    return headlines_page

@app.route('/links/<nm>')
def link_name(nm):
    five_stories = get_link(get_stories())
    return render_template('link.html', name = nm, headlines = five_stories)

@app.route('/images/<nm>')
def image_name(nm):
    five_stories = get_image(get_stories())
    return render_template('table_image.html', name = nm, headlines = five_stories)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)